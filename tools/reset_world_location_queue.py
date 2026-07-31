"""Reset interrupted and failed world-location captures for another run."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path
import sqlite3


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATABASE = (
    ROOT
    / "converted"
    / "world-location-database"
    / "full-world"
    / "locations.sqlite3"
)


def queue_counts(connection: sqlite3.Connection) -> dict[str, int]:
    return {
        str(status): int(count)
        for status, count in connection.execute(
            """SELECT queue_status,COUNT(*)
               FROM places
               WHERE queue_status IN ('failed','in_progress')
               GROUP BY queue_status"""
        )
    }


def reset_queue(database: Path) -> tuple[dict[str, int], int, dict[str, int], int]:
    if not database.is_file():
        raise FileNotFoundError(f"world-location database not found: {database}")

    connection = sqlite3.connect(database)
    try:
        before = queue_counts(connection)
        connection.execute("BEGIN IMMEDIATE")
        cursor = connection.execute(
            """UPDATE places
               SET queue_status='pending',failure_code=NULL,failure_detail=NULL,updated_at=?
               WHERE scope_status='in_scope'
                 AND queue_status IN ('failed','in_progress')""",
            (datetime.now(UTC).isoformat(timespec="milliseconds"),),
        )
        connection.commit()
        after = queue_counts(connection)
        pending = int(
            connection.execute(
                """SELECT COUNT(*) FROM places
                   WHERE scope_status='in_scope' AND queue_status='pending'"""
            ).fetchone()[0]
        )
        return before, cursor.rowcount, after, pending
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Reset all in-scope failed and interrupted world-location captures "
            "to pending."
        )
    )
    parser.add_argument(
        "--database",
        type=Path,
        default=DEFAULT_DATABASE,
        help=f"SQLite database (default: {DEFAULT_DATABASE})",
    )
    args = parser.parse_args()

    before, reset, after, pending = reset_queue(args.database.resolve())
    print(f"database: {args.database.resolve()}")
    print(f"before: {before}")
    print(f"reset: {reset}")
    print(f"after: {after}")
    print(f"pending in scope: {pending}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Requeue failed captures; interrupted work is recovered by the controller."""

from __future__ import annotations

import argparse
from pathlib import Path
import sqlite3

from world_locations.database import connect, requeue_places


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATABASE = (
    ROOT / "converted" / "world-location-database" / "full-world" / "locations.sqlite3"
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

    connection = connect(database)
    try:
        before = queue_counts(connection)
        reset = requeue_places(connection)
        after = queue_counts(connection)
        pending = int(
            connection.execute(
                """SELECT COUNT(*) FROM places
                   WHERE scope_status='in_scope' AND queue_status='pending'"""
            ).fetchone()[0]
        )
        return before, reset, after, pending
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Reset eligible in-scope failed captures to pending. Refuses during "
            "an active session; the capture controller recovers interrupted work."
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

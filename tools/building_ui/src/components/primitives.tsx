import { useEffect, useId, useRef, useState, type ReactNode } from "react";
import { X } from "lucide-react";
export function Button({
  children,
  onClick,
  disabled = false,
  primary = false,
  danger = false,
  title,
  className = "",
}: {
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  primary?: boolean;
  danger?: boolean;
  title?: string;
  className?: string;
}) {
  return (
    <button
      type="button"
      title={title}
      disabled={disabled}
      onClick={onClick}
      className={`btn ${primary ? "btn-primary" : ""} ${danger ? "text-red-300" : ""} ${className}`}
    >
      {children}
    </button>
  );
}
export function Field({
  label,
  value,
  onCommit,
  type = "text",
  step,
  min,
  max,
  disabled = false,
}: {
  label: string;
  value: string | number;
  onCommit: (v: string) => unknown;
  type?: string;
  step?: number;
  min?: number;
  max?: number;
  disabled?: boolean;
}) {
  const [draft, setDraft] = useState(String(value));
  const cancelled = useRef(false);
  useEffect(() => setDraft(String(value)), [value]);
  return (
    <label className="field">
      <span>{label}</span>
      <input
        aria-label={label}
        value={draft}
        type={type}
        step={step}
        min={min}
        max={max}
        disabled={disabled}
        onChange={(e) => setDraft(e.target.value)}
        onBlur={async () => {
          if (cancelled.current) {
            cancelled.current = false;
            return;
          }
          if (draft !== String(value)) {
            if (
              type === "number" &&
              (draft.trim() === "" || !Number.isFinite(Number(draft)))
            ) {
              setDraft(String(value));
              return;
            }
            const result = await onCommit(draft);
            if (result === false) setDraft(String(value));
          }
        }}
        onKeyDown={(e) => {
          if (e.key === "Enter") e.currentTarget.blur();
          if (e.key === "Escape") {
            cancelled.current = true;
            setDraft(String(value));
            e.currentTarget.blur();
          }
        }}
      />
    </label>
  );
}
export function Select({
  label,
  value,
  onChange,
  options,
  disabled = false,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  options: { value: string; label: string }[];
  disabled?: boolean;
}) {
  return (
    <label className="field">
      <span>{label}</span>
      <select
        aria-label={label}
        value={value}
        disabled={disabled}
        onChange={(e) => onChange(e.target.value)}
      >
        {options.map((o) => (
          <option key={o.value} value={o.value}>
            {o.label}
          </option>
        ))}
      </select>
    </label>
  );
}
export function Toggle({
  label,
  checked,
  onChange,
}: {
  label: string;
  checked: boolean;
  onChange: (v: boolean) => void;
}) {
  return (
    <label className="flex cursor-pointer items-center gap-2 text-xs text-slate-300">
      <input
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
      />
      {label}
    </label>
  );
}
export function Section({
  title,
  children,
  action,
}: {
  title: string;
  children: ReactNode;
  action?: ReactNode;
}) {
  return (
    <section className="border-b border-line p-4">
      <div className="mb-3 flex items-center justify-between gap-2">
        <h2 className="eyebrow">{title}</h2>
        {action}
      </div>
      {children}
    </section>
  );
}
export function Modal({
  title,
  children,
  onClose,
  wide = false,
  locked = false,
}: {
  title: string;
  children: ReactNode;
  onClose: () => void;
  wide?: boolean;
  locked?: boolean;
}) {
  const ref = useRef<HTMLDialogElement>(null),
    id = useId();
  useEffect(() => {
    ref.current?.showModal();
    ref.current?.querySelector<HTMLElement>("[data-autofocus]")?.focus();
    return () => ref.current?.close();
  }, []);
  return (
    <dialog
      ref={ref}
      aria-labelledby={id}
      onCancel={(event) => {
        event.preventDefault();
        if (!locked) onClose();
      }}
      className={wide ? "modal modal-wide" : "modal"}
    >
      <div className="flex items-center justify-between border-b border-line p-5">
        <h2 id={id} className="text-xl font-semibold tracking-tight">
          {title}
        </h2>
        <button
          className="btn"
          aria-label="Close dialog"
          disabled={locked}
          onClick={onClose}
        >
          <X size={17} />
        </button>
      </div>
      <div className="modal-body">{children}</div>
    </dialog>
  );
}

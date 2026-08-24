import { FormEvent, type ReactNode, useState } from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";

const nav = [
  { to: "/characters", label: "Characters" },
  { to: "/locations", label: "Locations" },
  { to: "/events", label: "Events" },
  { to: "/peoples", label: "Peoples" },
  { to: "/timeline", label: "Timeline" },
];

export function Layout({ children }: { children: ReactNode }) {
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const navigate = useNavigate();

  function onSearch(event: FormEvent) {
    event.preventDefault();
    const q = query.trim();
    if (!q) return;
    navigate(`/search?q=${encodeURIComponent(q)}`);
    setOpen(false);
  }

  return (
    <div className="shell">
      <div className="vignette" aria-hidden="true" />
      <header className="site-header">
        <div className="header-inner">
          <Link to="/" className="brand" onClick={() => setOpen(false)}>
            <span className="ring" aria-hidden="true" />
            <span>
              <strong>The Chronicle</strong>
              <em>of Middle-earth</em>
            </span>
          </Link>
          <button
            className="menu-toggle"
            type="button"
            aria-expanded={open}
            aria-label="Toggle navigation"
            onClick={() => setOpen((v) => !v)}
          >
            <span />
            <span />
          </button>
          <nav className={open ? "open" : undefined}>
            {nav.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                onClick={() => setOpen(false)}
                className={({ isActive }) => (isActive ? "active" : undefined)}
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
          <form className="search" onSubmit={onSearch}>
            <input
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search the legendarium…"
              aria-label="Search"
            />
            <button type="submit">Seek</button>
          </form>
        </div>
      </header>
      <main>{children}</main>
      <footer className="site-footer">
        <p>
          Original encyclopedia prose inspired by J. R. R. Tolkien’s legendarium.
          This is an unofficial fan work, not affiliated with the Tolkien Estate
          or Middle-earth Enterprises.
        </p>
      </footer>
    </div>
  );
}

import { useMemo } from "react";
import { useSearchParams } from "react-router-dom";
import { searchEntries } from "../data/entries";
import { EntryCard } from "../components/EntryCard";

export function SearchPage() {
  const [params] = useSearchParams();
  const q = params.get("q") ?? "";
  const results = useMemo(() => searchEntries(q), [q]);

  return (
    <section className="section page">
      <div className="section-head">
        <p className="kicker">Seek and find</p>
        <h1>{q ? `Results for “${q}”` : "Search"}</h1>
        <p>
          {q
            ? `${results.length} ${results.length === 1 ? "entry" : "entries"} in the chronicle.`
            : "Use the field above to search names, places, and the War of the Ring."}
        </p>
      </div>
      {results.length > 0 ? (
        <div className="card-grid">
          {results.map((entry) => (
            <EntryCard key={entry.slug} entry={entry} />
          ))}
        </div>
      ) : (
        q && <p className="empty">Nothing by that name is written here — yet.</p>
      )}
    </section>
  );
}

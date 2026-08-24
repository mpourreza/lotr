import { Link } from "react-router-dom";
import type { Entry } from "../data/entries";

export function EntryCard({ entry }: { entry: Entry }) {
  return (
    <Link to={`/${entry.category}/${entry.slug}`} className="card">
      <p className="kicker">{entry.category}</p>
      <h3>{entry.name}</h3>
      <p className="epithet">{entry.epithet}</p>
      <p>{entry.summary}</p>
    </Link>
  );
}

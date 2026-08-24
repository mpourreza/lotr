import { Link, Navigate, useParams } from "react-router-dom";
import { categories, getEntry, relatedEntries, type Category } from "../data/entries";
import { EntryCard } from "../components/EntryCard";

export function EntryPage() {
  const { category, slug } = useParams();
  const entry = slug ? getEntry(slug) : undefined;
  if (!entry) return <Navigate to="/" replace />;
  if (category && entry.category !== category) {
    return <Navigate to={`/${entry.category}/${entry.slug}`} replace />;
  }
  const related = relatedEntries(entry);
  const cat = categories.find((c) => c.id === entry.category as Category);

  return (
    <article className="entry page">
      <p className="kicker">
        <Link to={`/${entry.category}`}>{cat?.title}</Link>
        <span> · {entry.era}</span>
      </p>
      <h1>{entry.name}</h1>
      <p className="epithet">{entry.epithet}</p>
      <p className="lede">{entry.summary}</p>
      <div className="tags">
        {entry.tags.map((tag) => (
          <span key={tag}>{tag}</span>
        ))}
      </div>
      {entry.body.map((para) => (
        <p key={para.slice(0, 24)}>{para}</p>
      ))}
      {related.length > 0 && (
        <section className="related">
          <h2>Roads that meet this one</h2>
          <div className="card-grid">
            {related.map((item) => (
              <EntryCard key={item.slug} entry={item} />
            ))}
          </div>
        </section>
      )}
    </article>
  );
}

import { Navigate, useParams } from "react-router-dom";
import { categories, getByCategory, type Category } from "../data/entries";
import { EntryCard } from "../components/EntryCard";

const ids = new Set(categories.map((c) => c.id));

export function CategoryPage() {
  const { category } = useParams();
  if (!category || !ids.has(category as Category)) {
    return <Navigate to="/" replace />;
  }
  const meta = categories.find((c) => c.id === category)!;
  const list = getByCategory(category as Category);

  return (
    <section className="section page">
      <div className="section-head">
        <p className="kicker">Index</p>
        <h1>{meta.title}</h1>
        <p>{meta.blurb}</p>
      </div>
      <div className="card-grid">
        {list.map((entry) => (
          <EntryCard key={entry.slug} entry={entry} />
        ))}
      </div>
    </section>
  );
}

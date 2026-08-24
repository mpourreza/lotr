import { Link } from "react-router-dom";
import { categories, entries, timeline } from "../data/entries";
import { EntryCard } from "../components/EntryCard";

const featured = [
  "frodo-baggins",
  "aragorn",
  "galadriel",
  "mordor",
  "minas-tirith",
  "destruction-of-the-ring",
]
  .map((slug) => entries.find((e) => e.slug === slug))
  .filter((e): e is NonNullable<typeof e> => Boolean(e));

export function HomePage() {
  return (
    <>
      <section className="hero">
        <p className="kicker">A fan chronicle of the Third Age</p>
        <h1>One Ring to remember them all</h1>
        <p className="lede">
          Wander an original encyclopedia of the characters, realms, kindreds,
          and turning points of Middle-earth — written for this site, not copied
          from the books.
        </p>
        <div className="hero-actions">
          <Link className="btn" to="/characters">
            Meet the company
          </Link>
          <Link className="btn ghost" to="/timeline">
            Walk the timeline
          </Link>
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>The four books of this chronicle</h2>
          <p>Start anywhere. Every entry links onward, as roads in Eriador do.</p>
        </div>
        <div className="category-grid">
          {categories.map((cat) => (
            <Link key={cat.id} to={`/${cat.id}`} className="category-tile">
              <h3>{cat.title}</h3>
              <p>{cat.blurb}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>Illuminated entries</h2>
          <p>A handful of names the War of the Ring will not let you forget.</p>
        </div>
        <div className="card-grid">
          {featured.map((entry) => (
            <EntryCard key={entry.slug} entry={entry} />
          ))}
        </div>
      </section>

      <section className="section">
        <div className="section-head">
          <h2>From the forging to the Havens</h2>
          <Link to="/timeline">Full timeline →</Link>
        </div>
        <ol className="home-timeline">
          {timeline.slice(0, 5).map((item) => (
            <li key={item.year}>
              <span>{item.year}</span>
              <Link to={`/${entries.find((e) => e.slug === item.slug)?.category}/${item.slug}`}>
                {item.title}
              </Link>
            </li>
          ))}
        </ol>
      </section>
    </>
  );
}

import { Link } from "react-router-dom";
import { entries, timeline } from "../data/entries";

export function TimelinePage() {
  return (
    <section className="section page">
      <div className="section-head">
        <p className="kicker">The long count</p>
        <h1>Timeline of the Ring</h1>
        <p>
          A path from the forging in Orodruin to the white ship at Mithlond,
          with the War of the Ring drawn in heavier ink.
        </p>
      </div>
      <ol className="timeline">
        {timeline.map((item) => {
          const entry = entries.find((e) => e.slug === item.slug);
          return (
            <li key={item.year}>
              <time>{item.year}</time>
              <div>
                <h2>
                  {entry ? (
                    <Link to={`/${entry.category}/${entry.slug}`}>{item.title}</Link>
                  ) : (
                    item.title
                  )}
                </h2>
                <p>{item.text}</p>
              </div>
            </li>
          );
        })}
      </ol>
    </section>
  );
}

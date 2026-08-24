---
title: Tags
layout: archive
permalink: /tags/
author_profile: false
entries_layout: list
classes: wide
excerpt: "Entries grouped by tag across characters, locations, events, and people."
---

{% assign all_docs = site.characters | concat: site.locations | concat: site.events | concat: site.kindreds %}
{% assign tag_names = "" | split: "" %}
{% for doc in all_docs %}
  {% for tag in doc.tags %}
    {% assign tag_names = tag_names | push: tag %}
  {% endfor %}
{% endfor %}
{% assign tag_names = tag_names | uniq | sort %}

<ul class="taxonomy__index">
  {% for tag_name in tag_names %}
    {% assign tag_count = 0 %}
    {% for doc in all_docs %}
      {% if doc.tags contains tag_name %}
        {% assign tag_count = tag_count | plus: 1 %}
      {% endif %}
    {% endfor %}
    <li>
      <a href="#{{ tag_name | slugify }}">
        <strong>{{ tag_name }}</strong> <span class="taxonomy__count">{{ tag_count }}</span>
      </a>
    </li>
  {% endfor %}
</ul>

{% for tag_name in tag_names %}
  <section id="{{ tag_name | slugify }}" class="taxonomy__section">
    <h2 class="archive__subtitle">{{ tag_name }}</h2>
    <div class="entries-{{ page.entries_layout | default: 'list' }}">
      {% for post in all_docs %}
        {% if post.tags contains tag_name %}
          {% include archive-single.html type=page.entries_layout %}
        {% endif %}
      {% endfor %}
    </div>
    <a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: "Back to the Top" }}</a>
  </section>
{% endfor %}

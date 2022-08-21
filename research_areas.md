---
layout: page
title: "Research"
---
{% for slide in site.research %}
<div class="row checker" style="margin:auto;justify-content:center;width:100%;max-width:1000px">
  <h2><a href="{{ slide.url | relative_url}}">{{slide.title}}</a></h2>
  <img src="{{slide.splash | relative_url}}" alt="{{slide.title}}">
  <p>{{slide.summary}}</p>
  <h3>Highlighted Work</h3>
  {% for pro in slide.projects %}
  {% assign rem = forloop.index | modulo: 2 %}
    {% if rem == 1 %}
      <div class="row" style="background-color:#c1cef5;padding-bottom:20px">
    {% else %}
      <div class="row" style="padding-bottom:20px">
    {% endif %}
      <h5>{{pro.name}}</h5>
      {% if pro.image %}
      <div class="col" style="margin:0 auto;min-width:300px;max-width:400px">
        <img src="{{pro.image | relative_url}}" alt="{{pro.name}}">
      </div>
      {% endif %}
      <div class="col" style="width:100%;min-width:350px">
        {{pro.blurb}}
      </div>
    </div>
  {% endfor %}
</div>
{% endfor %}

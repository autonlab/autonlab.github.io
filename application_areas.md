---
layout: page
title: "Application Areas"
---

At the Auton Lab, we believe that the most useful concepts in AI and ML reveal themselves through frequent exposure to domain-specific challenges and constraints.
It is these limitations that motivate us to engage creatively and think about how to address the hurdles that stand in the way of widespread, beneficial adoption of AI technology.
Our goal is to assuage these pain points to best meet the needs of potential users of AI, whether they be subject matter experts, developers of AI systems, or general users.
To get a flavor for the type of work happening at the lab, here is a selection of five broad application areas where we are applying and proving our research.

{% for slide in site.applications %}
<div class="row checker" style="margin:auto;justify-content:center;width:100%;max-width:1000px">
  <h2>{{slide.title}}</h2>
  <img src="{{slide.splash | relative_url}}" alt="{{slide.title}}">
  <p><br/>{{slide.summary}}</p>
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
      <div class="row" style="margin:0 auto;width:100;max-width:400px">
        <img src="{{pro.image | relative_url}}" alt="{{pro.name}}">
      </div>
      {% endif %}
      <div class="col" style="width:100%">
        {{pro.blurb}}
      </div>
    </div>
  {% endfor %}
</div>
<div>
&nbsp;
</div>
{% endfor %}

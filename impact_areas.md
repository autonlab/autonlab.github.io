---
layout: page
title: "Impact"
---
Beyond publications, our lab's contributions have real-world impact.
Most direct impact comes from application of technologies developed in the lab.
Other impacts result from the educational mission of the lab and partnerships with industry.
<div class="impact-page-styles">
  <div class="row" style="margin:auto;justify-content:center;width:100%;max-width:1000px;border:4px solid #323399;border-radius:25px">
    {% for slide in site.impact %}
    {% assign rem = forloop.index | modulo: 2 %}
    {% if rem == 1 %}
    <div class="row" style="margin:auto;justify-content:center;width:100%;max-width:1000px;background-color:#cdd7ef;padding-bottom:30px;border-radius:20px">
    {% else %}
    <div class="row impact-row" style="margin:auto;justify-content:center;width:100%;max-width:1000px;padding-bottom:30px;">
    {% endif %}
    <h4><a href="{{ slide.url | relative_url}}">{{slide.title}}</a></h4>
      <div class="row" style="margin:0 auto;width:100%;max-width:400px">
        <img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
      </div>
      <div class="col" style="width:100%">
      <p>{{slide.summary}}</p>
      </div>
    </div>
  {% endfor %}
  </div>
</div>


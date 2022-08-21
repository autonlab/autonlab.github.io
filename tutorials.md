---
layout: page
title: "Machine Learning Tutorials"
---

{% for tut in site.tutorials %}
{% assign rem = forloop.index | modulo: 2 %}
{% if rem == 1 %}
<div class="container" style="background-color:#c1cef5;border:2px solid blue;border-radius:5px;">
{% else %}
<div class="container" style="border:2px solid blue;border-radius:5px;">
{% endif %}
<div class="row">
<div class="col"><a href="{{tut.pdf | relative_url }}"><h4>{{tut.title}}</h4></a></div>
</div>
<div class="row">{{tut.content}}</div>
</div>
{%endfor%}

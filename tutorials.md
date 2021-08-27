---
layout: page
title: "Machine Learning Tutorials"
---

{% for tut in site.tutorials %}
<div class="container" style="border:2px solid blue;border-radius:5px;">
<div class="row">
<div class="col"><a href="{{tut.url | relative_url }}">{{tut.title}}</a></div>
<div class="col"><div class="float-end"><a style="background-color:blue;color:white;padding:2px 5px 2px 5px;margin:2px 5px 2px 5px;border:1px solid black;border-radius:5px;" href="{{tut.pdf | relative_url}}">PDF</a></div></div>
</div>
<div class="row">{{tut.content}}</div>
</div>
{%endfor%}

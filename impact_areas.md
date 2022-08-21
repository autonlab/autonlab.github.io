---
layout: page
title: "Impact"
---
Beyond publications, our lab's contributions have real-world impact.


{% for slide in site.impact %}
{% assign rem = forloop.index | modulo: 2 %}
{% if rem == 1 %}
<div class="row checker" style="margin:auto;justify-content:center;width:100%;max-width:1000px;background-color:#c1cef5;padding-bottom:20px">
{% else %}
<div class="row checker" style="margin:auto;justify-content:center;width:100%;max-width:1000px;padding-bottom:20px">
{% endif %}
	<h3><a href="{{ slide.url | relative_url}}">{{slide.title}}</a></h3>
   	<img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
	<p>{{slide.summary}}</p>
</div>
<div>
&nbsp;
</div>
{% endfor %}



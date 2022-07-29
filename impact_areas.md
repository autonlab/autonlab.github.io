---
layout: page
title: "Impact"
---
Beyond publications, our lab's contributions have real-world impact.


{% for slide in site.impact %}
{% assign rem = forloop.index | modulo: 2 %}
<h1><a href="{{ slide.url | relative_url}}">{{slide.title}}</a></h1>
<div class="row" style="width:95%">
	{% if rem == 0 %}
	<div class="col">
   	<img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
   	</div>
	{%endif%}
  	<div class="col align-self-center">
		<p>{{slide.summary}}</p>
    </div>
    {% if rem == 1 %}
	<div class="col">
    <img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
    </div>
    {%endif%}
</div>


{% endfor %}



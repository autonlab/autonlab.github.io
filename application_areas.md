---
layout: page
title: "Application Areas"
---
The Auton Lab works on theory, algorithms, and applications.
The lab is unique in that identified needs in real-world application domains are backpropagated to inform design choices in theory and algorithms.
There are four broad application areas that motivate much of our research at the lab, and many of our projects fit into one or more of these groups.

{% for slide in site.applications %}
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
		<h4>Projects</h4>
		<ul>
		{% for pro in slide.projects %}
			<li><a href="{{slide.url | relative_url}}#{{pro.anchor}}"><h5>{{pro.name}}</h5></a> - {{pro.blurb}}</li>
		{% endfor %}
		</ul>
    </div>
    {% if rem == 1 %}
	<div class="col">
    <img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
    </div>
    {%endif%}
</div>


{% endfor %}



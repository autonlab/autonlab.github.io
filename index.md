---
layout: home
title: "Auton Lab"
tagline: "Developing Artificial Intelligence for practical solutions to real world problems"
hero: "/assets/images/showcase.jpg"
permalink: /
---


<div class="home">
  <div class="hero container-fluid text-center">
  {%- if page.title -%}
    <h1>{{ page.title }}</h1>    
  {%- endif -%}
  {%- if page.tagline -%}
    <h3>{{ page.tagline }}</h3>
  {%- endif -%}
<div id="researchCarousel" class="carousel slide" data-bs-ride="carousel">

  <div class="carousel-inner">
    {% for slide in site.applications %}
    {% assign rem = forloop.index | modulo: 2 %}
    <div class="carousel-item{% if forloop.first %} active{% endif %}">
    	<div class="row">
    		{% if rem == 0 %}
			<div class="col">
        		<img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
        	</div>
        	{%endif%}
        	<div class="col align-self-center slide-div">
      			<h3><a href="{{slide.url | relative_url}}">{{slide.title}}</a></h3>
      			<br/>
      			<p>{{slide.summary}}</p>
      		</div>
      		{% if rem == 1 %}
			<div class="col">
        		<img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
        	</div>
        	{%endif%}
      	</div>
    </div>
    {% endfor %}
  </div>

</div>
  </div>
<br/>

<h3>Latest News</h3>


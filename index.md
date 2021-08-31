---
layout: home
title: "The Auton Lab"
tagline: "Developing Artificial Intelligence for practical solutions to real world problems"
hero: "/assets/images/showcase.jpg"
permalink: /
---

---
layout: home
title: "The Auton Lab"
tagline: "Developing Artificial Intelligence for practical solutions to real world problems"
hero: "/assets/images/showcase.jpg"
permalink: /
---

<div class="home">
  <div class="hero container-fluid text-center">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>    
  {%- endif -%}
  {%- if page.tagline -%}
    {{ page.tagline }}
  {%- endif -%}
<div id="researchCarousel" class="carousel slide" data-bs-ride="carousel">

  <div class="carousel-inner">
    {% for slide in site.research %}
    {% assign rem = forloop.index | modulo: 2 %}
    <div class="carousel-item{% if forloop.first %} active{% endif %}">
    	<div class="row">
    		{% if rem == 0 %}
			<div class="col">
        		<img src="{{slide.splash | relative_url}}" class="d-block w-100" alt="{{slide.title}}">
        	</div>
        	{%endif%}
        	<div class="col align-self-center slide-div">
      			<h4><a href="{{slide.url | relative_url}}">{{slide.title}}</a></h4>
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

<h1>Latest News</h1>


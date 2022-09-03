---
layout: home
carousel: "Areas where we are making an impact"
permalink: /
---


<div class="home">
 <div class="hero container-fluid text-center">
   <img id="autonLogo" src="{{'/assets/images/auton_logo.png' | relative_url}}" style="text-align: center;max-width:400px;width:100%;" alt="Auton Lab">
    <!-- unnecessary with no page title
    <br /> 
    <br /> 
    <br /> 
    {%- if page.title -%}
      <h1>{{ page.title }}</h1>    
    {%- endif -%}
    -->
    <h4>Intelligent systems that work, are useful, and make economic sense.</h4>
    <div class="row" style="margin:auto;max-width:1000px">
    <p>We are an academic lab that studies theory, algorithms, and applications of Artificial Intelligence, Machine Learning, and Robotics. We are part of the School of Computer Science at Carnegie Mellon University. By constantly exposing our work to application domain specific constraints and challenges that occur in the real world, we identify gaps in the science of AI and our fundamental research focuses on developing new methods to improve the application of AI in practice.</p>
    </div>
	<br/>
    <h1>{{ page.carousel }}:</h1>
	<br/>
    <div id="researchCarousel" class="carousel slide text-center" data-bs-ride="carousel">
      <div class="carousel-inner" >
        {% for slide in site.carousel %}
          <div class="carousel-item{% if forloop.first %} active{% endif %}" >
			<div class="row align-self-center slide-div" style="margin:auto;height:100%">
        	  <img src="{{slide.splash | relative_url}}" style="margin:auto;object-fit:contain;width:100%;height:100%;max-width:1000px" alt="{{slide.title}}">
        	</div>
        	<div class="row align-self-center slide-div" style="margin:auto;height:100%;max-width:1000px" >
      		  <h1><a href="{{slide.url | relative_url}}">{{slide.title}}</a></h1>
      		  <br/>
      		  <p>{{slide.summary}}</p>
      		</div>
  		  </div>
        {% endfor %}
      </div>
    </div>
  </div>

<br/>
<h1>Latest News</h1>

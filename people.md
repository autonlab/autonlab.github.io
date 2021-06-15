---
layout: page
title: "People"
permalink: /people
---
# Founders
{% assign sortedStaff = site.staff | where:'category','founder' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url }}">{{member.first_name}} {{member.last_name}}</a></h4>
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

# Staff
{% assign sortedStaff = site.staff | where:'category','staff' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url }}">{{member.first_name}} {{member.last_name}}</a></h4>
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

# Graduate Students

{% assign sortedStaff = site.staff | where:'category','student' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url }}">{{member.first_name}} {{member.last_name}}</a></h4>
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>
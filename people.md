---
layout: page
title: "People"
---
<div class="people-title">
Faculty
</div>

<div class="staff-container">
{% assign sortedStaff = site.staff | where:'category','founder' | sort: 'last_name' %}
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	<h4>{{member.first_name}} {{member.last_name}}</h4>
	{% endif %}
	<p>{{member.title}}</p>
</div>
{% endfor %}
{% assign sortedStaff = site.staff | where:'category','faculty' | sort: 'last_name' %}
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	<h4>{{member.first_name}} {{member.last_name}}</h4>
	{% endif %}
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

<div class="people-title">
Students
</div>

{% assign sortedStaff = site.staff | where:'category','student' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	<h4>{{member.first_name}} {{member.last_name}}</h4>
	{% endif %}
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

<div class="people-title">
Staff
</div>

{% assign sortedStaff = site.staff | where:'category','staff' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	<h4>{{member.first_name}} {{member.last_name}}</h4>
	{% endif %}
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

<div class="people-title">
Alumni
</div>

{% assign sortedStaff = site.staff | where:'category','alumni' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	<h4>{{member.first_name}} {{member.last_name}}</h4>
	{% endif %}
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

---
layout: page
title: "People"
permalink: /people
---
# Faculty
{% assign sortedStaff = site.staff | where:'category','faculty' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

# Alumni
{% assign sortedStaff = site.staff | where:'category','alumni' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>

# Researchers
{% assign sortedStaff = site.staff | where:'category','staff' | sort: 'last_name' %}
<div class="staff-container">
{% for member in sortedStaff %}
<div class="staff-block" data-bs-toggle="tooltip" data-bs-placement="top" title="{{member.summary}}">
	{% if member.image %}
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url |relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
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
	<img class="bio-img" src="{{member.image | relative_url}}" alt="{{member.first_name}} {{member.last_name}}">
	{% else %}
	<div class="bio-img">
	No Image
	</div>
	{% endif %}
	<h4><a href="{{ member.url | relative_url}}">{{member.first_name}} {{member.last_name}}</a></h4>
	<p>{{member.title}}</p>
</div>
{% endfor %}
</div>
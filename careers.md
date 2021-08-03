---
layout: page
title: "Careers"
permalink: /careers
---

The Auton Lab is always looking for qualified, driven individuals to join our team and push the envelope in Machine Learning and robotics technology. If you have a desire to learn and hone your skills in these areas, take a look at our available opportunities!

{% assign filtered = site.careers | where:'status','open' %}

{% for job in filtered %}
<div data-bs-toggle="tooltip" data-bs-placement="top" class="career-div" title="{{job.summary}}">

	<h4>{{job.title}}<a class="btn btn-info" href="{{ job.apply }}">APPLY</a></h4>
	<p>{{job.content}}</p>
</div>
{% endfor %}


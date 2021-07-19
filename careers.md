---
layout: page
title: "Careers"
permalink: /careers
---

{% assign filtered = site.careers | where:'status','open' %}

{% for job in filtered %}
<div data-bs-toggle="tooltip" data-bs-placement="top" title="{{job.summary}}">

	<h4>{{job.title}}<a href="{{ job.apply }}">[APPLY]</a></h4>
	<p>{{job.content}}</p>
</div>
{% endfor %}


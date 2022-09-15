---
layout: page
title: "Careers"

---

#### [Let's chat](https://docs.google.com/forms/d/e/1FAIpQLSd6pPZXIZII8bBnBgoQoU3l0OOsc4wxVc9zDBRfQPOSklk9Dg/viewform?usp=sf_link) about Auton Lab! 

The Auton Lab is always looking for highly motivated individuals to join our team and push the envelope in Machine Learning and robotics technology.
We are hiring across all roles, including: post-docs, programmers, data analysts, researchers, UX designers, engineers, interns.

**Already know the specific position to which you want to formally apply?**
Check out the descriptions and links below to submit your job application through Carnegie Mellon's HR department.

{% assign filtered = site.careers | where:'status','open' %}

{% for job in filtered %}
<div data-bs-toggle="tooltip" data-bs-placement="top" class="career-div" title="{{job.summary}}">

	<h4>{{job.title}}<a class="btn btn-info career-button" href="{{ job.apply }}">APPLY</a></h4>
	<p>{{job.content}}</p>
</div>
{% endfor %}


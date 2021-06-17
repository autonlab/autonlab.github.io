# Auton Lab Website

If you are reading this, you are likely attempting to update or maintain the Auton Lab website in some fashion.  Read on for some quick howtos.

## Updating the News Feed

## adding and editing career entries

## Adding to staff

If you wish to add a staff member profile, it's very easy. Simply create a file in the directory /collections/_staff/

This file should have the format of lastname_firstname.md in all lowercase.

The contents of the file must follow the format below, and category must be one of *staff*,*founder*, or *student*:

---  
layout: homepage  
first_name: Jane  
last_name: Doe  
title: Peon  
category: staff  
image: "/assets/staff/lastname_firstname.png" (can be left out if no image available. Place the image in the directory as shown)  
summary: "This is what shows up on mouseover of the staff member's entry."  
---  
Anything below the three dashes here is shown when the name is clicked. This can be used to make a simple(or complex!) homepage, using HTML or jekyll markdown.  


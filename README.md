# Auton Lab Website

If you are reading this, you are likely attempting to update or maintain the Auton Lab website in some fashion.  Read on for some quick howtos.

## Updating the News Feed

The news feeds are located under the *collections* directory, under the *_posts* subdirectory. Each file *MUST* be titled in the format YYYY-MM-DD-XXXX.md, with XXXX a word or two description of the post. The actual post follows the format:

```
---
layout: post
title:  "Title here"
date:   YYYY-MM-DD HH:MM:SS -0400
categories: site news
excerpt: "Insert what appears on the front page here."
---

Place the text of the full news article here, if different from the excerpt. This can be forematted like an individual page with images and so on, using the markup language.
```

Currently, only the "site news" category is used.

## Adding and Editing career entries

## Adding to staff

If you wish to add a staff member profile, it's very easy. Simply create a file in the directory /collections/_staff/

This file should have the format of lastname_firstname.md in all lowercase.

The contents of the file must follow the format below, and category must be one of *staff*,*founder*, or *student*:

```
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
```

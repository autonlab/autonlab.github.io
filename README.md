# Auton Lab Website

If you are reading this, you are likely attempting to update or maintain the Auton Lab website in some fashion.  Read on for some quick howtos.

## I want to tweak text on an existing page

If you want to make straightforward changes to text (e.g. spelling error or new sentence in paragraph), you can make them directly on Github.
Find the file you want to change and use the edit button (pencil).
Changes to text are likely safe to commit directly to the master branch.

Note that if you are making larger changes to the text, like adding new elements to a list, you will need to pay attention to markdown syntax.
In these cases, it would be safer to create a new branch for your commit and start a pull request.

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

The contents of the file must follow the format below, and category must be one of *staff*,*faculty*, *alumni* or *student*:

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

## Adding a new collection and linking to home page header

If you wish to add a new tab on the top of the home screen that links to a new collection, there are a few things you need to do.

1) create a new directory under collections/ that begins with an underscore (e.g. /_newCollection/)
2) Add new elements to this directory that form the colleciton. As a template, you may copy elements from another collection, e.g. /_research/, and change text as needed
3) create a new markdown file newCollection.md in the same directory as this README (If you want it to look like other collections on the site, copy an existing collection, e.g. application_areas.md).  The markdown file name and your collection directory name do not need to match
4) update _config.yml with these changes. Add newCollection.md to the list of header_pages in the order that you want it to appear alongside other headers.  Also add the new collection directory with an output: true flag (like other collections)

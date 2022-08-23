# Auton Lab Website

If you are reading this, you are likely attempting to update or maintain the Auton Lab website in some fashion.  Read on for some quick howtos.

[FAQ](https://docs.google.com/document/d/1cBfbX9edwId-wbtjpLK3FxDHYtadFnEY5ne2Q2JsXCw/edit?usp=sharing)

# How to view edits locally
[Github Documentation](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

The directions on this page are good.
The added note about adding webrick to the gemfile depending on the version of Jekyll that you are using came in handy.
The general path to getting the website up and running on your local machine is:
  - Install Ruby
  - Install Bundler
  - Install Jekyll
  - $ bundle install
  - $ bundle exec jekyll serve
  - Navigate to http://localhost:4000/ on your local machine

### Features of the website
  - Welcome page with big ideas in AI/ML to introduce how we view the field and how we think
  - Our work is indexable by application area, fundamental research thrust, and real-world impact
  - News feed on the home page
  - Searchable publication table
  - Resources, including ML tutorials, lectures, data, code repos, and demos
  - Informal (google form) and formal (CMU HR) job postings
  - List of Autonians, past and present

### Key points
  - Keep it broad - most people do not go to a website for specifics of individual projects
  - No mentions of individual projects - these get dated quickly!
  - You can make your own markdown homepage on the site if you do not already have a personal homepage
  - Small changes to text can be done directly on github, larger edits can be done by creating a branch and testing locally

### Directory Structure (key elements shown)
/autonlab.github.io/
  - assets/images/ <- all images on the website go here
  - collections/ <- lists of things are collated here
    - \_staff/ (All last\_first.md pages for Autonians)
    - \_posts/ (All posts in Latest News on the homepage)
    - \_impact/ (All pages describing the impact of our work)
    - \_research/ (All pages describing the research thrusts and highlighted works)
    - \_applications/ (All pages describing application domains in the lab portfolio)
  - publications/ (bibtex files to be included in the table)
  - static/page.css (element-specific formatting)
  - \_layouts/ (page-specific formatting)
  - \_config.yml <- sets navbar elements and page structure
    - application\_areas.md
    - careers.md
    - impact\_areas.md
    - people.md
    - publications.md
    - research\_areas.md
    - resources.md
    - welcome.md
  - Gemfile (you must add this yourself one time only, make sure it is here /autonlab.github.io/Gemfile if you want to be able to view local changes before committing them)

# FAW How-To:

## Edit your personal page / Add a new employee
If you wish to add a staff member profile, it's very easy. Simply create a file in the directory autonlab.github.io/collections/\_staff/
This file should have the format of lastname\_firstname.md in all lowercase.
The contents of the file must follow the format below, and category must be one of *staff*,*faculty*, *alumni* or *student*:
```
---
layout: homepage
first_name: [First]
last_name: [Last]
title: [e.g. PhD Student]
category: {student, staff, alumni, faculty} (selection tell the site where to sort your entry)
image: "/assets/images/[last]_[first].jpg" (can be left out if no image available,. Place the image in the directory as shown)
summary: "mouseover text"
---  
[Anything below the three dashes here is shown when the name is clicked. This can be used to make a simple(or complex!) homepage, using HTML or jekyll markdown.]
```
  - category: tells the site where to sort and insert your entry
  - image: this line is optional and can be left out if no image is available.  Place your image in the directory as shown in the example above, and please name your image *[last name]\_[first name].jpg*
  - summary: this text shows up on mouseover of the staff member's entry

## Add new publications to the searchable table
The website can handle bibtex entries.
Add your bibtex citations to any file in autonlab.github.io/publications/ .We recommend creating a new file for all of your past and future publications named [last]\_[first].bib.

## I want to tweak text on an existing page

If you want to make straightforward changes to text (e.g. spelling error or new sentence in paragraph), you can make them directly on Github, *you must be logged in to Github*.
Find the file you want to change and use the edit button (pencil).
Changes to text are likely safe to commit directly to the master branch.

Note that if you are making larger changes to the text, like adding new elements to a list, you will need to pay attention to markdown syntax.
In these cases, it would be safer to create a new branch for your commit and start a pull request.

Entries in the white/blue checker cells tend to be files in the autonlab.github.io/collections/\* directories.


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

## Adding a new collection and linking to home page header

If you wish to add a new tab on the top of the home screen that links to a new collection, there are a few things you need to do.

  - create a new directory under collections/ that begins with an underscore (e.g. /\_newCollection/)
  - Add new elements to this directory that form the colleciton. As a template, you may copy elements from another collection, e.g. /\_research/, and change text as needed
  - create a new markdown file newCollection.md in the same directory as this README (If you want it to look like other collections on the site, copy an existing collection, e.g. application\_areas.md).  The markdown file name and your collection directory name do not need to match
  - update \_config.yml with these changes. Add newCollection.md to the list of header\_pages in the order that you want it to appear alongside other headers.  Also add the new collection directory with an output: true flag (like other collections)

## How to change formatting of an element on a particular page

Check out static/page.css

It is highly recommended that you render the site locally to see the effect of your changes before pushing to the live site.

## How to change formatting of an entire page

Check out \_layouts/\* which contain the templates that are called by all other files on the site (e.g., layout: research)

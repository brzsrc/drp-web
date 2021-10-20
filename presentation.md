%title: A flash introduction to Flask
%author: Ivan Procaccini (ip914@ic.ac.uk)
%date: 2020-03-16

-> Flask <-
=========

-> A web microframework. <-

"Micro" because it comes with a simple, *but highly extensible* core.
This means, among other things, a *gentle learning curve* for a beginner.

-------------------------------------------------
-> # Topics for today (feat. a Todo App) <-

1. One-file app
2. Fundamentals of the *Jinja2 templating language*
3. Basic *GET and POST methods* and *form data*
4. *Blueprints* for better organisation of endpoint
5. Data persistance with *Flask-SQLAlchemy*


-------------------------------------------------
-> # Materials <-

-> All the code is already available on [GitLab](https://gitlab.doc.ic.ac.uk/ip914/drp-flask), including this presentation. <-

-------------------------------------------------

-> # How "simple" is simple? <-

Let's say 
-> *"all-in-one-short-file-if-you-wanted-to"* <-
simple.

-------------------------------------------------
-> # What we did do <-

-> Created a Todo app from scratch, with database and all <-

-------------------------------------------------
-> # What we didn't do <-

-> TESTING!!! <-

-------------------------------------------------

-> # Resources <-

[Flask](https://flask.palletsprojects.com/en/1.1.x/)
[Flask-Login](https://flask-login.readthedocs.io/en/latest/)
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
[Flask-RestX](https://flask-restx.readthedocs.io/en/latest/)
...and the code of all the apps in the [edtech](https://gitlab.doc.ic.ac.uk/edtech) GitLab group.

-------------------------------------------------
-> # This presentation is cool <-

It's just markdown.
The magic is done by [mdp](https://github.com/visit1985/mdp).

To turn it into a PDF, install:
\- *markdown* to convert to HTML
\- *wkhtmltopdf* to convert from HTML to PDF

After installing them, you can simply run:

    $ markdown presentation.md | wkhtmltopdf - presentation.pdf

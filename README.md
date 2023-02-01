# [Django](https://en.wikipedia.org/wiki/Django_(web_framework))

Official Site: [www.djangoproject.com](https://www.djangoproject.com)

Learning from: [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) (~10hr)

1. [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer)
   1. How to get Django installed. (`pip install Django`)
   2. How to create a new project. (`django-admin startproject project_name`)
   3. Looked at the structure of what gets created.
   4. How to pull up that default site in the browser. (`python manage.py runserver`)

2. [Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes](https://www.youtube.com/watch?v=a48xeeo5Vnk&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2&ab_channel=CoreySchafer)
   1. Adding a Blog application to our Django site. (`python manage.py startapp app_name`)
   2. Setting up some URL routes, so that we can start directing people to pages that we'd like them to see.

3. [Python Django Tutorial: Full-Featured Web App Part 3 - Templates](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer)
   1. How to use templates to return more complex HTML code than we did in the last video.
   2. Note: Don't forget to add a new app to the list of installed apps. ([3:25](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=206))
   3. How to pass data to our HTML templates.
   4. Writing code in HTML. (`{% code %}`, `{{ variable }}`)
   5. Template Inheritance.
   6. Add [Bootstrap](https://getbootstrap.com). (**Imp**: [Docs](https://getbootstrap.com/docs), [Examples](https://getbootstrap.com/examples), [Icons](https://icons.getbootstrap.com))
   7. Note: Corey added a lot of HTML and CSS for custom structuring and styling, but didn't walk through those
      snippets, as this is backend course, not frontend (or fullstack), so I did not copy-pasted those snippets, but
      pulled up minimal snippets from Bootstrap, so now I know what the markup mean + a nice minimal look to the website
      is not bad for someone who's starting out!
   8. Don't hardcode the URLs in the HTML, use `url` tag instead.

# spectre (django-simple-blog)

A simple blogging engine written using the Django web development framework. It allows you to post blogs and comments. It also has a page hit counter and handles user accessibility. It handles the ability and authorization of users, posts, and comments. It also provides access to superadmin that allows editing user, groups, and posts. It supports fast integrating into your current project with a blog-system. Easy to setup and use.

This web application creates an very basic blog site using Django. The site allows blog authors to create text-only blogs using the Admin site, and any logged in user to add comments via a form. Any user can list all bloggers, all blogs, and detail for bloggers and blogs (including comments for each blog).


Installation
------------

Execute the following commands to install spectre

To install python and create a virtual environment:

    $ sudo apt-get install python-pip
    $ pip install django==1.10
    $ pip install virtualenv
    $ python -m virtualenv venv-spectre
    $ source venv-spectre/bin/activate

Now, clone the repository and change the working directory to app. To install django:

    $ pip install django==1.10

You can check if django is correctly installed or not using:

    $ django-admin --version

Now, you need to run migrations to create the database schema for blogs:

    $ python manage.py makemigrations review
    $ python manage.py migrate

You can now start the django server:

    $ python manage.py runserver

Or you can add it in your own application

1. Add ``review`` to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = (
           ...
           'review',
       )


    Note: if you want to customize the templates, please add ``el_pagination`` ``markdown_deux`` ``pagedown`` to your INSTALLED_APPS setting.

        INSTALLED_APPS = (
            ...
            'el_pagination',
            'markdown_deux',
            'pagedown',
            'review',
        )

2. Run ``python manage.py migrate``
3. Include the ``review urls`` like this to have your "home page" as the blog index::

        urlpatterns = [
          ...
          url(r'^spectre/', include('review.urls')),
          url(r'^admin/', include(admin.site.urls)),
        ]

Usage
-----

You can visit the django website at http://localhost:8000. It is also possible to access the admin site at http://localhost:8000/admin.

Contributing
------------

Bug reports and pull requests are welcome on GitHub at https://github.com/maanavshah/spectre. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

License
-------

The app is available as open source under the terms.

# Rest Blog

A blog is a discussion or information website consisting of discrete text entries, often in an informal diary style. Entries are usually displayed in reverse chronological order, with the most recent entry appearing first, at the top of the web page. 

This project is developed with Django Rest Framework. Use the wonderful features of said framework, such as viewsets, routers, serializers and permissions. Also, implement django-cors-headers for API security.

## Quickstart

First of all, clone this repo.

``
git clone https://github.com/DD21S/rest-blog.git
``

Then, in the project directory, you install the requirements.

``
pip install -r requirements.txt
``

In the folder ``core/`` create a file called ``.env`` and set your environment variables. Do it like this:

``
DEBUG=True_or_False
SECRET_KEY=YOUR_SECRET_KEY
``

Now, make the migrations.

``
python3 manage.py migrate
``

Create a superuser.

``
python3 manage.py createsuperuser
``

And finally, run the project.

``
python3 manage.py runserver
``

Ready, now your rest blog is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create one with this command:

``
python3 -m venv venv
``
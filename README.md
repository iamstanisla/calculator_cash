# wsgi application on Flask  #
### the app does: ###
- user authentication and registration;
- forms for authentication and registration;
- loading and saving jpeg or png images on the app;
- using a factory method to create an instance Flask app;
- logging to file app/logs/app.log
- using Pony ORM for working with a database.

### application launch playback steps ###
You must have installed python==3.8 and git in you system.
```sh
$ git clone https://github.com/iamstanisla/calculator_cash.git
$ cd calculator_cash
$ mkdir app/logs 
$ python3 -m venv venv
$ activate
$ python3 -m pip install -r requirements/development.txt
$ python3 manage.py runserver
```
You will see messages about starting the server.
Open a url `localhost:5000` in yout browser.

# Cilent-Expenses-Django-Project
It is a Web App which will display the Expenses of client.

I have used Bootstrap and Djnago to make this web app.
The Djnago project contains 1 Web App and it's name is "Expenses"

DataBase:
I have used Django In built database which is SQLITE3

you can access the DB by loging in the admin Page
Below are the credentials of Admin.

Before accessing the URL please run the Server.

follow the below steps:
1) Open project using PyCharm IDE
2) Open terminal in PyCharm
3) Type python manage.py runserver to run the server

ADMIN PAGE URL
URL: http://127.0.0.1:8000/admin/

# user name and password of DJANGO admin
Username bhaaratsingh
Email address: 123@gmail.com
password: root@12345
#########################################


Few important URL related to the project

1. This url will display the list of Clients
URL: http://127.0.0.1:8000/expenses/index/

You can add new Clients using this page. For this feature i have used the Django Admin page.
So if you click on the "+add clients" button it will lead you the Django Admin page.



2. This URL will list all the expenses of a given client.

URL: http://127.0.0.1:8000/expenses/client/allexpenses/?c_id=1

In the url Paremeter c_id is the client id  you can pass different client ids to get different results.














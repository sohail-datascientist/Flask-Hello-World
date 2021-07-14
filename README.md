# Flask-Hello-World
Flask web Development framework task with detailed explanation and easy. 

Initially check that the flask is available or not, if it is not available the install it using pip install flask

After it create a folder in and in that folder place a file with the .py extension 

In .py file write the following code:


from flask import Flask

app=Flask(__name__)

@app.route("/")

def Task_01():
     return "Hello World of Programmers"
     

Now copy open the folder copy the path and paste it into the CMD Command line

Now set FLASK_APP=File_name_with_.py_extension

Executer the last command that is flask run

Now copy the URL and paste it into the browser your code will execute. 


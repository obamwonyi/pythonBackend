#importing the flask method
from flask import Flask
#importing the search4letters method
from vsearch import search4letters

#instantiating the Flask class  
app = Flask(__name__)

@app.route('/')
# the hello function will be returning a string 
def hello() -> str : 
    return 'Hello world from Flask!'

@app.route('/searched')

#function with the type hint of string 
#to return the value of a searched string 
def do_search() -> str : 
    searchedvalue = str(search4letters("This is the string to search for ", 'eiru,!'))
    return searchedvalue




app.run()
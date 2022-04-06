#importing the flask method
from django.shortcuts import redirect
from flask import Flask,render_template,request
#importing the search4letters method
from vsearch import search4letters

#instantiating the Flask class  
app = Flask(__name__)

@app.route('/')
# the hello function will be returning a string 
def hello() -> '302' : 
    return redirect('/entry')

@app.route('/search4',methods = ['POST'])

#function with the type hint of string 
#to return the value of a searched string 
def do_search() -> str : 
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results:"
    results = str(search4letters(phrase,letters))

    return render_template('results.html',the_phrase = phrase,
            the_letters = letters,
            the_title = title,
            the_results =results,)


@app.route('/entry')
def entry_page() :
    return render_template('entry.html',the_title ="Welcome to seach4letters on the web!")


app.run(debug=True)
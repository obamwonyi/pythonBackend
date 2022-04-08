# importing the flask method
from flask import Flask, render_template, request, escape
# importing the search4letters method
from vsearch import search4letters

# instantiating the Flask class
app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep="|")


@app.route('/search4', methods=['POST'])
# function with the type hint of string
# to return the value of a searched string
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)

# making the root directory / kind of full through to entry


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title="Welcome to seach4letters on the web!")


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)

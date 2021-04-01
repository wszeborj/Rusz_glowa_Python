from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': '',
        'database': 'vsearchlogDB',
    }
    import mysql.connector

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
    (phrase,  letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    conn.commit()

    cursor.close()
    conn.close()


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        data = log.readlines()

        for line in data:
            contents.append([])
            listone = line.split('|')
            for item in listone:
                contents[-1].append(escape(item))
    titles = ('Dane z formularza', 'Adres klienta', 'Agent użytkownika', 'Wyniki')
    return render_template(
        'viewlog.html',
        the_title='Widok logu',
        the_row='titles',
        the_data=contents,
    )



    return escape(contents)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto Twoje wyniki:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Witamy na stronie internetowej Search4letters!')


if __name__ == '__main__':
    app.run(debug=True)

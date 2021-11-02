from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'NigdyNieZgadniesz'


@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return f'Użytkownikiem jest: {session["user"]}'


@app.route('/getuser')
def getuser() -> str:
    return f'Użytkownikiem jest obecnie: {session["user"]}'


if __name__ == '__main__':
    app.run(debug=True)
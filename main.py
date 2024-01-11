from typing import Union

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return '<h1>Hello, world!</h1>'


@app.route('/user/<username>/<age>')
def user_info(username: str, age: Union[int, str]) -> str:
    info = (
        f'<h1>Hi, {username}!</h1><br>'
        f' <p>You are {age} years old.</p>'
    )
    return info


app.run(debug=True)

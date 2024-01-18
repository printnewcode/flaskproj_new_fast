import time
import random

from flask import Flask, render_template

from typing import Union

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template('index.html', name='Zaxar')


@app.route('/randomizer/<num_1>/<num_2>')
def randomizer(num_1, num_2) -> Union[str, int]:
    return render_template('random.html', numRandom=random.randint(int(num_1), int(num_2)))


@app.route('/time/')
def timer():
    seconds = time.time()
    local_time = time.ctime(seconds)
    return render_template('time.html', timeNow=local_time)


@app.route('/user/<username>/<age>')
def user_info(username: str, age: Union[int, str]) -> str:
    info = (
        f'<h1>Hi, {username}!</h1><br>'
        f' <p>You are {age} years old.</p>'
    )
    return info


app.run(debug=True)

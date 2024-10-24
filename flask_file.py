from flask import Flask, render_template, redirect
from trying_numpy_to_html import get_table

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("starting_screen.html")

@app.route('/', methods=['POST'])
def play():

    print("Hello")
    m_html = get_table()

    return render_template("play_template.html", table=m_html)



if __name__ == '__main__':
   app.run()


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/<x>')
def rows(x):
    return render_template("rows.html", r=int(x))

# @app.route('/play')
# def threebox():
#     return render_template("index.html")


# @app.route('/play/<x>')
# def addBlue(x):
#     n = int(x)
#     return render_template("play_x.html", y=n)


# @app.route('/play/<x>/<color>')
# def addColor(x, color):
#     n = int(x)
#     return render_template("play_color.html", y=n, c=color)


if __name__ == "__main__":
    app.run(debug=True)

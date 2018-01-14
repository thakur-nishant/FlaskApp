from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test/', methods=["POST"])
def test():
    try:
        if request.method == "POST":
            name = request.form['name']
            age = request.form['age']

        return "Welcome " + name + "! Your are " + age + " years old!"
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run()

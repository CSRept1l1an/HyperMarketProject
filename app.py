from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/shopping')
def index():
    return render_template('shopping.html')


@app.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

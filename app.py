from flask import Flask, render_template

app = Flask(__name__)

product_data = {
    1: {'name': 'Product 1', 'description': 'Brief description of Product 1.', 'price': 19.99},
    2: {'name': 'Product 2', 'description': 'Brief description of Product 2.', 'price': 29.99},
    3: {'name': 'Product 3', 'description': 'Brief description of Product 3.', 'price': 39.99},
    4: {'name': 'Product 4', 'description': 'Brief description of Product 4.', 'price': 49.99},
}


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('products.html', products=product_data)


@app.route('/product/<int:product_id>')
def product(product_id):
    product = product_data.get(product_id)
    if product:
        return render_template('product.html', product=product)
    else:
        return "Product not found", 404


@app.route('/shopping')
def shopping():
    return render_template('shopping.html')


@app.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

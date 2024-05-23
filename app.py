from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

product_data = {
    1: {'name': 'Product 1', 'description': 'Brief description of Product 1.', 'price': 19.99},
    2: {'name': 'Product 2', 'description': 'Brief description of Product 2.', 'price': 29.99},
    3: {'name': 'Product 3', 'description': 'Brief description of Product 3.', 'price': 39.99},
    4: {'name': 'Product 4', 'description': 'Brief description of Product 4.', 'price': 49.99},
    5: {'name': 'Product 5', 'description': 'Brief description of Product 5.', 'price': 59.99},
    6: {'name': 'Product 6', 'description': 'Brief description of Product 6.', 'price': 69.99},
}

shopping_list = {}


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('products.html', products=product_data)


# noinspection PyShadowingNames
@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    product = product_data.get(product_id)
    if not product:
        return "Product not found", 404

    if request.method == 'POST':
        if 'shopping_list' not in session:
            session['shopping_list'] = []
        session['shopping_list'].append(product)
        session.modified = True
        return redirect(url_for('shopping_list'))

    return render_template('product.html', product=product)


@app.route('/shopping')
def shopping_list():
    shopping_list = session.get('shopping_list', [])
    return render_template('shopping.html', shopping_list=shopping_list)


@app.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

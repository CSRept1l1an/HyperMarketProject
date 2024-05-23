from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

product_data = {
    1: {
        'name': 'Organic Whole Milk',
        'description': 'A gallon of fresh, organic whole milk, perfect for drinking, cooking, or baking.',
        'price': 3.99,
        'category': 'Dairy',
        'stock_quantity': 120,
        'link': 'https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/64b18f43ba6e3052a60c21ff_2023-cen-ecommerce-eb-organicwholemilk128fz.jpg'
    },
    2: {
        'name': 'Free-Range Large Eggs',
        'description': 'A dozen large eggs from free-range hens, rich in flavor and nutrients.',
        'price': 4.29,
        'category': 'Dairy',
        'stock_quantity': 80,
        'link': 'https://www.kerrysfresh.co.uk/wp-content/uploads/2016/08/Free-Range-Eggs.jpg'
    },
    3: {
        'name': 'Almond Granola Cereal',
        'description': 'Crunchy granola cereal with almonds, a healthy start to your day.',
        'price': 5.49,
        'category': 'Cereal',
        'stock_quantity': 150,
        'link': 'https://www-konga-com-res.cloudinary.com/w_400,f_auto,fl_lossy,dpr_3.0,q_auto/media/catalog/product/R/R/192370_1630070057.jpg'
    },
    4: {
        'name': 'Whole Wheat Bread',
        'description': 'Freshly baked whole wheat bread, perfect for sandwiches and toast.',
        'price': 2.99,
        'category': 'Bakery',
        'stock_quantity': 200,
        'link': 'https://bakingamoment.com/wp-content/uploads/2019/01/IMG_2403-best-soft-whole-wheat-bread-recipe.jpg'
    },
    5: {
        'name': 'Natural Peanut Butter',
        'description': 'Creamy natural peanut butter made from 100% roasted peanuts.',
        'price': 6.79,
        'category': 'Pantry',
        'stock_quantity': 75,
        'link': 'https://www.foodandwine.com/thmb/u8U9iCm-u6Ryp_WrB8iIk6BTIxY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/peanut-buter-natural-conventional-FT-BLOG0517-98200eb4202a41bebc5746a8b72edc48.jpg'
    },
    6: {
        'name': 'Organic Baby Spinach',
        'description': 'Fresh organic baby spinach, great for salads, smoothies, and cooking.',
        'price': 3.49,
        'category': 'Produce',
        'stock_quantity': 100,
        'link': 'https://storage.googleapis.com/images-sof-prd-9fa6b8b.sof.prd.v8.commerce.mi9cloud.com/product-images/zoom/00032601952983.jpg'
    },
    7: {
        'name': 'Boneless Chicken Breasts',
        'description': 'A pack of boneless, skinless chicken breasts, perfect for grilling or baking.',
        'price': 9.99,
        'category': 'Meat',
        'stock_quantity': 60,
        'link': 'https://i5.walmartimages.com/seo/Boneless-Skinless-Chicken-Breasts-4-7-6-1-lb-Tray_4693e429-b926-4913-984c-dd29d4bdd586.780145c264e407b17e86cd4a7106731f.jpeg'
    },
    8: {
        'name': 'Wild Caught Salmon Fillet',
        'description': 'Fresh wild-caught salmon fillet, rich in omega-3 fatty acids.',
        'price': 12.99,
        'category': 'Seafood',
        'stock_quantity': 50,
        'link': 'https://wildalaskasalmonandseafood.com/wp-content/uploads/2021/05/kingrawb17.jpg'
    },
    9: {
        'name': 'Turkish Yogurt',
        'description': 'Creamy Greek yogurt, available in various flavors.',
        'price': 1.99,
        'category': 'Dairy',
        'stock_quantity': 180,
        'link': 'https://www.yasarhalim.com/images/thumbs/0019476_yayla-turkish-cream-yoghurt-6-800g_510.jpeg'
    },
    10: {
        'name': 'Apple Cider Vinegar',
        'description': 'Organic apple cider vinegar with the mother, great for health and cooking.',
        'price': 4.49,
        'category': 'Pantry',
        'stock_quantity': 90,
        'link': 'https://media.post.rvohealth.io/wp-content/uploads/2021/07/apple-cider-vinegar-1200x628-facebook-732x549.jpg'
    },
    11: {
        'name': 'Quinoa',
        'description': 'Organic quinoa, a versatile and healthy grain.',
        'price': 7.99,
        'category': 'Pantry',
        'stock_quantity': 120,
        'link': 'https://nuttyyogi.com/cdn/shop/products/Quinoa_White.jpg?v=1677652891'
    },
    12: {
        'name': 'Blueberries',
        'description': 'Fresh organic blueberries, perfect for snacking and baking.',
        'price': 5.99,
        'category': 'Produce',
        'stock_quantity': 130,
        'link': 'https://images.immediate.co.uk/production/volatile/sites/30/2017/01/Blueberries-in-a-bowl-ffafdbe.jpg?quality=90&resize=556,505'
    },
    13: {
        'name': 'Cheddar Cheese',
        'description': 'A block of sharp cheddar cheese, great for sandwiches and cooking.',
        'price': 6.49,
        'category': 'Dairy',
        'stock_quantity': 70,
        'link': 'https://shop.burnettdairy.com/cdn/shop/products/BD_MildChed.jpg?v=1589903792'
    },
    14: {
        'name': 'Olive Oil',
        'description': 'Extra virgin olive oil, perfect for cooking and salads.',
        'price': 8.99,
        'category': 'Pantry',
        'stock_quantity': 110,
        'link': 'https://www.netmeds.com/images/cms/wysiwyg/blog/2019/05/Olive_oil_898.jpg'
    },
    15: {
        'name': 'Mixed Nuts',
        'description': 'A bag of mixed nuts, a healthy and tasty snack.',
        'price': 10.49,
        'category': 'Snacks',
        'stock_quantity': 95,
        'link': 'https://cdn.mafrservices.com/sys-master-root/hf6/h6a/50283050205214/23180_Main.jpg?im=Resize=480?im=Resize=(60,60)'
    },
    16: {
        'name': 'Frozen Peas',
        'description': 'A bag of organic frozen peas, perfect for adding to various dishes.',
        'price': 2.29,
        'category': 'Frozen',
        'stock_quantity': 140,
        'link': 'https://cdnprod.mafretailproxy.com/sys-master-root/hf4/hf8/13955750690846/84553_main.jpg_480Wx480H'
    },
    17: {
        'name': 'Heinz Tomato Sauce',
        'description': 'Organic tomato sauce, great for pasta and cooking.',
        'price': 3.79,
        'category': 'Pantry',
        'stock_quantity': 100,
        'link': 'https://static.thcdn.com/images/large/original//productimg/1600/1600/14936299-1635087475500265.jpg'
    },
    18: {
        'name': 'Dishwashing Liquid',
        'description': 'Eco-friendly dishwashing liquid, tough on grease but gentle on hands.',
        'price': 3.49,
        'category': 'Household',
        'stock_quantity': 200,
        'link': 'https://www.sunlight.co.za/images/h0nadbhvm6m4/5V9JXopXHIokre6oGF1ZaV/c24a95f4fb5fce82a8e48743efff5e37/U0RXTF83NTBtbF9ib3R0bGVfcGFja3Nob3QucG5n/1080w-1080h/sunlight-dishwashing-liquid.jpg'
    },
    19: {
        'name': 'Baby Diapers',
        'description': 'Pack of eco-friendly baby diapers, comfortable and absorbent.',
        'price': 19.99,
        'category': 'Baby',
        'stock_quantity': 60,
        'link': 'https://www.bigbasket.com/media/uploads/p/l/40136606_5-pampers-diaper-pants-new-born.jpg'
    },
    20: {
        'name': 'Shampoo',
        'description': 'Natural shampoo with organic ingredients, suitable for all hair types.',
        'price': 7.49,
        'category': 'Personal Care',
        'stock_quantity': 85,
        'link': 'https://i5.walmartimages.com/seo/Head-and-Shoulders-Dandruff-Shampoo-Classic-Clean-8-45-fl-oz_5b87459e-fbdc-4a00-b90d-62d18147773e.a33e5019754b5677a089a08c9d8dea30.jpeg'
    }
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

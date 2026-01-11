from flask import Flask, render_template, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cloud-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database and seed data
with app.app_context():
    db.create_all()
    if not Product.query.first():
        products = [
            Product(name='Laptop Pro', price=1299.99),
            Product(name='Smartphone X', price=899.99),
            Product(name='Wireless Headphones', price=199.99),
            Product(name='Tablet 12"', price=599.99),
            Product(name='Smart Watch', price=299.99),
            Product(name='Gaming Mouse', price=79.99)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    if product_id not in session['cart']:
        session['cart'].append(product_id)
        session.modified = True
    return jsonify({'status': 'added', 'count': len(session['cart'])})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

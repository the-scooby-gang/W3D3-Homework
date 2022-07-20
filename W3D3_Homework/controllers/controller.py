from app import app
from flask import render_template
from models.shop_orders import orders


@app.route('/')
def index():
    return "Welcome to Aimee's Magic Shop"

@app.route('/magic_shop')
def tasks():
    return render_template('index.html', title = 'shop_orders', orders = orders)


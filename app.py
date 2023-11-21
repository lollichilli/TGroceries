from flask import redirect, url_for, request, render_template, jsonify
from config import app, db
from models import Products, ProductsSchema

cart_items = {}

@app.route("/")
def show_options():
    return render_template("base.html")

@app.route("/list")
def show_roster():
    products = Products.query.all()
    products_schema = ProductsSchema(many=True)
    return render_template("list.html", list=products_schema.dump(products))

@app.route("/add", methods=["GET", "POST"])
def show_admin_ui():
    if request.method == "GET":
        return render_template("add.html", text="")
    try:
        new = Products(
            name=request.form.get("fruit_name"),
            kind=request.form.get("fruit_kind"),
            owner=request.form.get("fruit_owner"),
            price=int(request.form.get("fruit_price")),
            image_url=request.form.get("image_url")
        )
        db.session.add(new)
        db.session.commit()
        return render_template('add.html', text=f"The fruit {request.form.get('fruit_name')} has been added to the store.")
    except:
        return render_template('add.html', text="Something went wrong.")

@app.route("/owner")
def owner_page():
    products = Products.query.all()
    products_schema = ProductsSchema(many=True)
    return render_template("owner.html", list=products_schema.dump(products))

@app.route("/edit/<string:name>", methods=["GET", "POST"])
def edit_product(name):
    product = Products.query.get(name)
    products_schema = ProductsSchema(many=True)
    if request.method == "POST":
        product.name = request.form.get("fruit_name")
        product.kind = request.form.get("fruit_kind")
        product.owner = request.form.get("fruit_owner")
        product.price = int(request.form.get("fruit_price"))
        image_url=request.form.get("image_url")
        db.session.commit()
        return render_template('owner.html', list=products_schema.dump(Products.query.all()))
    return render_template("edit.html", product=product)

@app.route("/remove/<string:name>")
def remove_product(name):
    product = Products.query.get(name)
    if product:
        db.session.delete(product)
        db.session.commit()
    return redirect(url_for('owner_page'))



@app.route("/cart")
def show_cart():
    total_amount = calculate_total_amount(cart_items)
    return render_template("cart.html", cart_items=cart_items, total_amount=total_amount)

def calculate_total_amount(cart_items):
    total_amount = 0
    for details in cart_items.values():
        total_amount += details["price"] * details["quantity"]
    return total_amount

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_name = request.form.get("product_name")
    quantity = int(request.form.get("quantity"))

    product = Products.query.filter_by(name=product_name).first()

    if product:
        if product_name in cart_items:
            cart_items[product_name]["quantity"] += quantity
        else:
            cart_items[product_name] = {
                "quantity": quantity,
                "image_url": product.image_url,
                "kind": product.kind,
                "price": product.price,
            }

        return {"message": f"Added {quantity} {product_name} to the cart!"}
    else:
        return {"message": f"Product {product_name} not found."}, 404

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_name = request.form.get("product_name")
    print("Removing item:", product_name)

    if product_name in cart_items:
        del cart_items[product_name]

        total_amount = calculate_total_amount(cart_items)
        print("Total Amount after removal:", total_amount)
        print("Cart Items after removal:", cart_items)  # Add this line

        return jsonify({"success": True, "total_amount": total_amount})
    else:
        print(f"Product {product_name} not found.")
        return jsonify({"success": False, "message": f"Product {product_name} not found."})

if __name__ == "__main__":
    app.run(debug=True)


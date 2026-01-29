from flask import Flask, jsonify, request

app = Flask(__name__) # Instance of Flask
# Flask works with GET on default


# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index(): 
    return "Welcome to the Flask Framework!"

# http://127.0.0.1:5000/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello world from Flask!"

# http://127.0.0.1:5000/cohort-63
@app.route("/cohort-63", methods=["GET"])
def cohort_63():
    student_list = ["Robert", "Barney", "Luis", "Lemuel", "Reece", "John", "Angel"]
    return student_list


# http://127.0.0.1:5000/cohort-63
# @app.route("/cohort-63", methods=["GET"])
# def cohort_63():
    # return ["Robert", "Barney", "Luis", "Lemuel", "Reece", "John", "Angel"]


# http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods=["GET"])
def cohort_99():
    student_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
    return student_list

# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {
        "email": "stephtruitt8@sdgku.edu",
        "phone": "1-800-555-1234"
    }
    return information

# http://127.0.0.1:5000/course-infomation
@app.route("/course-infomation", methods=["GET"])
def course_information():
    course_data = {
        "title": "Introduction Web API with Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }
    return course_data


# Path Parameter
# is a dynamic part of the URL used to identify a specific item or resource within an API.
# http://127.0.0.1.5000/greet/<name>

@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    print(f"this is the name {name}")
    return jsonify({"message": f"Hello {name}!"}), 200 # HTTP status code 200 means OK


products = [
    {
    "_id": 1,
    "title": "Nintendo Switch",
    "price": 299.99,
    "category": "Electronics",
    "image": "http://picsum.photos/seed/1/200/300"
    },
    {
    "_id": 2,
    "title": "Smart Refrigerator",
    "price": 899.99,
    "category": "Electronics",
    "image": "http://picsum.photos/seed/2/200/300"
    },
    {
    "_id": 3,
    "title": "Running Shoes",
    "price": 79.99,
    "category": "Footwear",
    "image": "http://picsum.photos/seed/3/200/300"
    },
]

# GET /api/products, endpoint that returns a list of products

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(
        {
            "success": True,
            "message": "Products retrieved successfully",
            "products": products,
        }),  200 # OK


# GET /api/products/3
@app.route("/api/products/<int:product_id>")
def get_products_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify(
                {
                    "success": True,
                    "message": "Product retrieved successfully",
                    "product": product
                }), 200 # OK


    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # Not Found


# POST /api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify(
        {
            "success": True,
            "message": "Product created successfully",
            "product": new_product
        }), 201 # Created


# DELETE /api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    for index, product in enumerate(products):
        if product["_id"] == product_id:
            products.pop(index)
            return jsonify({
                "success": True,
                "message": "Product deleted successfully"
            }), 200 # OK

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # Not Found


# PUT /api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    for product in products:
        if product["_id"] == product_id:
            product["title"] = data["title"]
            product["price"] = data["price"]
            product["category"] = data["category"]
            product["image"] = data["image"]

            return jsonify({
                "success": True,
                "message": "Product updated successfully",
                "data": product
            }), 200 # OK

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # Not Found




# ---- Coupons ----

# http://127.0.0.1:5000/coupons
@app.route("/coupons", methods=["GET"])
def coupons():
    coupon_list = [
        {"_id": 1, "code":  "SAVE10", "discount": "10%"},
        {"_id": 2, "code":  "FREESHIP", "discount": "Free Shipping"},
        {"_id": 3, "code":  "WELCOME15", "discount": "15%"}
    ]
    return coupon_list

# http://127.0.0.1:5000/coupons-count
@app.route("/coupons-count", methods=["GET"])
def coupon_count():
    return {"count": 3} 


#GET /api/coupons

@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupons():
    coupons = [
        {"_id": 1, "code": "SAVE10", "discount": "10%"},
        {"_id": 2, "code": "FREESHIP", "discount": "Free Shipping"},
        {"_id": 3, "code": "WELCOME15", "discount": "15%"}
    ]
    return jsonify(
        {
            "success": True,
            "message": "Coupons retrieved successfully",
            "coupons": coupons
        }), 200 # OK


#POST /api/coupons

@app.route("/api/coupons/<int:coupon_id>", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    print(new_coupon)
    return jsonify(
        {
            "success": True,
            "message": "Coupon created successfully",
            "coupon": new_coupon
        }), 201 # Created


# PUT /api/coupons/<int:coupon_id>

@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon(coupon_id):
    data = request.get_json()
    for product in products:
        if product["_id"] == product_id:
            product["code"] = data["code"]
            product["discount"] = data["discount"]

            updated_coupon = {
                "_id": coupon_id,
                "code": data["code"],
                "discount": data["discount"]
            }

    return jsonify({
        "success": True,
        "message": "Coupon updated successfully",
        "coupon": updated_coupon
    }), 200 # OK



# DELETE /api/coupons/<int:coupon_id>

@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon(coupon_id):
    for index, coupon in enumerate(coupons):
        if coupon["_id"] == coupon_id:
            coupons.pop(index)

            return jsonify({
                "success": True,
                "message": "Coupon deleted successfully"
            }), 200 # OK

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404 # Not Found



#-----

if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module: __name__ == "server.py"

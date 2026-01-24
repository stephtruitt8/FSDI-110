from flask import Flask 

app = Flask(__name__) # Instance of Flask


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


# ---- Coupons ----

# http://127.0.0.1:5000/coupons
@app.route("/coupons", methods=["GET"])
def coupons():
    coupon_list = [
        {"code":  "SAVE10", "discount": "10%"},
        {"code":  "FREESHIP", "discount": "Free Shipping"},
        {"code":  "WELCOME15", "discount": "15%"}
    ]
    return coupon_list

# http://127.0.0.1:5000/coupons-count
@app.route("/coupons-count", methods=["GET"])
def coupon_count():
    return {"count": 3} 

if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module: __name__ == "server.py"
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "supersecret"  # needed for forms/flash messages

# Mock products
products = [
    {"name": "Handmade Scarf", "desc": "Soft wool, cozy and warm", "price": "£25", "image": "scarf.jpg"},
    {"name": "Crochet Teddy", "desc": "Cute and cuddly teddy bear", "price": "£30", "image": "teddy.jpg"},
    {"name": "Wool Hat", "desc": "Stylish winter essential", "price": "£20", "image": "hat.jpg"}
]

recent_creations = [
    {"title": "Crochet Bunny", "video": "https://www.instagram.com/embed/video/123"},
    {"title": "Knitted Blanket", "video": "https://www.facebook.com/embed/video/456"}
]

# Store orders temporarily (in memory for now)
custom_orders = []

@app.route("/")
def home():
    return render_template("index.html", products=products, recent_creations=recent_creations)

@app.route("/made-to-order", methods=["GET", "POST"])
def made_to_order():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        idea = request.form.get("idea")
        color = request.form.get("color")
        size = request.form.get("size")

        order = {
            "name": name,
            "email": email,
            "idea": idea,
            "color": color,
            "size": size
        }
        custom_orders.append(order)
        print("New Custom Order:", order)  # for debugging

        flash("Thank you! Your request has been submitted. Thira will contact you soon ❤️")
        return redirect(url_for("made_to_order"))

    return render_template("made_to_order.html")
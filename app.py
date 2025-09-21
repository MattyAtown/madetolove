from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "supersecret"  # needed for forms/flash messages

# --- NEW grouped product data ---
top_ranges = {
    "Knitted Xmas Range": [
        {"name":"Festive Reindeer Hat","desc":"Cozy knit with antlers","price":"£22","image":"xmas_hat.jpg"},
        {"name":"Mini Stocking Set","desc":"Set of 3 ornaments","price":"£18","image":"xmas_stockings.jpg"},
    ],
    "Knitted Easter Range": [
        {"name":"Easter Bunny","desc":"Hand-knit bunny plush","price":"£28","image":"easter_bunny.jpg"},
        {"name":"Pastel Egg Cozies","desc":"Set of 4","price":"£14","image":"easter_eggcozies.jpg"},
    ],
    "Knitted Halloween Range": [
        {"name":"Pumpkin Plush","desc":"Soft knit pumpkin","price":"£16","image":"halloween_pumpkin1.jpg"},
        {"name":"Spooky Bat","desc":"Cute, not scary!","price":"£18","image":"halloween_bat.jpg"},
    ],
    "Knitted Home Range": [
        {"name":"Cable Cushion Cover","desc":"18'' x 18''","price":"£26","image":"home_cushion.jpg"},
        {"name":"Chunky Throw","desc":"120×150cm","price":"£55","image":"home_throw.jpg"},
    ],
    "Knitted Baby Range": [
        {"name":"Baby Booties","desc":"0–6 months","price":"£12","image":"baby_booties.jpg"},
        {"name":"Cot Blanket","desc":"Soft & breathable","price":"£38","image":"baby_blanket.jpg"},
    ],
    "Hand made flower Range": [
        {"name":"Crochet Rose Bouquet","desc":"Set of 5","price":"£24","image":"flower_roses.jpg"},
        {"name":"Sunflower Stem","desc":"Lifelike crochet","price":"£10","image":"flower_sunflower.jpg"},
    ]
}

# --- Recent Creations (can embed social vids later) ---
recent_creations = [
    {"title": "Crochet Bunny – timelapse", "video": "https://www.instagram.com/embed/video/123"},
    {"title": "Chunky Throw – process", "video": "https://www.facebook.com/embed/video/456"},
]

# --- ROUTES ---
@app.route("/")
def home():
    return render_template("index.html", top_ranges=top_ranges, recent_creations=recent_creations)

# keep your other routes here (e.g. made-to-order, etc.)

if __name__ == "__main__":
    app.run(debug=True)

# Store orders temporarily (in memory for now)
custom_orders = []

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


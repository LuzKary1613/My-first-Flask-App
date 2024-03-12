from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

     
        if username and username[0].isupper() and username[1:].islower() and any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
            return redirect(url_for("login_success"))

    return render_template("login.html")

@app.route("/login_success")
def login_success():
    return "Login Successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

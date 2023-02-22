from flask import Flask,render_template,url_for
app=Flask(__name__)

@app.route("/")
def sample():
    return render_template("login.html")

@app.route("/login")
def log():
    return render_template("login.html")

@app.route("/register")
def reg():
    return render_template("register.html")

@app.route("/Home")
def home():
    return render_template("Home.html")

if __name__=="__main__":
    app.run()
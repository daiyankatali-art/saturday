from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("hosting.html")


@app.route("/student info.html")
def projects():
    return render_template("student info.html")
    


if __name__=="__main__":
    app.run(debug=True)
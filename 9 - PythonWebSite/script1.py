from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home2.html")

@app.route('/about')
def about():
    return render_template("about2.html")

@app.route('/contato')
def contato():
    return "Contate-nos amanhã"

if __name__ == "__main__":
    app.run(debug=True)
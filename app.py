from flask import Flask
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/hello')
def hello():
    name = "Karan"
    data = [1,2,3,4,5,6,]
    return render_template("hello.html", data=data, name = name)


@app.route('/form')
def form():
    return render_template("form.html")


@app.route("/subform",methods=['POST'])
def subform():
    if request.method == 'POST':
        name = request.form['nm']
        num = request.form['num']
        return render_template("form.html", formname = name, formnum = num )
    else:
        return "not rum ....."

if __name__ == "__main__":
    app.run(debug=True)
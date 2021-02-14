from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/page_2')
def page_2():
    return render_template('page_2.html')

@app.route('/page_3')
def page_3():
    return render_template('page_3.html')

if __name__ == "__main__":
    app.run(debug=True)
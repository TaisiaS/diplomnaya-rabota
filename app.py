from flask import Flask, render_template
from database import get_spo
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/spo')
def spo():
    return render_template('spo.html')

@app.route('/uni')
def spo():
    return render_template('uni.html')

app.run(debug=True)
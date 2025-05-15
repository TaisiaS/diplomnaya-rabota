from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/spo')
def spo():
    return render_template('spo.html')


app.run(debug=True)
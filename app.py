from flask import Flask, render_template
from database import get_spo, get_uni
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/spo')
def spo():

    spo_list = get_spo()
    return render_template(
        'spo.html',
        title="СПО",
        spo_list = spo_list, 
    )

@app.route('/uni')
def uni():
    uni_list = get_uni()
    return render_template(
        'uni.html',
        title="ВУЗ",
        uni_list = uni_list, 
    )

@app.route('/formspo')
def formspo():
    return render_template('formspo.html')


@app.route('/formuni')
def formuni():
    return render_template('formuni.html')


app.run(debug=True)
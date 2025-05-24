from flask import Flask, render_template, request
from database import get_spo, get_uni
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/spo')
def spo():

    spo_list = get_spo(1000)
    return render_template(
        'spo.html',
        title="СПО",
        spo_list = spo_list, 
    )

@app.route('/uni')
def uni():
    uni_list = get_uni(1000)
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


@app.route('/serchspo', methods=['GET', 'POST'])
def search_spo():
    if request.method == 'POST':
        search_spo = float(request.form['search_spo'])
        spo_list = get_spo(search_spo)
        return render_template(
            'spo.html',
            title="СПО",
            spo_list = spo_list,
        )
    return render_template('formspo.html', title='searchspo')


@app.route('/serchuni', methods=['GET', 'POST'])
def search_uni():
    if request.method == 'POST':
        search_uni = float(request.form['search_uni'])
        uni_list = get_uni(search_uni)
        return render_template(
            'uni.html',
            title="ВУЗ",
            uni_list = uni_list, 
        )
    return render_template('formuni.html', title='searchuni')

app.run(debug=True)
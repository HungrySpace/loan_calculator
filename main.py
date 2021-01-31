from flask import Flask, render_template, Response, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def move_forward():
    money = float(request.form['money'])
    time = int(request.form['time'])
    prc = float(request.form['prc'])
    row = get_table(money, time, prc)
    return render_template('result.html', row=row)


@app.route('/contact')
def contact():
    return render_template('contact.html')


def get_table(money, time, prc):
    arr_table = [['Месяц', 'Платеж', 'Проценты', 'Тело займа', 'Остаток']]
    p = prc/100/12

    # x = money * (p + (p + (((1 + p)**time) - 1)))
    vvv = (1 + p)**time - 1
    vv = p / vvv
    v = p + vv
    x = round(money * v)
    for i in range(time):
        money -= round(x - (money * p))
        if money < 0:
            money = 0
        arr_table.append([i+1, x, round(money * p), round(x - (money * p)), round(money)])

    print(arr_table)
    return arr_table


if __name__ == "__main__":
    app.run(debug=True)

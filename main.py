from flask import Flask, render_template, request, jsonify


#以下是载入首页的公式方法
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    return render_template("bmi.html")
    



#以下是汇率转换工具的公式方法
exchange_rates = {
    "USD": {"CNY": 7.2, "EUR": 0.92},
    "CNY": {"USD": 0.14, "EUR": 0.13},
    "EUR": {"USD": 1.09, "CNY": 7.85},
}


@app.route("/exchange", methods=["GET", "POST"])
def exchange():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        if from_currency == to_currency:
            result = f"{amount:.2f} {from_currency} = {amount:.2f} {to_currency}"
        else:
            rate = exchange_rates[from_currency][to_currency]
            converted = amount * rate
            result = f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}"

    return render_template("exchange.html", result=result)



#以下是bmi转换工具的公式方法
@app.route("/bmi_ajax", methods=["POST"])
def bmi_ajax():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100
        bmi = round(weight / (height ** 2), 2)
        return jsonify(result=f"你的 BMI 是 {bmi}")
    except:
        return jsonify(result="计算失败，请稍后再试")
    


#以下是卡路里计算公式方法
@app.route('/calorie', methods=['GET', 'POST'])
def calorie():
    result = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        time = float(request.form['time'])
        activity = request.form['activity']
        factor = {'running': 0.12, 'walking': 0.05, 'cycling': 0.07}
        result = round(weight * time * factor.get(activity, 0), 2)
    return render_template('calorie.html', result=result)

#以下是五险一金计算公式方法
@app.route('/insurance', methods=['GET', 'POST'])
def insurance():
    result = None
    if request.method == 'POST':
        salary = float(request.form['salary'])
        rate = 0.22  # 养老8%、医保2%、失业0.5%、公积金12%等
        result = round(salary * rate, 2)
    return render_template('insurance.html', result=result)

#以下是离职补偿计算公式方法
@app.route('/compensation', methods=['GET', 'POST'])
def compensation():
    result = None
    if request.method == 'POST':
        salary = float(request.form['salary'])
        years = int(request.form['years'])
        result = round(salary * (years + 1), 2)  # N+1
    return render_template('compensation.html', result=result)

#以下是星座判断计算公式方法
@app.route('/zodiac', methods=['GET', 'POST'])
def zodiac():
    result = None
    if request.method == 'POST':
        birth = request.form['birth']
        month, day = map(int, birth.split('-'))
        zodiac_list = [
            (120, "摩羯座"), (219, "水瓶座"), (321, "双鱼座"), (420, "白羊座"),
            (521, "金牛座"), (621, "双子座"), (722, "巨蟹座"), (823, "狮子座"),
            (923, "处女座"), (1023, "天秤座"), (1122, "天蝎座"), (1222, "射手座"), (1231, "摩羯座")
        ]
        m_d = month * 100 + day
        for date, name in zodiac_list:
            if m_d <= date:
                result = name
                break
    return render_template('zodiac.html', result=result)

#以下是公历农历计算公式方法
@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    result = None
    if request.method == 'POST':
        date = request.form['date']
        result = f"（示例）农历：模拟转换 {date}"
    return render_template('calendar.html', result=result)

#以下是复利计算公式方法
@app.route('/compound', methods=['GET', 'POST'])
def compound():
    result = None
    years = 0
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate']) / 100
        years = int(request.form['years'])
        result = round(principal * (1 + rate) ** years, 2)
    return render_template('compound.html', result=result, years=years)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    result = ""
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # Convertir a metros
        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            result = "Bajo peso"
        elif 18.5 <= bmi < 24.9:
            result = "Peso normal"
        elif 25 <= bmi < 29.9:
            result = "Sobrepeso"
        else:
            result = "Obesidad"
    return render_template('index.html', bmi=bmi, result=result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    features = ['Nitrogen', 'Phosphorus', 'Potassium',
                'Soiltype_Clay', 'Soiltype_Loam', 'Soiltype_Sandy',
                'Crop_Barley', 'Crop_Corn', 'Crop_Rice']

    if request.method == 'POST':
        data = [float(request.form.get(f)) for f in features]
        # Replace this with your model prediction logic
        prediction = "Healthy" if sum(data) > 100 else "Unhealthy"

    return render_template('index.html', features=features, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

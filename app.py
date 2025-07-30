from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    dimensions = data.get('dimensions')

    try:
        length, breadth = map(float, dimensions.lower().replace('x', '*').split('*'))
        area_sqft = length * breadth
        cents = area_sqft / 435.6
        ankhanams = area_sqft / 72
        sq_meters = area_sqft * 0.092903
        sq_yards = area_sqft / 9

        return jsonify({
            'area_sqft': round(area_sqft, 2),
            'cents': round(cents, 2),
            'ankhanams': round(ankhanams, 2),
            'sq_meters': round(sq_meters, 2),
            'sq_yards': round(sq_yards, 2)
        })
    except Exception as e:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)

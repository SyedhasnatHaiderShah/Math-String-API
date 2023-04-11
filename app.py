from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()

    if not data or 'numbers' not in data or not isinstance(data['numbers'], list):
        return jsonify({'error': 'Invalid input. Expecting a JSON object with a list of numbers.'}), 400

    try:
        result = sum([float(num) for num in data['numbers']])
        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Elements in the list must be numbers.'}), 400

@app.route('/concat', methods=['POST'])
def concat_strings():
    data = request.get_json()

    if not data or 'string1' not in data or 'string2' not in data:
        return jsonify({'error': 'Invalid input. Expecting a JSON object with two strings.'}), 400

    if not isinstance(data['string1'], str) or not isinstance(data['string2'], str):
        return jsonify({'error': 'Invalid input. Both inputs must be strings.'}), 400

    result = data['string1'] + data['string2']
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

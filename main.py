from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    cats = int(data['cats'])
    dogs = int(data['dogs'])
    response = {'cats': str(cats + 1), 'dogs': str(dogs - 1)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

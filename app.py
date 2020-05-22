from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(message="Welcom to Planetary API 2020"), 200

@app.route('/simple_api')
def simple_api():
    return jsonify(message="Simple API"), 200

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f"Sorry {name}, you are not allowed"), 401
    else:
        return jsonify(message=f"Welcome {name}, you are old enough"), 200


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message=f"Sorry {name}, you are not allowed"), 401
    else:
        return jsonify(message=f"Welcome {name}, you are old enough"), 200


if __name__ == '__main__':
    app.run()

from flask import Flask, request, Response, make_response, jsonify

app = Flask('main')

@app.route('/', methods=['GET'])
def main_view():
    query_params = request.args
    name = query_params.get('name')
    age = query_params.get('age')
    city = query_params.get('city')
    template = 'Received beautiful parameters! name: {}, age: {}, city: {}.'
    msg = template.format(name, age, city)
    return make_response(msg, '200')

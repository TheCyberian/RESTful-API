from flask import Flask, jsonify, request

app = Flask(__name__)
languages = [{'name' : 'js'}, {'name' : 'ruby'}, {'name' : 'python'}]

#GET methods
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Hello World'})

@app.route('/lang', methods=['GET'])
def return_all_languages():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def return_given_languages(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

#POST method
@app.route('/lang', methods=['POST'])
def add_one_language():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})

#PUT method
@app.route('/lang/<string:name>', methods=['PUT'])
def edit_0ne_language(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'languages' : langs[0]})

#DELETE method
@app.route('/lang/<string:name>', methods=['DELETE'])
def delete_language(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'languages' : languages})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)
languages = [{'name' : 'js'}, {'name' : 'ruby'}, {'name' : 'python'}]

#GET methods
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Hello World'})

@app.route('/lang', methods=['GET'])
def return_all_languages():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def return_given_languages(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

#POST method
@app.route('/lang', methods=['POST'])
def add_one_language():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})

#PUT method
@app.route('/lang/<string:name>', methods=['PUT'])
def edit_0ne_language(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'languages' : langs[0]})

#DELETE method
@app.route('/lang/<string:name>', methods=['DELETE'])
def delete_language(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'languages' : languages})


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask


app = Flask(__name__)


@app.route('/<name>', methods=['GET'])
def hello_world(name):
    return 'hello {}'.format(name)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

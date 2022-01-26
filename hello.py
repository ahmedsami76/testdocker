from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Hello world! Again!!!'

@app.route('/aboshaymaa')
def test():
    return 'A7la mesa on you from Abushaymaa ;)'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)
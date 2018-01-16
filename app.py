from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/sp3581')
def sp():
    return render_template('webpage.html')

if __name__ == '__main__':
    app.run()

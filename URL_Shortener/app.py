from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url_received = request.form["name"]
        return url_received
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
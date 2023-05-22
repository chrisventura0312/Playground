from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play') #level 1
def home():
    return render_template('index.html', times=3)

@app.route('/play/<int:num>') #level 2
def play_num(num):
    return render_template('index.html', times= num)

@app.route('/play/<int:num>/<string:color>') #level 3
def play_num_color(num, color):
    return render_template('index.html', times=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)




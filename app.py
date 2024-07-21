from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def default():
    return redirect(url_for('index'))


@app.route('/trang-chu')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
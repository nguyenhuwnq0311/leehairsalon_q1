from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/trang-chu')
# def home():
#     return render_template('home.html')
# @app.route('/ve-chung-toi')
# def about():
#     return render_template('about.html')
# @app.route('/dat-hen')
# def schedule():
#     return render_template('schedule.html')
# @app.route('/chinh-sach-bao-hanh')
# def policy():
#     return render_template('policy.html')
# @app.route('/tin-tuc')
# def news():
#     return render_template('news.html')
# @app.route('/bang-gia-dich-vu')
# def price():
#     return render_template('price.html')


if __name__ == '__main__':
    app.run(debug=True)

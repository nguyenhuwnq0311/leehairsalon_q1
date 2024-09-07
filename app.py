# from flask import Flask, render_template, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def default():
#     return redirect(url_for('home'))

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

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Route chuyển hướng từ / đến /trang-chu
@app.route('/')
def default():
    return redirect(url_for('home'))

# Các route trang chính
@app.route('/trang-chu')
def home():
    return render_template('home.html')

@app.route('/ve-chung-toi')
def about():
    return render_template('about.html')

@app.route('/dat-hen')
def schedule():
    return render_template('schedule.html')

@app.route('/chinh-sach-bao-hanh')
def policy():
    return render_template('policy.html')

@app.route('/tin-tuc')
def news():
    return render_template('news.html')

@app.route('/bang-gia-dich-vu')
def price():
    return render_template('price.html')

# Route để phục vụ file robots.txt
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')

# Route để phục vụ file sitemap.xml
@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(app.root_path, 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)

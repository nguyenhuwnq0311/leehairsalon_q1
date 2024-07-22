from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('home.html')  # Render home.html for the root URL

@app.route('/home')
def home_redirect():
    return redirect(url_for('index'))  # Redirect to the index route

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

if __name__ == '__main__':
    app.run(debug=True)

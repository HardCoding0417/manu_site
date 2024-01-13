from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='odette_files')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio1')
def portfolio1():
    return render_template('portfolio1.html')
@app.route('/portfolio2')
def portfolio2():
    return render_template('portfolio2.html')
@app.route('/portfolio3')
def portfolio3():
    return render_template('portfolio3.html')

if __name__ == '__main__':
    app.run(debug=True)
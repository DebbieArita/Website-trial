from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/services')
def services():
    return 'Welcome To my services page'

@app.route('/about')
def about():
    return 'Welcome To my about page'

# run your app
if __name__ == '__main__':

    app.run()
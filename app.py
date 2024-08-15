from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates/about.html')
def about():
    return render_template('about.html')

@app.route('/templates/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

@app.route('/templates/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/templates/features.html')
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run(debug=True)
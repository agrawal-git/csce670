from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', name="this is the main page")

@app.route('/search/')
def search():
  return "this is the search page"

if __name__ == '__main__':
    app.run(debug=True)

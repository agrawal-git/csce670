from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'This is the main file'

@app.route('/search/')
def search():
  return "this is the search page"

if __name__ == '__main__':
    app.run(debug=True)

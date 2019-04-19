from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {'pagetitle':'Odds and Exabytes', 'pagename':'Index'}
    return render_template("index.html", **context)

@app.route('/blog')
def blog():
    context = {'pagetitle':'Odds and Exabytes', 'pagename':'Blog', 'post_id':1}
    return render_template("blog.html", **context)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

from flask import render_template, Flask, url_for, send_file
import serverless_wsgi

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    print(url_for('index'))
    return render_template("index.html")

def lambda_handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

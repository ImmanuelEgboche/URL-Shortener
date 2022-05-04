from flask import render_template, request, Flask
import pyshorteners
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

#form on the frontend 
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        target_url = request.form['url']
        # use templating to return result
        shorter = pyshorteners.Shortener()
        small_url = shorter.tinyurl.short(target_url)
        print(small_url)
        return render_template('home.html', result=small_url)
    else:
        return render_template('home.html')
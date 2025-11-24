from flask import Flask , request , render_template
from datetime import datetime
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
current_weekday = datetime.now().weekday()

client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = client.test
collection = db['flask-tutorial']


@app.route('/')
def home():
    current_day_name = datetime.now().strftime('%A')
     current_date = datetime.now().strftime('%Y-%m-%d') 
    current_time = datetime.now().strftime('%M:%M:%S')
    return render_template('index.html',current_day_name=current_day_name,current_time=current_time)

@app.route('/submit' , methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)
        collection.insert_one(form_data)
        return render_template('success-page.html')
    except Exception as e:
        return str(e)

app.run(debug=True)
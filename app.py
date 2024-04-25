from flask import Flask, render_template, request, url_for, redirect 
from pymongo import MongoClient

from bson.objectid import ObjectId

app = Flask(__name__)

connection_string = 'mongodb+srv://Cluster76087:dl50TE9kc19U@Cluster76087.iovpglg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster76087'

client = MongoClient(connection_string)

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index')) 
    
    all_todos = todos.find()    
    return render_template('index.html', todos = all_todos) 

@app.route("/<id>/delete/", methods=('GET', 'POST'))
def delete(id): 
    todos.delete_one({"_id":ObjectId(id)}) 
    return redirect(url_for('index')) 

db = client.flask_database
todos = db.todos 

if __name__ == "__main__":
    app.run(debug=True) 
from flask import Flask, render_template, jsonify, request

import sqlite3
conn = sqlite3.connect('mydictionary.db', check_same_thread=False)
c = conn.cursor()
app = Flask(__name__)



@app.route("/details",methods=['GET','POST'])
def details():
    if request.method=='POST':
        text = request.form['word'].lower()
        search_word = c.execute("SELECT * FROM dictionary_tb where word='%s'" % text)
        words = search_word.fetchall()
        if words:
            return render_template('details.html', rows=words)
        else:
            return "Missing input",400

    else:
        return "Invalid Request",500
@app.route("/",methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/about",methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/get/<string:search_word>",methods=['GET','POST'])
def get(search_word):
    cor = c.execute("SELECT * FROM dictionary_tb where word LIKE '"+search_word+"%'")
    datas = cor.fetchall()
    all_word_dict=[]
    for data in datas:
        one_word_dict={
            'word':data[0],
            'mean':data[1],

        }
        all_word_dict.append(one_word_dict)
    return jsonify({'result': all_word_dict})


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

import os

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/index")
def index() :
    return render_template('index.html')

@app.route('/get_column_name_change', methods=['POST'])
def column_name_change() :
    bef_column_name = request.forn.get('before_column_name')
    aft_column_name = request.form.get('after_column_name')

    print(bef_column_name)
    print(aft_column_name)

    return render_template('index.html')

@app.route('/get_image_pre_status', methods=['POST'])
def image_preprocessing() :
    if request.method == 'POST' :
        print("0=", request.form.get('pre_toggle_0'))
        print("1=", request.form.get('pre_toggle_1'))
        print("2=", request.form.get('pre_toggle_2'))

    return render_template('index.html')

@app.route('/get_selected_table', methods=["POST"])
def selected_table() :
    text = request.form.get('table_name')
    print(text)
    
    return render_template('index.html')

@app.route('/get_selected_table2', methods=["POST"])
def select_table2() :
    text = request.form.get('textbox')

    return render_template('index.html', label=text)

@app.route('/upload_image', methods=["POST"])
def upload_image_file() :
    if request.method == 'POST' :
        file = request.files['uploaded_image']
        if not file : 
            return render+template('index.html', label = "No Files")
        label = file

        return render_template('index.html', label = label)

if __name__ == '__main__' :
    app.run()


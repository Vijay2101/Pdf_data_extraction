from application import app
from flask import render_template, request, jsonify, redirect, send_file
import os
from application import result 
from application import result2 
import json
from io import BytesIO

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    selected_format = request.form['format']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Process the file in memory
        file_stream = BytesIO(file.read())
        
        try:
            # Assuming `result` and `result2` are functions that accept file-like objects
            if selected_format == 'format1':
                res = result.format1(file_stream)
            else:
                res = result2.format2(file_stream)
            
            return render_template('result.html', json_data=json.dumps(res), result='result')
        except Exception as e:
            return f'Error processing file: {str(e)}'
    
    return 'Invalid file format'











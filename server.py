import sys
import os
import json
from flask import Flask, request, jsonify

with open('data.json') as file:
 	mapping_data = json.load(file)
print mapping_data

app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload_qrcode():
	data = request.json
	print data['id']
	output = data['id']
	print output

	return mapping_data[output]
		
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=9090,debug=True)
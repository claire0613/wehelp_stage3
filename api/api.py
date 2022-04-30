from flask import Flask, request, jsonify,Blueprint
import logging
import boto3
from database import insert_upload_data, search_upload_data,allowed_file
from env import *
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os
from datetime import datetime
load_dotenv()

api = Blueprint('api', __name__)


@api.route('/upload', methods=['POST'])
def post_upload(): 
	try:
		message = request.form['message']
		image= request.files['file'] #接收檔案
		record=datetime.now().strftime('%Y%m%d%H%M%S%f')
		
		if image and allowed_file(image.filename):
			image.filename = secure_filename(image.filename)
			image_filename=record+image.filename
			image_url=os.getenv("CDN_URL")+image_filename
			
			# print('留言', message)
			# print('圖檔', picture)
			# print('圖檔名稱',picture.filename)
			s3 = boto3.client('s3', 
			aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
			aws_secret_access_key=os.getenv("S3_SECRET_KEY")
			)
			
			s3.upload_fileobj(image,os.getenv("S3_BUCKET"),image_filename)
			insert_upload_data(message = message, image_url = image_url)
			return jsonify({'data':True})
			
       

		else:
			return jsonify({"error": True, "message": "S3 upload failed "})


	except Exception as e:
		logging.error(e)
		return jsonify({ "error": True, "message": "伺服器內部錯誤" })

@api.route('/upload',methods=['GET'])
def get_upload():
	try:
		check_message=search_upload_data()
		if check_message:
			return jsonify({'data':check_message})

	except:
		return {"error": True, "message": "伺服器內部錯誤"}, 500
		
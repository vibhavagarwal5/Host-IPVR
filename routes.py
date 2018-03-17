import os, json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify,flash
from watson_developer_cloud import VisualRecognitionV3
from werkzeug import secure_filename
import urllib

# Initialize the Flask application
app = Flask(__name__)
visual_recognition = VisualRecognitionV3('2018-03-16', api_key = 'df264a51547839277a3c59d672c1593def3009a1')

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('static', 'img_uploads'))

def getInfo(data):
	content = []
	file_name = data['images'][0]['image']
	content.append(file_name)
	try:
		class1 = data['images'][0]['classifiers'][0]['classes'][0]['class']
		score1 = data['images'][0]['classifiers'][0]['classes'][0]['score']
		content.append((class1, score1))
	except:
		pass
	return content

def save_image(latitude, longitude, pitch = -30, heading = 0):
	filename = str(latitude) + "_" + str(longitude) + "_"+ str(pitch)+ "_" + str(heading)+".jpg"
	f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb')
	f.write(urllib.urlopen('https://maps.googleapis.com/maps/api/streetview?size=600x300&location='+str(latitude)+','+str(longitude)+'&heading='+str(heading)+'&pitch='+str(pitch)+'&key=AIzaSyDAg6VivTbhqj7tuS85rg1fpI1iqoOFWcU').read())
	f.close()
	return filename

# This route will show a form to perform an AJAX request jQuery is loaded to execute the request and update the
# value of the operation and that will process the file upload
@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('another.html',result=None)

@app.route('/upload', methods = ['GET', 'POST'])
def uploader():
	# Download the image into the correct folder for analysis
	latitude = request.form['latitude']
	longitude = request.form['longitude']
	pitch = int(request.form['pitch'])
	heading = int(request.form['heading'])
	filename = save_image(latitude, longitude, pitch, heading)

	with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as image_file:
		info = visual_recognition.classify(images_file = image_file, classifier_ids = 'Potholedetector_995527067', threshold = 0.23)
		data = getInfo(info)
		try:
			image_data={'file_name':filename,'class':data[1][0],'score':str(data[1][1])}
		except:
			image_data={'file_name':filename,'class':"Not pothole",'score':"0"}
		image_data = json.dumps(image_data)
		image_data = json.loads(image_data)
		return render_template('another.html',result=image_data)

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host = "0.0.0.0", port = port)

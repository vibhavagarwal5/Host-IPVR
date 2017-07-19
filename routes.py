import os, json
# We'll render HTML templates and access data sent by POST using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify,flash
from watson_developer_cloud import VisualRecognitionV3
from werkzeug import secure_filename

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

# Initialize the Flask application
app = Flask(__name__)
visual_recognition = VisualRecognitionV3('2017-07-01', api_key = 'f2fbfa38ca877dadbbaf9e8e3d04ac9dff33ccc5')

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/img_uploads/')
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request jQuery is loaded to execute the request and update the
# value of the operation and that will process the file upload
@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('another.html',result=None)

@app.route('/upload', methods = ['GET', 'POST'])
def uploader():
		# Get the name of the uploaded file
		file = request.files['file']
		# Check if the file is one of the allowed types/extensions
		if file and allowed_file(file.filename):
			# Make the filename safe, remove unsupported chars
			filename = secure_filename(file.filename)
			# Move the file form the temporal folder to the upload folder we setup
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as image_file:
				info = visual_recognition.classify(images_file = image_file, classifier_ids = 'pothole_967824303', threshold = 0.25)
				data = getInfo(info)
				try:
					image_data={'file_name':filename,'class':data[1][0],'score':str(data[1][1])}
				except:
					image_data={'file_name':filename,'class':"Not pothole",'score':"0"}
				image_data = json.dumps(image_data)
				image_data = json.loads(image_data)
				return render_template('another.html',result=image_data)
		elif not file:
			return render_template('another.html',result="no file")
		elif not allowed_file(file.filename):
			return render_template('another.html',result="wrong ext")

if __name__ == '__main__':
	app.run(
		port=5000,
		debug = True)

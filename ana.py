from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return "Welcome to the Oracle web app with python in DevSecOPs this is change new  !! Modified modified2 Modified3 Modified4 Modified5"


if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5000, debug = True) 

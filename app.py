from flask import Flask , jsonify,render_template
from flask_restful import Resource , Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import Constant


app = Flask(__name__)
CORS(app)
api = Api(app)
auth = HTTPBasicAuth()

PREFIX = "/api/v1/"


@auth.verify_password
def verify(username , password):
    if not (username and password):
        return False
    return Constant.SECRET_DATA.get(username) == password

@app.route('/')
def index():
    return render_template('index.html')


@app.route(PREFIX+'/test' , methods=['GET'])
@auth.login_required
def get_test_response():
    return jsonify("Successful response")

if  __name__ == '__main__':  
     app.run(debug=True)




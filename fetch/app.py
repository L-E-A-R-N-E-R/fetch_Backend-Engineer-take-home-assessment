from flask import Flask, request, jsonify
import uuid,json
from utils import *

app = Flask(__name__)
dict = {}

@app.route('/receipts/<id>/points',methods = ['GET'])
def show_points(id):

    if request.method == 'GET':

        if(isinstance(id,str) and re.match("^\\S+$",id) and (id in dict)):
            result = dict[id]
        else:
            return "404: No receipt found for that id"

        return jsonify({"points":result})
    
    else:
        return "Err! For this path, select GET method and enter the receipt id in the path to get points"

@app.route('/receipts/process',methods=['GET','POST'])
def generate_id():

    if request.method == "POST":

        points = 0

        data = request.json
        
        if('retailer' in data and 'purchaseDate' in data and 'purchaseTime' in data and 'items' in data and 'total' in data):

            try:
                points = points + rule1(data,points) + rule2_and_rule3(data,points) + rule4_and_rule5(data,points) + rule6(data,points) + rule7(data,points)
            except:
                return "400: The receipt is invalid"

            unique_id = str(uuid.uuid4())
            dict[unique_id] = points

            return jsonify({"Receipt id":unique_id})
        
        else:
            return "400: The receipt is invalid"
    
    else:
        return "Err! For this path, select POST method and submit a receipt (JSON payload) to generate a receipt id"

if __name__=="__main__":
    app.run(debug=True)
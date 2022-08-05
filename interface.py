import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import MedicalInsurence

app = Flask(__name__)

##########################################################################
########################## Login API ######################################
##########################################################################

@app.route('/') 
def hello_flask():
    print("Welcome to Flask")
    return render_template('login.html')

@app.route('/result/<name>')
def result(name):
    return f"Hello {name}"

@app.route('/login',methods = ['POST','GET'])
def login():
    print("HELLO")
    if request.method == 'POST':
        data = request.form
        name = data['name']
        print("Name ::::",name)
        return redirect(url_for('result',name = name))

    if request.method == 'GET':
        name = request.args.get('name')
        print("Name ::::",name)
        return redirect(url_for('result',name = name))

#########################################################################
#########################################################################
#########################################################################

@app.route('/predict_charges',methods = ['POST','GET'])
def get_insurence_charges():
    if request.method == 'POST':
        print("We are using POST method")
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']

        print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
        med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
        charges = med_ins.get_predicted_charges()

        return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})

    else:
        print("We are using GET method")
        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')

        print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
        med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
        charges = med_ins.get_predicted_charges()

        return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})
 
@app.route('/testing/<student_name>')
def testing1(student_name):
    return f"Hello {student_name}"

@app.route('/marks/<float:score>')
def marks(score):
    print(type (score))
    return f"Score is : {score}"

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)

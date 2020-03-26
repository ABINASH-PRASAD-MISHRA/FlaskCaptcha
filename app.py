from flask import Flask,render_template,render_template_string
import os
import random
from captcha.image import ImageCaptcha
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcvsuMUAAAAAAJN0bxwZm_C8FYLiEjSC4rnW576' 
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcvsuMUAAAAAEqgsBpJ2ICbYSi9fm-ncO6Lv87j' 


class LoginForm(FlaskForm): 
    username= StringField('username',validators=[InputRequired('A username is required')])
    password= PasswordField('password',validators=[InputRequired('A password is required')])
    recaptcha = RecaptchaField()

@app.route("/form" , methods= ['POST','GET'])
def cap_img():
    form=LoginForm()
    
    if form.validate_on_submit():
        return "Form Submitted !!!"
        #html = '''<html> <head> </head> <body> <h1> Form Submitted !!! </h1> <form method='POST' action='/form'> <input type='Submit' name = 'resumbit'> </form> </body> </html> '''
    return render_template('form.html',form=form)

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True,host='0.0.0.0', port=5000)
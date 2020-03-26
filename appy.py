from flask import Flask,render_template,render_template_string
import os
import random
from captcha.image import ImageCaptcha
image_captcha = ImageCaptcha()
from io import BytesIO
import base64

number_list = ['0','1','2','3','4','5','6','7','8','9']

alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def create_random_captcha_text(captcha_string_size=6):

    captcha_string_list = []

    base_char = alphabet_lowercase + alphabet_uppercase + number_list

    for i in range(captcha_string_size):

        # Select one character randomly.
        char = random.choice(base_char)

        # Append the character to the list.
        captcha_string_list.append(char)

    captcha_string = ''

    # Change the character list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

def captchaimage():
    string = create_random_captcha_text()
    image = image_captcha.generate_image(string)
    #image2 = image_captcha.create_noise_dots(image,color="blue")
    print(string)
    return string,image

app = Flask(__name__,static_url_path = "/static", static_folder = "static")

@app.route("/",methods=['GET','POST'])
def cap_img():
    st,img = captchaimage()
    img_save= img.save("F:/bot/captcha/static/captcha.png")
    #img_path = r"F:\bot\captcha"
    #image = os.path.join('F:\\bot\captcha\static\"+"captcha.jpg');
    #path = "/captcha.jpg"
    #print(path)
    #old {{ url_for('static',filename='captcha.jpg') }}
    #new "static/images/{{ employee.profile_image }}" "static/{{captcha}}" ,captcha='captcha.jpg'

    figfile = BytesIO()
    img.save(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    html= '''<html> <head> 

</head> 

<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=password], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}
input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
  width:500;
  position:relative;
  left:500;
}
</style>

<body> 

<div name="formdiv" align="center" > 
<form method="POST" align="center">
    <label for="login">Login/Username</label> <input type="text" name="login"> <br> <br>
    <label for="password">Password</label> <input type="password" name="password"> <br> <br> 

    {% if result != None %}
    <img src="data:image/png;base64,{{ result }}" width="100" height='45' align="center"> <br> <br>
    {% endif %}
    <label for="captcha">Enter text as shown in image: </label> 
    <input type="text" name="captcha">
    <input type="submit">
</form> </div> </body> </html>'''
        
    return render_template_string(html,result=result)

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True)
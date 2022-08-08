from flask import Flask, render_template,request
from flask_mail import Mail, Message
from random import randint

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 456
app.config["MAIL_USERNAME"] = 'vidhanpython@gmail.com'
app.config["MAIL_PASSWORD"] = 'Vidhan@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)
otp = randint(100000, 999999)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/verify', methods=["POST", "GET"])
def verify():
    email = request.form.get('email')
    msg = Message(subject="OTP Verification for ATM", sender='vidhanpython@gmail.com', recipients=[email])
    msg.body = "OTP is 123456"
    mail.send(msg)
    return render_template('verify.html')


@app.route('/validate', methods=["POST", "GET"])
def validate():
    user_otp = request.form.get('otp')
    if otp == int(user_otp):
        return "Email Verified"

    return "Wrong OPT Try Again"


if __name__ == '__main__':
    app.run(debug = True)


from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/signup", methods=['POST'])
def user_signup():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    username_error = ''
    if (not username) or username.strip() == "" or len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username."       

    
    password_error = ''    
    if (not password) or password.strip() == "" or len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password."


    verify_password_error = ''
    if verify_password != password or verify_password == '':
        verify_password_error = "Password don't match."
        verify_password = ''


    email_error = ''    
    if (email):
        if len(email) < 3 or len(email) > 20 or '@' not in email or '.' not in email or ' ' in email:
            email_error = "That's not valid email."

    
    if username_error or password_error or verify_password_error or email_error :
        return render_template('edit.html', username_error=username_error, password_error=password_error, 
            verify_password_error=verify_password_error, email_error=email_error, username=username, email=email)
    else:       
        return render_template('welcome.html', username=username)
    
    

@app.route("/")
def index():
    return render_template('edit.html')
    

app.run()
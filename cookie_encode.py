from flask import Flask, url_for, render_template, abort, send_file, request, redirect, session, make_response
inputed_key = input("Flask session key:")
inputed_ckey= input("Cookie key: ")
inputed_val = input("Cookie value: ")
print("Encoding...")
app = Flask(__name__)
app.secret_key = inputed_key

@app.route('/')
def index():
    resp = make_response(redirect(url_for("test")))
    session[inputed_ckey] = inputed_val
    
    return resp
    
    
@app.route('/test')
def test():

    resp = make_response(render_template("test.html",  sessionc=request.cookies.get('session')))
    
    return resp
    

app.run(port=8080)

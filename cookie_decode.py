from flask import Flask, url_for, render_template, abort, send_file, request, redirect, session, make_response
inputed_key = input("Flask session key:")
session_cont = input("Cookie to decode: ")
print("Decoding...")
app = Flask(__name__)
app.secret_key = inputed_key

@app.route('/')
def index():
    resp = make_response(redirect(url_for("test")))
    resp.set_cookie('session', session_cont)
    
    return resp
    
    
@app.route('/test')
def test():
    resp = make_response(render_template("test.html",  sessionc=session))
    
    return resp
    
app.run(port=8080)

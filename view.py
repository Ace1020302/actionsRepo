from flask import Flask
from flask import render_template, make_response
from markupsafe import escape
from flask import request
from collections import defaultdict
import os

dic = defaultdict(dict)

app = Flask(__name__)

times = [x/2 for x in range(8+1)]

@app.route("/")
@app.route("/<name>")
def hello_world(name=None):
    return render_template("hello.html", person=name)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login( request.form['username'], request.form['password'] ):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = "Invalid user/pass"
#         return render_template('login.html', error=error);

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/gfg', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       full_name = first_name + " " + last_name
       return (render_template("login.html") + render_template("hello.html", person=full_name))
    return render_template("login.html")

@app.route('/buttons', methods=["GET", "POST"])
def buttons():
    output = render_template("buttons.html", times=times, linkcode=request.cookies.get("code"), name=request.cookies.get("name"))  
    return output

@app.route('/cookies')
def getCookies():
    text = request.cookies.get("user")
    return text
    
    
    
@app.route('/submit', methods=["GET", "POST"])
def submit():
    name = request.form.get("name")
    linkcode = request.form.get("code")
    # link code is right
    time = request.form.get("time")
    dic[linkcode][name] = time
    
    output = (render_template("buttons.html", times=times, linkcode=request.cookies.get("code"), name=request.cookies.get("name")))
    
    resp = make_response(output)
    resp.set_cookie("code", value=linkcode, domain='127.0.0.1')
    resp.set_cookie("name", value=name, domain='127.0.0.1')
    # resp needs to be returned to be cookied
    return resp


@app.route('/displaySubmissions')
def displaySubmissions():
    code = request.cookies.get("code")
    print("------------")
    # print(f"{dic}")
    print("------------")
    # print(request.cookies.get("code"))
    output = buttons()
    output += """<div id="people">"""
    for name in dic[code]:
        print(name)
        output += render_template("people.html", name=name, time=dic[code][name])
    print("------------")
    output += """</div>"""
    return output

    
@app.route('/clearEstimates')
def clearEstimates():
    code = request.cookies.get("code")
    print("------------")
    # print(f"{dic}")
    print("------------")
    # print(request.cookies.get("code"))
    
    for name in dic[code]:
        dic[code][name] = None
    print("------------")
    output = displaySubmissions()
    return output

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
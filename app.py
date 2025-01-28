from flask import Flask,redirect,url_for,request,session,flash,render_template
app=Flask(__name__)
app.secret_key="secret_key"
users={}
@app.route("/")
def home():
    return redirect(url_for("login"))
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        if username in users and users["username"=="password"]:
            session['username']=username
            return redirect(url_for("homescreen"))
        else:
            flash("invalid username","error")
    return render_template('login.html')  
@app.route("/register",methods=['GET','POST']) 
def register():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        if username in users:
            flash("you already have an account","error")
        else:
            users[username]=password
            flash("registered successfully","success")
            return redirect( url_for("login"))
        
    return render_template('register.html')
@app.route("/homescreen")
def homescreen():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("home.html",username=session["username"])

if __name__=="__main__":
    app.run(debug=True)




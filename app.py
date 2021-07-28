from flask import Flask , render_template , request
app = Flask(__name__)
import pickle
model=pickle.load(open('pricenew1.pkl','rb'))
@app.route('/') # bind to an url 
def helloworld():
    return render_template("demo1.html")
@app.route('/login2')#url
def user():
    return render_template("pro.html")
@app.route('/login3',methods = ['POST']) # bind to an url 
def admin():
    from datetime import datetime
    date_time_str = request.form["preddate"]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    #print ("The type of the date is now",  type(date_time_obj))
    #print ("The date is", date_time_obj)
    year_inp=date_time_obj.year
    month_inp=date_time_obj.month
    day_inp=date_time_obj.day
    t=[[int(day_inp),int(month_inp),int(year_inp)]]
    y=model.predict(t)
    return render_template("pro.html", y ="The Price of Natural Gas on "+date_time_str+" would be "+str(y[0])+" Dollars per Million BTU")


if __name__ == '__main__' :
    app.run(debug = True)
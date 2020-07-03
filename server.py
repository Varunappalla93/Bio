import csv
from flask import Flask,render_template,request,redirect
app = Flask(__name__)
print(__name__)


# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None,post_id=None):
#     return render_template('index.html',name=username,pid=post_id)

#for dynamic page options by single function
@app.route('/<string:page_name>')
def htmlpage(page_name):
	return render_template(page_name)


def writetofile(data):
	with open('database.txt',mode='a') as db:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		
		dt=db.write(f'\n{email},{subject},{message}')


# def writetocsv(data):
# 	with open('db.csv',mode='a') as db2:
# 		email= data["email"]
# 		subject= data["subject"]
# 		message= data["message"]
# 		csv_writ=csv.writer(db2,delimiter='',quotechar='#',quoting=csv.QUOTE_MINIMAL)
# 		csv_writ.writerow([email,subject,message])



@app.route('/submit', methods=['POST', 'GET'])
def submitform():
	if request.method=="POST":
		try:
			data=request.form.to_dict()
			writetofile(data)
			return redirect('/Thank you.html')
		except:
			return 'did not save to database'
	else:
		return 'not correct'   



# @app.route('/index.html')
# def myhome():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/work.html')
# def work():
# 	return render_template('work.html')


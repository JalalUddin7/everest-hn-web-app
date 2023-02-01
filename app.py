from datetime import datetime
import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   referral_id = request.args.get("referral_id")

   # TODO - 
   # Lookup referral_id in the SQL DATABASE (basically, page shouldn't accept referral ID 1 if referral ID 1 does not exist.)
   # python library sql, jdbc connection, all that jazz.  
  
   # If it exists
   print('Request for index page received')
   return render_template('index.html', referral_id = referral_id)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/dobchecker', methods=['POST'])
def dobchecker():
   dob = request.form.get('dob')
   referral_id = request.form.get('referral_id')
   # TODO - 
   #  Check dob entered, with dob from referral_id SQL record

   if dob:
       print('Request for hello page received with name=%s' % dob)
       return render_template('dobchecker.html', name = dob, referral_id = referral_id) 
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('thankyou'))



@app.route('/thankyou')
def thankyou():
   # If it exists
   print('Request for index page received')
   return render_template('thankyou.html')


if __name__ == '__main__':
   app.run()
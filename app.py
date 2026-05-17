from flask import Flask, request, render_template
import database
from celery_worker import save_user

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def main_post():
    #database.connect_to_db()
    if request.method == 'POST':
        print("hello")
        fn = request.form['fn']
        ln = request.form['ln']
        #database.input_name(fn,ln)
        #database.discon()
        save_user.delay(fn,ln)
        return "taks queued"
    return render_template("main.html")

if __name__ == '__main__':
    app.run()
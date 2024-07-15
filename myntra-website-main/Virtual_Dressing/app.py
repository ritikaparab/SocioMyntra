#run app.py server before viewing the virtual room in the html 


from flask import Flask, render_template, Response, redirect, url_for
import vdress, vdress1, vdress2, vdress3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('virindex.html')

@app.route('/run-vdress')
def run_vdress():
   return Response(vdress.run(), mimetype='text/plain')

@app.route('/run-vdress1')
def run_vdress1():
   return Response(vdress1.run(), mimetype='text/plain')

@app.route('/run-vdress2')
def run_vdress2():
    return Response(vdress2.run(), mimetype='text/plain')

@app.route('/run-vdress3')
def run_vdress3():
    return Response(vdress3.run(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)

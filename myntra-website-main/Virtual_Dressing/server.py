from flask import Flask, request
import subprocess

app = Flask(__name__)

# Route to run script 1
@app.route('/run_script1', methods=['GET'])
def run_script1():
    result = subprocess.run(['python', 'vdress.py'], capture_output=True, text=True)
    return result.stdout

# Route to run script 2
@app.route('/run_script2', methods=['GET'])
def run_script2():
    result = subprocess.run(['python', 'vdress1.py'], capture_output=True, text=True)
    return result.stdout

# Route to run script 3
@app.route('/run_script3', methods=['GET'])
def run_script3():
    result = subprocess.run(['python', 'vdress3.py'], capture_output=True, text=True)
    return result.stdout

# Route to run script 4
@app.route('/run_script4', methods=['GET'])
def run_script4():
    result = subprocess.run(['python', 'vdress2.py'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)

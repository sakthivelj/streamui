import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run()

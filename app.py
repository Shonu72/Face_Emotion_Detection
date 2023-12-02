from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_script', methods=['GET'])
def run_python_script():
    try:
        # Run your Python script using subprocess
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        output = result.stdout
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

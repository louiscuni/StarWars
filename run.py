from flask import Flask, jsonify, render_template, request
import json
import ast
from pathlib import Path
import services.src.controller.controller as ctrl


def get_path():
    p = Path.cwd()
    p = p.parent.parent / 'front' / 'templates' 
    return str(p)

path_template = get_path()
app = Flask(__name__)

@app.route('/back_end')
def moteur():
    data = request.args.get('data', type=str)
    data = ast.literal_eval(data)
    res, path = ctrl.main(data)
    return jsonify(result=[res, path])


@app.route('/')
def index():
    return render_template('C3PO_front.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

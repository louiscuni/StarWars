from flask import Flask, jsonify, render_template, request
import json
import ast
from pathlib import Path
import src.controller.controller as ctrl


def get_path():
    p = Path.cwd()
    #app.logger.info(p)
    p = p.parent.parent / 'front' / 'templates' 
    return str(p)

path_template = get_path()

app = Flask(__name__, static_url_path='', template_folder=path_template)

@app.route('/machine_a_laver')
def moteur():
    data = request.args.get('data', type=str)
    data = ast.literal_eval(data)
    res = ctrl.main(data)
    return jsonify(result=res)

@app.route('/')
def index():
    #url = url_for('static', filename='s.js')
    return render_template('C3PO_front.html')
    #return json.dumps(plop())

if __name__ == '__main__':
    #b = single_bridge('b')#don't know if i can do that
    app.run(host='127.0.0.1', port=5001, debug=True)

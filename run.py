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
#static_url_path='/templates/static', template_folder=path_template
app = Flask(__name__)

@app.route('/machine_a_laver')
def moteur():
    data = request.args.get('data', type=str)
    data = ast.literal_eval(data)
    res, path = ctrl.main(data)
    return jsonify(result=[res, path])


@app.route('/')
def index():
    #app.logger.info(app.template_folder)
    #url = url_for('static', filename='s.js')
    return render_template('C3PO_front.html')
    #return json.dumps(plop())

if __name__ == '__main__':
    #b = single_bridge('b')#don't know if i can do that
    app.run(host='127.0.0.1', port=5001, debug=True)

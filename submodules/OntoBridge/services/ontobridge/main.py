from utils.config_utils import HOME, INDEX, TRANSFORMATION_SUCCES, ONTOP_MATERIALIZE, EXECUTE_CHOSEN_MODEL
from flask import Flask, render_template, request
from flask_cors import CORS
from utils.RDB2RDF_utils import execute_ontop_materialize, create_properties_file
from app import execute_chosen_model

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route(HOME, methods=['GET',])
def index():
    return render_template(INDEX)

@app.route(ONTOP_MATERIALIZE, methods=['GET','POST'])
def run_execute_ontop_materialize():
        if request.method == 'POST':
            jdbc_name = request.form['jdbc_name']
            jdbc_url = request.form['jdbc_url']
            jdbc_user = request.form['jdbc_user']
            jdbc_password = request.form['jdbc_password']

            create_properties_file(jdbc_name, jdbc_url, jdbc_user, jdbc_password)
            execute_ontop_materialize()
            return render_template(INDEX, success=True)

        return render_template(INDEX)

@app.route(EXECUTE_CHOSEN_MODEL, methods=['POST'])
def create_final_tables():
    chosen_model = request.form['chosen_model']
    execute_chosen_model(chosen_model)
    return render_template(TRANSFORMATION_SUCCES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('adhoc'))

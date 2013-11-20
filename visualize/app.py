import os

from collections import defaultdict

from flask import Flask
from flask import json
from flask import request
from flask import render_template

app = Flask(__name__)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.join(PROJECT_DIR, '../results')


@app.route('/result')
def visualise_file():
    versions = request.args.getlist('version') or ['1.4.10', '1.5.5', '1.6']
    db_vendors = request.args.getlist('vendor') or [
        'postgresql', 'mysql', 'sqlite']
    app_names = request.args.getlist('app_name') or [
        'polymorphic_test', 'model_utils_test', 'generic_m2m']

    fn_tmpl = '{app_name}_{db_vendor}_Django-{version}_benchmark_results.csv'

    grouped_data = defaultdict(list)
    for app_name in app_names:
        for version in versions:
            for db_vendor in db_vendors:
                name = '{}_{}_{}'.format(app_name, version, db_vendor)
                filename = fn_tmpl.format(
                    app_name=app_name, db_vendor=db_vendor, version=version)
                path = os.path.join(RESULTS_DIR, filename)
                if not os.path.exists(path):
                    continue
                with open(path) as fh:
                    for line in fh:
                        try:
                            line = json.loads(line)
                            grouped_data[name].append(line)
                        except:
                            pass
    return json.dumps(grouped_data)


@app.route('/')
def index():
    return render_template(
        'visualise_file.html', parsecom_app_id=os.getenv('PARSECOM_APP_ID'),
        parsecom_js_key=os.getenv('PARSECOM_JAVASCRIPT_KEY'))


if __name__ == '__main__':
    app.run(debug=True)

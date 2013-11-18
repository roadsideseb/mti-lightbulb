import os

from collections import defaultdict

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/result')
def visualise_file():
    versions = request.args.getlist('version') or ['1.4.10', '1.5.5', '1.6']
    db_vendors = request.args.getlist('vendor') or [
        'postgresql', 'mysql', 'sqlite']
    app_names = request.args.getlist('app_name') or [
        'polymorphic_test', 'model_utils_test', 'generic_m2m']
    metric = request.args.get('metric', 'query_time_sql')

    fn_tmpl = '{app_name}_{db_vendor}_Django-{version}_benchmark_results.csv'

    base_dir = os.path.join(os.getcwd(), '../results')
    grouped_data = defaultdict(list)
    for app_name in app_names:
        for version in versions:
            for db_vendor in db_vendors:
                name = '{}_{}_{}'.format(app_name, version, db_vendor)
                filename = fn_tmpl.format(
                    app_name=app_name, db_vendor=db_vendor, version=version)
                path = os.path.join(base_dir, filename)
                if not os.path.exists(path):
                    continue
                with open(path) as fh:
                    for line in fh:
                        grouped_data[name].append(line)
    return render_template('visualise_file.html', grouped_data=grouped_data,
                           metric=metric)


@app.route('/')
def index():
    base_dir = os.path.join(os.getcwd(), '../results')
    files = []
    for filename in os.listdir(base_dir):
        if filename.endswith('.csv'):
            filename, __ = os.path.splitext(filename)
            files.append(filename)
    return render_template('index.html', filenames=files)


if __name__ == '__main__':
    app.run(debug=True)

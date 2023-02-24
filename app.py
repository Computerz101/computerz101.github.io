import os
from pathlib import Path
from flask_frozen import Freezer
from flask import Flask, Response, render_template, request, make_response

app = Flask(__name__)
freezer = Freezer(app)


@app.route('/')
def home():
    return Response(response=render_template('home.html'), mimetype='text/html', status=200)


@app.route('/services')
def services():
    return Response(response=render_template('services.html'), mimetype='text/html', status=200)


@app.route('/testimonials')
def testimonials():
    return Response(response=render_template('testimonials.html'), mimetype='text/html', status=200)


@app.route('/faq')
def faq():
    return Response(response=render_template('faq.html'), mimetype='text/html', status=200)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        template = render_template(
            'contact.html', name=name, email=email, message=message)
    else:
        template = render_template('contact.html')
    return Response(response=template, mimetype='text/html', status=200)


@app.cli.command('build')
def build_command():
    freezer.freeze()
    for file in Path('templates').glob('*.html'):
        file_name = file.stem
        for built_file in Path('build').glob('*'):
            if built_file.stem == file_name and built_file.suffix != '.html':
                with open(built_file, 'r') as f:
                    contents = f.read()
                contents = contents.replace('../static', 'static')
                built_file.rename(built_file.with_suffix('.html'))


if __name__ == '__main__':
    app.run(debug=True)

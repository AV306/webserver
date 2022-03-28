from flask import *;

app = Flask(__name__);

@app.route('/', methods=['GET'])
def on_index_get():
	if request.method != 'GET':
		abort( 405 ); # method not allowed
	else:
		return render_template( 'index.html' );

@app.route('/about', methods=['GET'])
def on_about_get():
	if request.method != 'GET':
		abort( 405 );
	else:
		return render_template( 'about.html' );

@app.route('/about/<name>', methods=['GET'])
def on_about_person_get( name ):
	if request.method != 'GET':
		abort( 405 );
	else:
		return render_template( f'about/{escape(name)}.html' );
	
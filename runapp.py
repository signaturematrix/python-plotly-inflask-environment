from dashflaskapp import app
from werkzeug.serving import run_simple

run_simple('0.0.0.0', 8080, app, use_reloader=True)
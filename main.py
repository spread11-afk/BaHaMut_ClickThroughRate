from flask import Flask,render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from dash_file.dash_app1 import dash1
# from dash_file.dash_app2 import dash2
from werkzeug.serving import run_simple

app = Flask(__name__)

# application = DispatcherMiddleware(
#     app,
#     {"/dash/app1": dash1.server,
#     "/dash/app2": dash2.server}
# )

@app.route("/")
def index():
    return render_template('2020.html')

# if __name__ == "__main__":
#     run_simple("localhost", 8080, application,use_debugger=True,use_reloader=True)
from flask import Flask, request
from models.task import db
from controllers.task_controller import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@172.17.0.1:3306/isbn'
db.init_app(app)

@app.before_request
def override_method():
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['PUT']:
            request.environ['REQUEST_METHOD'] = method

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
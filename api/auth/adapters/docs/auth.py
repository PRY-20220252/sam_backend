from flask_cors import cross_origin
from flask_restx import Namespace, fields

auth_namespace = Namespace('', description='Authentication operations', decorators=[cross_origin()])

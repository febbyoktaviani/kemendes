''' flask app with mongo '''
import os
import json
import datetime
from flask import Flask, request
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS
from mongoengine import connect
from .controller import *

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    # app.config.from_mapping(

    # )
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=10)
    jwt = JWTManager(app)
    connect(
        host = os.getenv('DATABASE')
    )
    print('database connected')
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    @app.route('/test', methods=['GET'])
    def home():
        return 'alive'


    @app.route('/register', methods=['POST'])
    def register():
        print(request.form)
        try:
            register = RegisterView(app)
            return register.post(request.form)
        except Exception as e:
            return e.__str__(), 500


    @app.route('/login', methods=['POST'])
    def login():
        try:
            login = LoginView(app)
            return login.post(request.form)
        except Exception as e:
            return e.__str__(), 500

    @app.route('/user')
    @jwt_required
    def user():
        try:
            login = LoginView(app)
            return login.get()
        except Exception as e:
            print(e)
            return e, 500

    @app.route('/berita', methods=['POST', 'GET'])
    @jwt_required
    def berita():
        berita = BeritaView(app)
        if request.method == 'POST':
            if 'image' in request.files:
                file = request.files['image']
            else:
                file = None
            try:
                return berita.post(request.form, file)
            except Exception as e:
                print(e)
                return e, 500
        elif request.method == 'GET':
            search_text = request.args.get('search')
            print(search_text)
            return berita.get(search_text)

    @app.route('/title-berita', methods=['GET'])
    def title_berita():
        berita = BeritaView(app)
        search_text = request.args.get('search')
        print(search_text)
        return berita.get_title(search_text)

    @app.route('/title-unitkerja', methods=['GET', 'POST'])
    def title_unit_kerja():
        unit_kerja = UnitKerjaView(app)
        if request.method == 'GET':
            search_text = request.args.get('search')
            print(search_text)
            return unit_kerja.get_title(search_text)
    
    @app.route('/unitkerja', methods=['GET', 'POST'])
    @jwt_required
    def unit_kerja(): 
        if request.method == 'POST':  
            if 'bagan' in request.files:
                    file = request.files['bagan']
            else:
                file = None
            try:
                return unit_kerja.post(request.form, file)
            except Exception as e:
                print(e)
                return e, 500

    @app.route('/rencana-kerja', methods=['GET', 'POST'])
    def rencana_kerja():
        rencana_kerja = RiskFormView(app)

        if request.method == 'GET':
            tujuan_id = request.args.get('tujuan_id')
            return json.dumps(rencana_kerja.get(tujuan_id))

        if request.method == 'POST':
            print('post', request.get_json())
            print('post', request.data.decode('utf8').replace("'", '"'))
            data = request.data.decode('utf8').replace("'", '"')
            # print(request.json['name'])
            result = rencana_kerja.post(data)
            print(result)
            return result
            


    return app
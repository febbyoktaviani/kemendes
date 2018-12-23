''' flask app with mongo '''
import base64
import os
import json
import datetime
from flask import Flask, flash, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS
from mongoengine import connect
from .controller import *


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=10)
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
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

    @app.route('/user/login', methods=['POST'])
    def login():
        try:
            login = LoginView(app)
            data = request.data.decode('utf8').replace("'", '"')
            print('login', data)
            return login.post(data)
        except Exception as e:
            print(e)
            return e.__str__(), 500

    @app.route('/post-user', methods=['POST'])
    @jwt_required
    def post_user():
        print(request.form)
        try:
            register = UserView(app)
            return register.post(request.form)
        except Exception as e:
            return e.__str__(), 500

    @app.route('/list-user', methods=['GET'])
    @jwt_required
    def list_user():
        try:
            search_text = request.args.get('search')
            list_user = UserListView(app)
            return list_user.get(search_text)
        except Exception as e:
            print(e)
            return e, 500

##################################################### BERITA #####################################
    # post berita
    @app.route('/post-berita', methods=['POST'])
    @jwt_required
    def post_berita():
        print('post-berita', request.files)
        berita = BeritaView(app)
        if 'image' in request.files:
            file = request.files['image']
        else:
            file = None
        try:
            return berita.post(request.form, file)
        except Exception as e:
            print(e)
            return e, 500

    # api get berita
    @app.route('/berita/<berita_id>', methods=['GET'])
    def berita(berita_id):
        berita = BeritaView(app)
        print(berita_id)
        return berita.get(berita_id)

    @app.route('/list-berita', methods=['GET'])
    # @jwt_required
    def list_berita():
        berita = BeritaListView(app)
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
        berita = BeritaListView(app)
        search_text = request.args.get('search')
        print(search_text)
        return berita.get_title(search_text)

##################################################### END API BERITA ###############################

############################################ API UNITKERA #########################################
    # api get unit kerja
    @app.route('/unitkerja/<unit_kerja_id>', methods=['GET'])
    def unitkerja(unit_kerja_id):
        unit_kerja = UnitKerjaView(app)
        return unit_kerja.get(unit_kerja_id)

    @app.route('/list-unitkerja', methods=['GET'])
    def list_unitkerja():
        unit_kerja = UnitKerjaListView(app)
        search_text = request.args.get('search')
        print(search_text)
        return unit_kerja.get(search_text)

    @app.route('/title-unitkerja', methods=['GET'])
    def title_unitkerja():
        unit_kerja = UnitKerjaListView(app)
        search_text = request.args.get('search')
        print(search_text)
        return unit_kerja.get_title(search_text)
    
    @app.route('/post-unitkerja', methods=['POST'])
    @jwt_required
    def post_unitkerja():
        unit_kerja = UnitKerjaView(app)
        if 'bagan' in request.files:
            file = request.files['bagan']
            print('file', file)
        else:
            file = None
        return unit_kerja.post(request.form, file)

########################################### END API UNITKERJA #####################################

    @app.route('/rencana-kerja', methods=['GET', 'POST'])
    @jwt_required
    def rencana_kerja():
        rencana_kerja = RiskFormView(app)

        if request.method == 'GET':
            tujuan_id = request.args.get('tujuan_id')
            return json.dumps(rencana_kerja.get(tujuan_id))

        if request.method == 'POST':
            data = request.data.decode('utf8').replace("'", '"')
            # print(request.json['name'])
            result = rencana_kerja.post(data)
            print(result)
            return result

    @app.route('/list-rencana-kerja', methods=['GET'])
    @jwt_required
    def rencana_kerja_list():
        rencana_kerja_list = RencanaKerjaListView(app)
        result = rencana_kerja_list.get()
        print('get', result)
        return json.dumps(result)
     
    return app
import json

from flask import jsonify
from mongoengine import DoesNotExist

from .constants import StatusCodes
from .model import *
from .helpers import *
from .services import create_berita, create_unit_kerja, get_rencana_kerja, update_rencana_kerja


class RegisterView(object):
    def __init__(self, app):
        self.app = app

    def post(self, user_data):
        username = user_data['username']
        password = user_data['password']
        email = user_data['email']

        if not username or not password or not email:
            return 'all field must be filled'
        
        password_hash = generate_password(self.app, user_data['password'])

        new_user = User(username=username, email=email, password=password_hash)
        new_user.save()
        return 'add user success'


class LoginView(object):
    def __init__(self, app):
        self.app = app

    def post(self, user_data):
        username = user_data['username']
        password = user_data['password']

        if not username or not password:
            return 'all field must be filled', StatusCodes.HTTP_404_BAD_REQUEST
        
        try:
            db_user = User.objects.get(username=username)
        except DoesNotExist:
            return 'username not found', StatusCodes.HTTP_404_NOT_FOUND
        
        if not check_password(self.app, db_user['password'], password):
            return 'wrong password', StatusCodes.HTTP_400_BAD_REQUEST

        return jsonify(access_token=create_token(username))

    def get(self):
        identity = authenticate_user()
        user = User.objects.get(username=identity)
        return jsonify({
            'username':user['username'],
            'email':user['email']
            })

class BeritaView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def post(self, data, file=None):
        try:
            if file:
                berita = create_berita(data, self.identity, file)
            else:
                berita = create_berita(data, self.identity, None)
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return 'success insert berita'

    def get(self, query_param=None):
        user = User.objects.get(username=self.identity)
        if query_param:
            beritas = Berita.objects.search_text(query_param).to_json()
        else:
            beritas = Berita.objects.to_json()
        return beritas

    def get_title(self, query_param=None):
        if query_param:
            beritas = Berita.objects.only('title').search_text(query_param).to_json()
        else:
            beritas = Berita.objects.only('title').to_json()
        return beritas


class UnitKerjaView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def post(self, data, file=None):
        try:
            if file:
                unit_kerja = create_unit_kerja(data, self.identity, file)
            else:
                unit_kerja = create_unit_kerja(data, self.identity, None)
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return 'success insert unit kerja'

    def get_title(self, query_param=None):
        if query_param:
            title_unit_kerja = UnitKerja.objects.only('name').search_text(query_param).to_json()
        else:
            title_unit_kerja = UnitKerja.objects.only('name').to_json()
        return title_unit_kerja


class RiskFormView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get(self, tujuan_id):
        try:
            result = get_rencana_kerja(tujuan_id)
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return result

    def post(self, data):
        data = json.loads(data)
        try:
            tujuan_id = update_rencana_kerja(data)
        except Exception as e:
            print(e)
            return {'status': 'failed'}, StatusCodes.HTTP_400_BAD_REQUEST
        return json.dumps({'status': 'success', 'tujuan_id': tujuan_id})



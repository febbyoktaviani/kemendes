import json
import os
import pdb

from flask import jsonify
from mongoengine import DoesNotExist

from .constants import StatusCodes
from .model import *
from .helpers import *
from .services import create_berita
from .services import create_unit_kerja
from .services import get_rencana_kerja
from .services import get_list_rencana_kerja
from .services import update_rencana_kerja


class UserView(object):
    def __init__(self, app):
        self.app = app

    def post(self, user_data):
        username = user_data.get('username')
        password = user_data.get('password')
        email = user_data['email']
        role_id = user_data['role']
        if not username or not password or not email:
            return 'all field must be filled', StatusCodes.HTTP_400_BAD_REQUEST

        password_hash = generate_password(self.app, user_data['password'])
        role = Role.objects.get(id=role_id)

        if user_data.get('id'):
            user = User.objects.get(id=user_data.get('id'))
            user.update(username=username, password=password, email=email, role=role)
        else:
            try:
                existed_username = User.objects.get(username=username)
            except DoesNotExist:
                existed_username = None
        
            if existed_username:
                return 'username already exist', StatusCodes.HTTP_400_BAD_REQUEST

            user = User(username=username, email=email, password=password_hash, role=role)
            user.save()
        
        return user.to_json()

    def get(self, user_id):
        user = User.objects.get(id=user_id).to_json()
        print('us', user)
        return user


class UserListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get(self, query_param):
        print('qp', query_param)
        if query_param:
            users = User.objects.search_text(query_param).to_json()
        else:
            users = User.objects.to_json()
        
        users = json.loads(users)
        for user in users:
            if user.get('role'):
                role = Role.objects.get(id=user.get('role')['$oid'])
                user['role']['name'] = role.name

        print(users)
        return json.dumps(users)


class LoginView(object):
    def __init__(self, app):
        self.app = app

    def post(self, user_data):
        user_data = json.loads(user_data)
        username = user_data.get('username')
        password = user_data.get('password')

        if not username or not password:
            return 'all field must be filled', StatusCodes.HTTP_404_BAD_REQUEST
        
        try:
            db_user = User.objects.get(username=username)
        except DoesNotExist:
            return 'username not found', StatusCodes.HTTP_404_NOT_FOUND
        
        if not check_password(self.app, db_user['password'], password):
            return 'wrong password', StatusCodes.HTTP_400_BAD_REQUEST

        result = {}
        result['username'] = db_user.username
        result['access_token'] = create_token(username)
        return jsonify(result)

    def get(self):
        identity = authenticate_user()
        user = User.objects.get(username=identity)
        return jsonify({
            'username':user['username'],
            'email':user['email']
            })


class BeritaListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get(self, query_param=None):
        # user = User.objects.get(username=self.identity)
        print(query_param)
        if query_param:
            beritas = Berita.objects.search_text(
                query_param).order_by('-updated_at').to_json()
        else:
            beritas = Berita.objects.order_by('-updated_at').to_json()
        print(beritas)
        return beritas

    def get_title(self, query_param=None):
        if query_param:
            beritas = Berita.objects.only('title').search_text(
                query_param).order_by('-updated_at').to_json()
        else:
            beritas = Berita.objects.only('title').order_by('-updated_at').to_json()
        return beritas


class BeritaView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def post(self, data, file=None):
        try:
            if file and allowed_file(file.filename):
                image_url = upload_file(file)
                berita = create_berita(data, self.identity, image_url)
            else:
                berita = create_berita(data, self.identity, None)
        except Exception as e:
            print(e)
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return 'success insert berita'

    def get(self, berita_id):
        # user = User.objects.get(username=self.identity)
        berita = Berita.objects.get(id=berita_id).to_json()
        return berita

    def delete(self, berita_id):
        berita = Berita.objects.get(id=berita_id)
        berita.delete()
        return 'success delete berita', StatusCodes.HTTP_204_NO_CONTENT


class UnitKerjaView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def post(self, data, file=None):
        try:
            if file and allowed_file(file.filename):
                bagan_url = upload_file(file)
                unit_kerja = create_unit_kerja(data, self.identity, bagan_url)
            else:
                unit_kerja = create_unit_kerja(data, self.identity, None)
        except Exception as e:
            print(e)
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return 'success insert unit kerja'

    def get(self, unit_kerja_id):
        unit_kerja = UnitKerja.objects.get(id=unit_kerja_id).to_json()
        return unit_kerja

    def delete(self, unit_kerja_id):
        unit_kerja = UnitKerja.objects.get(id=unit_kerja_id)
        unit_kerja.delete()
        return 'success delete unit kerja', StatusCodes.HTTP_204_NO_CONTENT


class UnitKerjaListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get(self, query_param):
        if query_param:
            list_unit_kerja = UnitKerja.objects.search_text(
                query_param).order_by('-updated_at').to_json()
        else:
            list_unit_kerja = UnitKerja.objects.order_by('-updated_at').to_json()
        return list_unit_kerja

    def get_title(self, query_param=None):
        if query_param:
            title_unit_kerja = UnitKerja.objects.only(
                'name').search_text(query_param).order_by('-updated_at').to_json()
        else:
            title_unit_kerja = UnitKerja.objects.only('name').order_by('-updated_at').to_json()
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
            print('error', e)
            return {'status': 'failed'}, StatusCodes.HTTP_400_BAD_REQUEST
        return json.dumps({'status': 'success', 'tujuan_id': tujuan_id})

    def delete(tujuan_id):
        pass


class RencanaKerjaListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get(self):
        try:
            result = get_list_rencana_kerja()
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return result

class RoleListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get(self):
        try:
            result = Role.objects.all()
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        return result.to_json()

    def post(self, data):
        try:
            if data.get('id'):
                role_obj = Role.objects.get(id=data.get('id'))
                role_obj.update(name=data.get('name'))
            else:
                role_obj = Role(name=data.get('name'))
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR
        
        return role_obj.to_json()


class VideoListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get_list(self, query_param):
        try:
            if query_param:
                result = Video.objects.search_text(
                    query_param).order_by('-updated_at').to_json()
            else:
                result = Video.objects.order_by('-updated_at').to_json()
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_400_BAD_REQUEST

        return result

    def get(self, video_id):
        try:
            result = Video.objects.get(id=video_id).to_json()
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_400_BAD_REQUEST

        return result

    def post(self, data):
        try:
            if data.get('id'):
                video_obj = Video.objects.get(id=data.get('id'))
                is_shown = True if data.get('is_shown') == 'true' else False
                video_obj.update(title=data.get('title'),
                                 description=data.get('description'),
                                 url=data.get('url'),
                                 is_shown=is_shown)
            else:
                is_shown = True if data.get('is_shown') == 'true' else False
                video_obj = Video(title=data.get('title'),
                                  description=data.get('description'),
                                  url=data.get('url'),
                                  is_shown=is_shown)
                video_obj.save()
        except Exception as e:
            print(e)
            return e.__str__(), StatusCodes.HTTP_400_BAD_REQUEST

        return video_obj.to_json()

    def delete(self, video_id):
        return


class ImageListView(object):
    def __init__(self, app):
        self.app = app
        self.identity = authenticate_user()

    def get_list(self, search_text):
        try:
            if search_text:
                result = Image.objects.search_text(search_text).order_by('-updated_at').to_json()
            else:
                result = Image.objects.order_by('-updated_at').to_json()
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_400_BAD_REQUEST

        return result

    def get(self, image_id):
        try:
            result = Image.objects.get(id=image_id).to_json()
        except Exception as e:
            return e.__str__(), StatusCodes.HTTP_400_BAD_REQUEST

        return result

    def post(self, data, file):
        try:
            is_shown = True if data.get('is_shown') == 'true' else False
            is_slider = True if data.get('is_slider') == 'true' else False
            if data.get('id'): 
                image_obj = Image.objects.get(id=data.get('id'))
                if file:
                    image_url = upload_file(file)
                else:
                    image_url = image_obj.image_url
                image_obj.update(title=data.get('title'),
                                 image_url=image_url,
                                 description=data.get('description'),
                                 is_shown=is_shown,
                                 is_slider=is_slider)
            else:
                if not file:
                    return 'Image Could Not be blank', StatusCodes.HTTP_400_BAD_REQUEST
                image_url = upload_file(file)
                image_obj = Image(title=data.get('title'),
                                  description=data.get('description'),
                                  image_url=image_url,
                                  is_shown=is_shown,
                                  is_slider=is_slider)
                image_obj.save()
        except Exception as e:
            print(e)
            return e.__str__(), StatusCodes.HTTP_400_BAD_REQUEST

        return image_obj.to_json()


class DownloadListView(object):
    pass
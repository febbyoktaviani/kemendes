import base64
import glob
import json
import os

from .helpers import *
from .model import *


def create_berita(data, identity, file_url):
    print(data)
    title = data['title']
    content = data['title']
    user = User.objects.get(username=identity)

    if data.get('id'):
        berita_obj = Berita.objects.get(id=data.get('id'))
        berita_obj.update(title=data.get('title'), content=data.get('content'), image=file_url)
    else:
        berita_obj = Berita(title=title, content=content, image=file_url, created_by=user)
        berita_obj.save()

    print(berita_obj)

def create_unit_kerja(data, identity, file_url):
    print(data)
    name = data['name']
    profil = data['profil']
    user = User.objects.get(username=identity)

    if data.get('id'):
        unitkerja_obj = UnitKerja.objects.get(id=data.get('id'))
        unitkerja_obj.update(name=name, profil=profil, bagan=file_url, created_by=user)
    else:
        unitkerja_obj = UnitKerja(name=name, profil=profil, bagan=file_url, created_by=user)
        unitkerja_obj.save()

    print(unitkerja_obj)

def get_rencana_kerja(id):
    tujuan = Tujuan.objects.get(id=id)
    indikators = Indikator.objects.filter(tujuan=tujuan)
    data = {}
    data['name'] = tujuan.name
    data['id'] = tujuan.id.__str__()
    data['unit_pemilik_resiko'] = tujuan.unit_pemilik_resiko
    data['unit_eselon'] = tujuan.unit_eselon
    data['periode'] = tujuan.periode
    data['kegiatan'] = tujuan.kegiatan
    data['indikators'] = []
    data['rowspan'] = 0
    for indikator in indikators:
        data_indikator = {}
        kegiatans = Kegiatan.objects.filter(indikator=indikator)
        data_indikator['id'] = indikator.id.__str__()
        data_indikator['name'] = indikator.name
        data_indikator['count_kegiatan'] = 0
        data_indikator['count_resiko'] = 0
        data_indikator['rowspan'] = 1
        data_indikator['kegiatans'] = []
        for kegiatan in kegiatans:
            data_kegiatan = {}
            data_kegiatan['id'] = kegiatan.id.__str__()
            data_kegiatan['name'] = kegiatan.name
            data_kegiatan['resiko_kegiatan'] = []
            data_indikator['count_kegiatan'] += 1
            resiko_kegiatan = ResikoKegiatan.objects.filter(kegiatan=kegiatan)
            for rs in resiko_kegiatan:
                data_rs = json.loads(rs.to_json())
                data_rs['id'] = rs.id.__str__()
                data_kegiatan['resiko_kegiatan'].append(data_rs)
                data_indikator['count_resiko'] += 1
            data_indikator['kegiatans'].append(data_kegiatan)
        data['rowspan'] += max(data_indikator['count_kegiatan'], data_indikator['count_resiko'])
        data_indikator['rowspan'] = max(data_indikator['count_kegiatan'],
                                        data_indikator['count_resiko'])
        data['indikators'].append(data_indikator)

    return data

def update_resiko_kegiatans(resiko_kegiatans, kegiatan_obj, indikator_obj, tujuan):
    # update resiko kegiatan 
    old_rks = ResikoKegiatan.objects.filter(kegiatan=kegiatan_obj)
    old_rk_ids = [rk.id.__str__() for rk in old_rks]
    new_rk_ids = []
    for resiko in resiko_kegiatans:
        if resiko.get('id') != '' and resiko.get('id') is not None:
            resiko_obj = ResikoKegiatan.objects.get(id=resiko['id'])
            resiko_obj.update(sumber_resiko=resiko['sumber_resiko'],
                              kategori_resiko=resiko['kategori_resiko'],
                              resiko=resiko['resiko'],
                              penyebab_resiko=resiko['penyebab_resiko'],
                              dampak_resiko=resiko['dampak_resiko'],
                              pengendalian_uraian=resiko['pengendalian_uraian'],
                              pengendalian_kategori=resiko['pengendalian_kategori'],
                              resiko_residual=resiko['resiko_residual'],
                              pemilik_resiko=resiko['pemilik_resiko'],
                              pengukuran_kemungkinan=resiko['pengukuran_kemungkinan'],
                              pengukuran_dampak=resiko['pengukuran_dampak'],
                              pengukuran_status_resiko=resiko['pengukuran_status_resiko'],
                              level_resiko=resiko['level_resiko'],
                              peringkat_resiko=resiko['peringkat_resiko'],
                              rtp=resiko['rtp'],
                              penanggung_jawab=resiko['penanggung_jawab'],
                              target_waktu=resiko['target_waktu'],
                              komunikasi=resiko['komunikasi'],
                              pemantauan=resiko['pemantauan'])
        else:
            resiko_obj = ResikoKegiatan(kegiatan=kegiatan_obj,
                                        indikator=indikator_obj,
                                        tujuan=tujuan,
                                        sumber_resiko=resiko['sumber_resiko'],
                                        kategori_resiko=resiko['kategori_resiko'],
                                        resiko=resiko['resiko'],
                                        penyebab_resiko=resiko['penyebab_resiko'],
                                        dampak_resiko=resiko['dampak_resiko'],
                                        pengendalian_uraian=resiko['pengendalian_uraian'],
                                        pengendalian_kategori=resiko['pengendalian_kategori'],
                                        resiko_residual=resiko['resiko_residual'],
                                        pemilik_resiko=resiko['pemilik_resiko'],
                                        pengukuran_kemungkinan=resiko['pengukuran_kemungkinan'],
                                        pengukuran_dampak=resiko['pengukuran_dampak'],
                                        pengukuran_status_resiko=resiko['pengukuran_status_resiko'],
                                        level_resiko=resiko['level_resiko'],
                                        peringkat_resiko=resiko['peringkat_resiko'],
                                        rtp=resiko['rtp'],
                                        penanggung_jawab=resiko['penanggung_jawab'],
                                        target_waktu=resiko['target_waktu'],
                                        komunikasi=resiko['komunikasi'],
                                        pemantauan=resiko['pemantauan'])
            resiko_obj.save()

        new_rk_ids.append(resiko_obj.id.__str__())

    # delete resiko kegiatans
    deleted_rk_ids = set(old_rk_ids) - set(new_rk_ids)
    deleted_resiko_kegiatans = ResikoKegiatan.objects.filter(id__in=deleted_rk_ids)
    deleted_resiko_kegiatans.delete()


def update_kegiatans(kegiatans, indikator_obj, tujuan):
    # update kegiatans
    old_kegiatans = Kegiatan.objects.filter(indikator=indikator_obj)
    old_kg_ids = [kg.id.__str__() for kg in old_kegiatans]
    new_kg_ids = []
    for kegiatan in kegiatans:
        if kegiatan.get('id') != '' and kegiatan.get('id') is not None:
            kegiatan_obj = Kegiatan.objects.get(id=kegiatan.get('id'))
            if kegiatan_obj.name != kegiatan.get('name'):
                kegiatan_obj.update(name=kegiatan.get('name'))
        else:
            kegiatan_obj = Kegiatan(name=kegiatan.get('name'),
                                    indikator=indikator_obj,
                                    tujuan=tujuan)
            kegiatan_obj.save()

        new_kg_ids.append(kegiatan_obj.id.__str__())
        resiko_kegiatan = kegiatan.get('resiko_kegiatan')
        update_resiko_kegiatans(resiko_kegiatan, kegiatan_obj, indikator_obj, tujuan)

    # delete kegiatans
    deleted_kg_ids = set(old_kg_ids) - set(new_kg_ids)
    deleted_kegiatans = Kegiatan.objects.filter(id__in=deleted_kg_ids)
    deleted_kegiatans.delete()

def update_rencana_kerja(data):
    if data.get('id') != '' and data.get('id') is not None:
        tujuan = Tujuan.objects.get(id=data.get('id'))
        tujuan.update(name=data.get('name'),
                      periode=data.get('periode'),
                      unit_pemilik_resiko=data.get('unit_pemilik_resiko'),
                      unit_eselon=data.get('unit_eselon'),
                      kegiatan=data.get('kegiatan'))
    else:
        tujuan = Tujuan(name=data.get('name'),
                        periode=data.get('periode'),
                        unit_pemilik_resiko=data.get('unit_pemilik_resiko'),
                        unit_eselon=data.get('unit_eselon'),
                        kegiatan=data.get('kegiatan'))
        tujuan.save()
        print('tj', tujuan)

    indikators = data.get('indikators')
    old_indikators = Indikator.objects.filter(tujuan=tujuan)
    old_idk_ids = [idk.id.__str__() for idk in old_indikators]
    new_idk_ids = []
    print('update_indikator')
    for indikator in indikators:
        if indikator.get('id') != '' and indikator.get('id') is not None:
            indikator_obj = Indikator.objects.get(id=indikator.get('id'))
            indikator_obj.update(name=indikator.get('name'))
        else:
            indikator_obj = Indikator(name=indikator.get('name'), tujuan=tujuan)
            indikator_obj.save()
        new_idk_ids.append(indikator_obj.id.__str__())

        # update kegiatans
        kegiatans = indikator.get('kegiatans')
        print('update_kegiatan')
        update_kegiatans(kegiatans, indikator_obj, tujuan)
        
    # delete indikators
    deleted_idk_ids = set(old_idk_ids) - set(new_idk_ids)
    deleted_indikators = Indikator.objects.filter(id__in=list(deleted_idk_ids))
    deleted_indikators.delete()
    return tujuan.id.__str__()

def search_tag_rencana_kerja(**kwargs):
    tags = kwargs['tags']
    keyword = kwargs['keyword']

def get_list_rencana_kerja():
    tujuan_list = Tujuan.objects.all()
    return tujuan_list.to_json()

def create_init_user_data(app):
    # create role
    role = Role(name='admin')
    role.save()

    # create user
    user = User(name='mimin',
                password=generate_password(app, 'mimin123'),
                email='mimin@mail.com',
                role=role)
    user.save()

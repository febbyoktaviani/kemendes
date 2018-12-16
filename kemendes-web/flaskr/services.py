import glob
import json
import os

from .model import *


def create_berita(data, identity, file):
    print(data)
    title = data['title']
    content = data['title']
    user = User.objects.get(username=identity)
    new_berita = Berita(title=title, content=content, image=file, created_by=user)
    new_berita.save()

    print(new_berita)

def create_unit_kerja(data, identity, file):
    print(data)
    name = data['name']
    profil = data['profil']
    user = User.objects.get(username=identity)
    new_unit_kerja = UnitKerja(name=name, profil=profil, bagan=file, created_by=user)
    new_unit_kerja.save()

    print(new_unit_kerja)

def get_rencana_kerja(id):
    tujuan = Tujuan.objects.get(id=id)
    indikators = Indikator.objects.filter(tujuan=tujuan)
    data = {}
    data['name'] = tujuan.name
    data['id'] = tujuan.id.__str__()
    data['indikators'] = []
    for indikator in indikators:
        data_indikator = {}
        kegiatans = Indikator.objects.filter(tujuan=tujuan)
        data_indikator['id'] = indikator.id.__str__()
        data_indikator['name'] = indikator.name
        data_indikator['kegiatans'] = []
        for kegiatan in kegiatans:
            data_kegiatan = {}
            data_kegiatan['id'] = kegiatan.id.__str__()
            data_kegiatan['name'] = kegiatan.name
            data_kegiatan['resiko_kegiatan'] = []
            resiko_kegiatan = ResikoKegiatan.objects.filter(kegiatan=kegiatan)
            for rs in resiko_kegiatan:
                data_rs = rs.to_json()
                data_kegiatan['resiko_kegiatan'].append(data_rs)
            data_indikator['kegiatans'].append(data_kegiatan)
        data['indikators'].append(data_indikator)

    return data

def search_tag_rencana_kerja(**kwargs):
    tags = kwargs['tags']
    keyword = kwargs['keyword']


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
    data['unit_pemilik_resiko'] = tujuan.unit_pemilik_resiko
    data['unit_eselon'] = tujuan.unit_eselon
    data['periode'] = tujuan.periode
    data['indikators'] = []
    for indikator in indikators:
        data_indikator = {}
        kegiatans = Kegiatan.objects.filter(indikator=indikator)
        data_indikator['id'] = indikator.id.__str__()
        data_indikator['name'] = indikator.name
        data_indikator['count_kegiatan'] = 0
        data_indikator['count_resiko'] = 0
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
        data['indikators'].append(data_indikator)

    return data

def update_rencana_kerja(data):
    tujuan = Tujuan.objects.get(id=data['id'])
    tujuan.update(name=data['name'],
                  periode=data['periode'],
                  unit_pemilik_resiko=data['unit_pemilik_resiko'],
                  unit_eselon=data['unit_eselon'])
    indikators = data['indikators']
    for indikator in indikators:
        if indikator['id'] != '':
            indikator_obj = Indikator.objects.get(id=indikator['id'])
            indikator_obj.update(name=indikator['name'])
        else:
            indikator_obj = Indikator(name=indikator['name'], tujuan=tujuan)
            indikator_obj.save()
        kegiatans = indikator['kegiatans']
        for kegiatan in kegiatans:
            if kegiatan['id'] != '':
                kegiatan_obj = Kegiatan.objects.get(id=kegiatan['id'])
                if kegiatan_obj.name != kegiatan['name']:
                    kegiatan_obj.update(name=kegiatan['name'])
            else:
                kegiatan_obj = Kegiatan(name=kegiatan['name'], indikator=indikator, tujuan=tujuan)
                kegiatan_obj.save()
            resiko_kegiatan = kegiatan['resiko_kegiatan']
            for resiko in resiko_kegiatan:
                print(resiko)
                if resiko['id'] != '':
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
                                      penangung_jawab=resiko['penangung_jawab'],
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
                                                penangung_jawab=resiko['penangung_jawab'],
                                                target_waktu=resiko['target_waktu'],
                                                komunikasi=resiko['komunikasi'],
                                                pemantauan=resiko['pemantauan'])
                    resiko_obj.save()
    return tujuan.id.__str__()

def search_tag_rencana_kerja(**kwargs):
    tags = kwargs['tags']
    keyword = kwargs['keyword']


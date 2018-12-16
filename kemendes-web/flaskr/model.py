from mongoengine import *
import datetime

class TimeStampModel(object):
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

class Role(Document, TimeStampModel):
    name = StringField(max_length=250, required=True, unique=True)


class User(Document, TimeStampModel):
    username = StringField(max_length=50, required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=100, required=True)
    role = ReferenceField(Role)


class Berita(Document, TimeStampModel):
    title = StringField(max_length=100, required=True)
    content = StringField(max_length=20000)
    image = ImageField()
    created_by = ReferenceField(User)

    search_field = ("title", 'created_by',)

    meta = {
        'indexes': [{
            'fields': ['$title', "$content"],
            'default_language': 'english',
            'weights': {'title': 10, 'content': 2}
        }]
    }

    @queryset_manager
    def objects(doc_cls, queryset):
        # This may actually also be done by defining a default ordering for
        # the document, but this illustrates the use of manager methods
        return queryset.order_by('created_at')

class UnitKerja(Document, TimeStampModel):
    name = StringField(max_length=500, required=True)
    bagan = ImageField()
    profil = StringField(max_length=50000)
    created_by = ReferenceField(User)

    search_field = ('name', )

class Tujuan(Document, TimeStampModel):
    name = StringField(max_length=500000, required=True)

class Indikator(Document, TimeStampModel):
    name = StringField(max_length=500, required=True)
    tujuan = ReferenceField(Tujuan)

class Kegiatan(Document, TimeStampModel):
    name = StringField(max_length=50000, required=True)
    tujuan = ReferenceField(Tujuan)
    indikator = ReferenceField(Indikator)

class ResikoKegiatan(Document, TimeStampModel):
    tujuan = ReferenceField(Tujuan)
    indikator = ReferenceField(Indikator)
    kegiatan = ReferenceField(Kegiatan)
    sumber_resiko = StringField(max_length=500, required=True)
    kategori_resiko = StringField(max_length=500, required=True)
    penyebab_resiko = StringField(max_length=500000, required=True)
    dampak_resiko = StringField(max_length=500000, required=True)
    pengendalian_uraian = StringField(max_length=500000, required=True)
    penyebab_kategori = StringField(max_length=500000, required=True)
    resiko_residual = StringField(max_length=500000, required=True)
    rtp = StringField(max_length=500000, required=True)
    penangung_jawab = StringField(max_length=500000, required=True)
    komunikasi = StringField(max_length=500000, required=True)
    pemantauan = StringField(max_length=500000, required=True)

<template>
  <div class='resiko-form'>
    <div class="panel-heading">
      <h4>{{tujuanName}}</h4>
    </div>
    <div class="panel-body">
      <div class="panel panel-success" v-for="(indikator, idx) in indikators">
        <div class="panel-heading">
          {{ indikator.name }}
        </div>
        <div class="panel-body" v-for="(kegiatan, kgidx) in indikator.kegiatans">
          <label>{{ kegiatan.name }}</label> 
          <button type="button" class="btn btn-info" v-on:click="add(idx, kgidx)">+</button>
          <div class="panel-body">
            <div class="panel panel-success" v-for="resiko in kegiatan.resiko_kegiatan">
              <div class="panel-body">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label class="control-label col-sm-3">Sumber Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.sumber_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Kategori Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.kategori_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Penyebab Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.penyebab_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Dampak:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.dampak_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Pegendalian Uraian:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.pengendalian_uraian">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Pegendalian Kategori:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.pengendalian_kategori">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Resiko Residual:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.resiko_residual">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Pemilik Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.pemilik_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Pengukuran Kemungkinan:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.pengukuran_kemungkinan">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Pengukuran Dampak:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.pengukuran_dampak">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Pengukuran Status resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.pengukuran_status_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Level Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.level_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Peringkat Resiko:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.peringkat_resiko">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">RTP:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.rtp">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Penanggung Jawab:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.penanggung_jawab">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Target Waktu:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.target_waktu">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Komunikasi:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model="resiko.komunikasi">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-3">Rencana Pemantauan:</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control" v-model='resiko.pemantauan'>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
          <!-- <form class="form-horizontal" v-for="(kegiatan, kgidx) in indikator.kegiatans">
            <button type="button" class="btn btn-info" v-on:click="add(idx, kgidx)">+</button>
            <div class="form-group">
              <label class="control-label col-sm-2">Kegiatan:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" name="email" v-model="kegiatan.name">
              </div>
            </div>
            <div class="panel panel-success" v-for="resiko in kegiatan.resiko_kegiatan">
              <div class="panel-body">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label class="control-label col-sm-2">Sumber Resiko:</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control">
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label col-sm-2">Kategori Resiko:</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control">
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </form>
        <hr>
      </form> -->
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['tujuanId', 'indikators', 'tujuanName'],
    name: 'ResikoForm',
    data() {
      return {
      };
    },
    methods: {
      add(idx, kgidx) {
        console.log('here', this.indikators[idx].kegiatans[kgidx])
        const data_resiko = {
          'id': '',
          'sumber_resiko': '',
          'kategori_resiko': '',
          'resiko': '',
          'penyebab_resiko': '',
          'dampak_resiko': '',
          'pengendalian_uraian': '',
          'pengendalian_kategori': '',
          'resiko_residual': '',
          'pemilik_resiko': '',
          'pengukuran_kemungkinan': '',
          'pengukuran_dampak': '',
          'pengukuran_status_resiko': '',
          'level_resiko': '',
          'peringkat_resiko': '',
          'rtp': '',
          'penanggung_jawab': '',
          'target_waktu': '',
          'komunikasi': '',
          'pemantauan': ''
        }
        this.indikators[idx].kegiatans[kgidx].resiko_kegiatan.push(data_resiko)
      }
    }
  };
</script>
<style type="text/css">
  .panel-footer {
    text-align: right !important;
  }
  .panel-success {
    margin-left: 10%;
    margin-right: auto;
  }
</style>
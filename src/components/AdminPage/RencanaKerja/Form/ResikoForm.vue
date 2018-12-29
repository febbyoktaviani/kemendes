<template>
  <div class='resiko-form'>
    <b-form class="mb-4">
      <h4>Resiko Kegiatan</h4>
      <br>
      <b-card v-for="(indikator, idx) in indikators" class="mt-2">
        <b-input-group prepend="Indikator" class="mb-2">
          <b-form-input v-model="indikator.name" type="text" disabled>
          </b-form-input>
        </b-input-group>
        <hr>
        <b-form v-for="(kegiatan, kgidx) in indikator.kegiatans" class="mt-4 ml-4">
          <b-input-group prepend="Kegiatan">
            <b-form-input v-model="kegiatan.name" type="text" disabled>
            </b-form-input>
            <b-input-group-append>
              <b-btn variant="outline-info" v-on:click="add(idx, kgidx)">+</b-btn>
            </b-input-group-append>
          </b-input-group>

          <b-card  v-for="(resiko, r_idx) in kegiatan.resiko_kegiatan" class="mt-2">
            <b-card-text>
              <b-btn variant="outline-danger"
                     size="sm"
                     v-on:click="remove(idx, kgidx, r_idx)">-</b-btn>
            </b-card-text>
            <br>
            <b-form>
              <b-form-group label="Sumber Resiko"
                            horizontal
                            :label-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.sumber_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Kategori Resiko"
                            horizontal
                            :label-cols="3"
                         class="p-1">
                <b-form-input v-model="resiko.kategori_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Resiko"
                            horizontal
                            label-cols="3"
                         class="p-1">
                <b-form-input v-model="resiko.resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Penyebab Resiko"
                            horizontal
                            :label-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.penyebab_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Dampak"
                            horizontal
                            :label-cols="3"
                            class="p-2">
                <b-form-input v-model="resiko.dampak_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Pengendalian Uraian"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pengendalian_uraian" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Pengendalian Kategori"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pengendalian_kategori" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Resiko Residual"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.resiko_residual" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Pemilik Resiko"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pemilik_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Pengukuran Kemungkinan"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pengukuran_kemungkinan" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Pengukuran Dampak"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pengukuran_dampak" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Pengukuran Status Resiko"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pengukuran_status_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Level Resiko"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.level_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Peringkat Resiko"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.peringkat_resiko" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="RTP"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.rtp" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Penanggung Jawab"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.penanggung_jawab" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Target Waktu"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.target_waktu" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Komunikasi"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.komunikasi" type="text">
                </b-form-input>
              </b-form-group>
              <b-form-group label="Rencana Pemantauan"
                            horizontal
                            :lbel-cols="3"
                            class="p-1">
                <b-form-input v-model="resiko.pemantauan" type="text">
                </b-form-input>
              </b-form-group>
            </b-form>
          </b-card>
        </b-form>
      </b-card>
    </b-form>
  </div>
</template>
<script>
export default {
  props: ['indikators', 'tujuanName'],
  name: 'ResikoForm',
  data() {
    return {
    };
  },
  methods: {
    add(idx, kgidx) {
      console.log('here', this.indikators[idx].kegiatans[kgidx]);
      const data_resiko = {
        id: '',
        sumber_resiko: '',
        kategori_resiko: '',
        resiko: '',
        penyebab_resiko: '',
        dampak_resiko: '',
        pengendalian_uraian: '',
        pengendalian_kategori: '',
        resiko_residual: '',
        pemilik_resiko: '',
        pengukuran_kemungkinan: '',
        pengukuran_dampak: '',
        pengukuran_status_resiko: '',
        level_resiko: '',
        peringkat_resiko: '',
        rtp: '',
        penanggung_jawab: '',
        target_waktu: '',
        komunikasi: '',
        pemantauan: '',
      };
      this.indikators[idx].kegiatans[kgidx].resiko_kegiatan.push(data_resiko);
    },
    remove(idx, kgidx, r_idx) {
      this.indikators[idx].kegiatans[kgidx].resiko_kegiatan.splice(r_idx, 1);
    },
  },
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

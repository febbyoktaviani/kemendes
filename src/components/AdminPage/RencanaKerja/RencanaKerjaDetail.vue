<template>
  <div class="rencana-kerja-detail">
    <b-container fluid class="text-left">
      <b-card bg-variant="sand"
              text-variant="brown"
              class="text-left">
        <p><strong>Unit pemilik resiko : {{ tujuan.unit_pemilik_resiko }}</strong></p>
        <p><strong>Unit Eselon III/IV : {{ tujuan.unit_eselon }}</strong></p>
        <p><strong>Periode : {{ tujuan.periode }}</strong></p>
        <p><strong>Kegiatan : {{ tujuan.kegiatan }}</strong></p>
        <div class="panel-body scroll">
          <table border="1px" width="200%" class="small">
            <tr>
              <th> Tujuan </th>
              <th>indikator</th>
              <th>kegiatan</th>
              <th v-for="field in riskFormList">
                {{ field }}
              </th>
            </tr>
            <tr v-for="(indikator, idx) in tujuan.indikators" >
              <td v-if="idx==0" :rowspan="tujuan.rowspan">
                {{ tujuan.name }}
              </td>
              <td> {{ indikator.name }} </td>
              <td>
                <table width="100%" class="table no-border">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td v-if="idx % 2 != 0">
                      {{ kegiatan.name }}
                    </td>
                    <td v-else> {{ kegiatan.name }} </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table no-border">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td style="border-top: 0px;">
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.sumber_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table no-border">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.kategori_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table no-border">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table no-border">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.penyebab_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.dampak_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pengendalian_uraian }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pengendalian_kategori }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.resiko_residual }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pemilik_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pengukuran_kemungkinan }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pengukuran_dampak }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pengukuran_status_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.level_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.peringkat_resiko }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.rtp }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.penanggung_jawab }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.target_waktu }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.komunikasi }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
              <td>
                <table width="100%" class="table table-striped">
                  <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                    <td>
                      <table>
                        <tr v-for="resiko in kegiatan.resiko_kegiatan">
                          <td>{{ resiko.pemantauan }}</td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </div>
        <br>
        <b-button href="#"
                  variant="success"
                  v-b-tooltip.hover title="download">
          <i class="fas fa-download fa-lg"></i>
        </b-button>
      </b-card>
    </b-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';

export default {
  props: ['tujuanId'],
  name: 'RencanaKerjaDetail',
  data() {
    return {
      fields: ['indikator', 'keg', 'resiko_kegiatan']
    };
  },
  created() {
    this.$store.dispatch('getTujuan', this.tujuanId);
    console.log('tujuan');
  },
  computed: {
    ...mapGetters({
      tujuan: 'tujuan',
      riskFormList: 'riskFormList',
    }),
  },
  methods: {

  },
};
</script>
<style type="text/css">
  table .no-border td {
    border-top: 0px;
  }
  .scroll {
    overflow-x: scroll;
  }
  th {
    font-size: 1.2em;
    text-align: center;
  }
  td {
    vertical-align: middle;
  }
  .container-table {
    min-width: 90%;
    margin-left: 5%;
    margin-right: 95%;
  }
</style>

<template>
  <div class="rencana-kerja-detail">
    <!-- <div class="container text-left">     -->
      <br>
      <!-- <div class="row"> -->
      <div class="container-table text-left">
        <div class="panel panel-success">
          <div class="panel-heading">
            <p><strong>Unit pemilik resiko : {{ tujuan.unit_pemilik_resiko }}</strong></p>
            <p><strong>Unit Eselon III/IV : {{ tujuan.unit_eselon }}</strong></p>
            <p><strong>Periode : {{ tujuan.periode }}</strong></p>
            <p><strong>Kegiatan : {{ tujuan.kegiatan }}</strong></p>
          </div>
          <div class="panel-body scroll">
            <table border="1px" width="200%">
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
                  <table width="100%" class="table table-striped">
                    <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                      <td v-if="idx % 2 != 0">
                        {{ kegiatan.name }}
                      </td>
                      <td v-else> {{ kegiatan.name }} </td>
                    </tr>
                  </table>
                </td>
                <td>
                  <table width="100%" class="table table-striped">
                    <tr v-for="(kegiatan, idx) in indikator.kegiatans">
                      <td>
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
                  <table width="100%" class="table table-striped">
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
                  <table width="100%" class="table table-striped">
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
                  <table width="100%" class="table table-striped">
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
          <div class="panel-heading"></div>
        </div>
      </div>
      <!-- </div> -->
    </div>
  <!-- </div> -->
</template>
<script>
  import { mapGetters } from 'vuex';
  export default {
    props: ['tujuanId'],
    name: 'RencanaKerjaDetail',
    data() {
      return {
        // tujuan: 'test',
      };
    },
    created() {
        this.$store.dispatch('getTujuan', this.tujuanId);
        console.log('tujuan')

    },
    computed: {
        ...mapGetters({
          tujuan: 'tujuan',
          riskFormList: 'riskFormList',
        })
    },
    methods: {
    //     createTujuan() {
    //         const opt = {
    //           method: 'POST',
    //           headers: new Headers({
    //             'Accept': 'application/json',
    //             'Access-Control-Allow-Origin': '*',
    //             'mode': 'no-cors'
    //           })
    //         }
    //         fetch('http://localhost:5000/tujuan', opt)
    //           .then((response) => {
    //             if(response.status == 200){
    //               return response.json();
    //             } 
    //           }).then((res) => {
    //             console.log('tujuan', res);
    //             this.tujuan = res;
    //           }).catch((err)=>{
    //             console.log('err', err);
    //           });
    //         }
      
    },
  };
</script>
<style type="text/css">
  .top-bordered {
    border-top: 2px;
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
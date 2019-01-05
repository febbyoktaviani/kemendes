<template>
  <div class="rencana-kerja-detail">
    <b-container fluid class="text-left">
      <b-card bg-variant="sand"
              text-variant="brown"
              class="text-left"
              ref="printed">
        <!-- <p><strong>Unit pemilik resiko : {{ tujuan.unit_pemilik_resiko }}</strong></p>
        <p><strong>Unit Eselon III/IV : {{ tujuan.unit_eselon }}</strong></p>
        <p><strong>Periode : {{ tujuan.periode }}</strong></p>
        <p><strong>Kegiatan : {{ tujuan.kegiatan }}</strong></p> -->
        <div :class="isPrinted">
          <table border="1px" width="100%" class="small">
            <tr>
              <td colspan="22">
                <strong>Unit pemilik resiko : {{ tujuan.unit_pemilik_resiko }}</strong>
              </td>
            </tr>
            <tr>
              <td colspan="22">
                <strong>Unit Eselon III/IV : {{ tujuan.unit_eselon }}</strong>
              </td>
            </tr>
            <tr>
              <td colspan="22">
                <strong>Periode : {{ tujuan.periode }}</strong>
              </td>
            </tr>
            <tr>
              <td colspan="22">
                <strong>Kegiatan : {{ tujuan.kegiatan }}</strong>
              </td>
            </tr>
            <tr>
              <th> Tujuan </th>
              <th>indikator</th>
              <th>kegiatan</th>
              <th v-for="field in riskFormList">
                {{ field }}
              </th>
            </tr>
            <tbody v-html="generateTable(tujuan)">
            </tbody>
            <!-- <tr v-for="(indikator, idx) in tujuan.indikators" >
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
            </tr> -->
          </table>
        </div>
        <br>
        <a href="#" v-on:click="print()">
          <i class="fas fa-download fa-lg"></i>
        </a>
      </b-card>
    </b-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import XLSX from 'xlsx';
export default {
  props: ['tujuanId'],
  name: 'RencanaKerjaDetail',
  data() {
    return {
      fields: ['indikator', 'keg', 'resiko_kegiatan'],
      output: null,
      isPrinted: 'panel-body scroll',
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
    generateTable(tujuan) {
      let table = ''
      var indikator_pointer = 1
      var indikator = {}
      var kegiatan_pointer = 1
      var idk_idx = 0
      var kg_idx = 0
      var rk_idx = 1
      for (var i = 1; i <= tujuan.rowspan; i++) {
        console.log('i', i, 'idk_point', indikator_pointer, 'kg_point', kegiatan_pointer)
        if (i == 1) {
          console.log('indikator', indikator, 'idkidx', idk_idx)
          indikator = tujuan.indikators[i-1]
          indikator_pointer += indikator.count_resiko;
          table += `<tr>\
                      <td rowspan="${tujuan.rowspan}">${tujuan.name}</td>\
                      <td rowspan="${indikator.count_resiko}">${indikator.name}</td>\
                      <td rowspan="${indikator.kegiatans[0].rowspan-1}">
                        ${indikator.kegiatans[0].name}
                      </td>`;
          table += this.generateColumnSr(indikator.kegiatans[0].resiko_kegiatan[0])
          table += '</tr>';
          kegiatan_pointer += indikator.kegiatans[0].resiko_kegiatan.length;
          idk_idx += 1
        } else if(0 < i  && i < indikator_pointer){
          if (i == kegiatan_pointer) {
            console.log('i', i, '=', 'kegiatan_pointer', kegiatan_pointer)
            kg_idx = i-2
            kegiatan_pointer += 1
            table += `<tr>\
                        <td rowspan="${indikator.kegiatans[kg_idx].rowspan-1}">\
                          ${indikator.kegiatans[kg_idx].name}\
                        </td>`;
            table += this.generateColumnSr(indikator.kegiatans[kg_idx].resiko_kegiatan[0])
            table += '</tr>'
          } else {
            rk_idx = kegiatan_pointer - i
            console.log('else kgidx', kg_idx, indikator.kegiatans, 'rkidx', rk_idx)
            table += `<tr>\
              ${this.generateColumnSr(indikator.kegiatans[kg_idx-1].resiko_kegiatan[rk_idx])}\
              </tr>`;
          }
        } else if(i == indikator_pointer && i != 1){
          indikator = tujuan.indikators[idk_idx]
          console.log('indikator', indikator, 'idkidx', idk_idx)
          indikator_pointer += indikator.count_resiko
          kegiatan_pointer += indikator.kegiatans[0].resiko_kegiatan.length;
          table += `<tr>\
                      <td rowspan="${indikator.count_resiko}">${indikator.name}</td>\
                      <td rowspan="${indikator.kegiatans[0].rowspan-1}">\
                        ${indikator.kegiatans[0].name}\
                      </td>`;
          table += this.generateColumnSr(indikator.kegiatans[0].resiko_kegiatan[0])
          table += '</tr>'
          idk_idx += 1
        } 
      }
      return table
    },
    generateColumnSr(sumber_resiko) {
      let rks = [ "sumber_resiko",
                  "kategori_resiko",
                  "resiko",
                  "penyebab_resiko",
                  "dampak_resiko",
                  "pengendalian_uraian",
                  "pengendalian_kategori",
                  "resiko_residual",
                  "pemilik_resiko",
                  "pengukuran_kemungkinan",
                  "pengukuran_dampak",
                  "pengukuran_status_resiko",
                  "level_resiko",
                  "peringkat_resiko",
                  "rtp",
                  "penanggung_jawab",
                  "target_waktu",
                  "komunikasi",
                  "pemantauan",
                ]
      let columns = ''
      for (var f = 0; f < rks.length; f++) {
        columns += `<td>\
                    ${sumber_resiko[rks[f]]}\
                  </td>`;
      }
      return columns
    },
    test() {
      alert('hai')
    },
    print() {
      this.isPrinted = 'panel-body'
      alert('hai')
      var el = this.$refs.printed;
      var wb = XLSX.utils.table_to_book(el)
      console.log(wb)
      XLSX.writeFile(wb, 'sample-excel.xls', {})
      // console.log(el)
      // html2canvas(el, {
      //       onrendered: function(canvas) {
      //           el.parentNode.style.overflow = 'hidden';         
      //           var imgData = canvas.toDataURL(
      //               'image/png');            
      //           var doc = new jsPDF("landscape");
      //           var width = doc.internal.pageSize.getWidth();
      //           var height = doc.internal.pageSize.getHeight();
      //           window.open(imgData, "toDataURL() image");
      //           doc.addImage(imgData, 'PNG', 20, 20);
      //           doc.save('sample-file.pdf');
      //       }
      //   });
    }
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
  table {
    padding: 0px;
  }
</style>

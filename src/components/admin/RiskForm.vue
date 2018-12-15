<template>
  <div class="risk-form">
    <div class="container text-left">    
      <br>
      <div class="row">
        <div class="col-sm-12 linkapp-container">
          <div class="panel panel-success">
            <div class="panel-heading">
              <h4>Tujuan</h4>
            </div>
            <div class="panel-body">
              <input class="form-control" type="text" v-model="tujuan" />
            </div>
            <div class="panel panel-success" v-for="idk in indikatorList">
              <div class="panel-heading">
                <h4>{{ indikators[idk] }}</h4>
              </div>
              <div class="panel-body">
                <div class="panel panel-success" v-for="kg in kegiatanList" v-if="kegiatan[kg]['indikator_id'] == idk">
                  <div class="panel-heading">
                    <h4>{{ kegiatan[kg]['desc'] }}</h4>
                  </div>
                  <div class="panel-body">
                    <div class="panel panel-success" v-for="sr in srList" v-if="srData[sr]['keg_id'] == kg">
                      <div class="panel-heading">
                        <h4>{{ srData[sr]['desc'] }}</h4>
                      </div>
                      <div class="panel-body">
                        <div class="row sub-field" v-for="field in sr_fields">
                          <label>{{ field }}</label>
                          <input type="text" name="" class="form-control" />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'RiskForm',
    data() {
      return {
        tujuan: 'Tujuan 1',
        indikators: {1: 'indikator 1', 2: 'indikator 2'},
        indikatorList: [1, 2],
        kegiatan: {
          1: {'indikator_id': 1, 'desc': 'kegiatan 1.1'},
          2: {'indikator_id': 1, 'desc': 'kegiatan 1.2'},
        },
        kegiatanList: [1, 2],
        srList: [1, 2],
        srData: {
          1: {'indikator_id': 1, 'keg_id': 1, 'desc': 'Sumber Resiko 1.1'},
          2: {'indikator_id': 1, 'keg_id': 1, 'desc': 'Sumber Resiko 1.2'}
        },
        sr_fields: [
          "kategori resiko",
          "penyebab resiko",
          "dampak resiko",
          "pengendalian uraian"
        ]
      };
    },
    watch() {

    },
    methods: {
      
    },
  };
</script>
<style type="text/css">
  .sub-field {
    padding: 10px;
  }
</style>
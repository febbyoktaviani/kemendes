<template>
  <div class='kegiatan-form'>
    <div class="panel-heading">
      <h4>Tujuan {{tujuanName}}</h4>
    </div>
    <div class="panel-body">
      <form class="form-horizontal" v-for="(indikator, idx) in indikators">
        <button type="button" class="btn btn-info" v-on:click="add(idx)">+</button>
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Indikator:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="email" v-model='indikator.name'>
            </div>
          </div>
        </div>
        <div class="row">
          <form class="form-horizontal" v-for="(kegiatan, k_idx) in indikator.kegiatans">
            <div class="form-group">
              <label class="control-label col-sm-2">Kegiatan:</label>
              <div class="col-sm-9">
                <input type="text" class="form-control" name="email" v-model="kegiatan.name">
              </div>
              <div class="col-sm-1">
                <button type="button" class="btn btn-info" v-on:click="remove(idx, k_idx)">-</button>
              </div>
            </div>
          </form>
        </div>
        <hr>
      </form>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['tujuanId', 'indikators', 'tujuanName'],
    name: 'KegiatanForm',
    data() {
      return {
      };
    },
    methods: {
      add(idx) {
        console.log(this.indikators[idx])
        this.indikators[idx].kegiatans.push({'name': '', 'id': '', 'resiko_kegiatan': []})
      },
      remove(idx, k_idx) {
        this.indikators[idx].kegiatans.splice(k_idx, 1)
      }
    }
  };
</script>
<style type="text/css">
  .panel-footer {
    text-align: right !important;
  }
</style>
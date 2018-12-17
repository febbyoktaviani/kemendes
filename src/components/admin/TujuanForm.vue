<template>
  <div class='tujuan-form'>
    <div class="panel-heading">
      <h4>Tujuan {{tujuan.name}}</h4>
    </div>
    <div class="panel-body">
      <form class="form-horizontal">
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Tujuan:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="email" v-model='tujuan.name'>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Unit Pemilik resiko:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="unit_pemilik_resiko" v-model='tujuan.unit_pemilik_resiko'>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Unit Eselon III/IV:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="unit_eselon" v-model='tujuan.unit_eselon'>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Periode:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="periode" v-model='tujuan.periode'>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Kegiatan:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="kegiatan" v-model='tujuan.kegiatan'>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['tujuanId', 'tujuan'],
    name: 'TujuanForm',
    data() {
      return {
        id: this.tujuanId,
        name: this.tujuan.name,
        unit_pemilik_resiko: this.tujuan.unit_pemilik_resiko,
        unit_eselon: this.unit_eselon
      };
    },
  };
</script>
<style type="text/css">
  .panel-footer {
    text-align: right !important;
  }
</style>
<template>
  <div class='indikator-form'>
    <div class="panel-heading">
      <h4>Tujuan {{tujuanName}}</h4>
    </div>
    <div class="panel-body">
      <button type="button" class="btn btn-info" v-on:click="add()">+</button>
      <form class="form-horizontal" v-for="(indikator, idx) in indikators">
        <div class="row">
          <div class="form-group">
            <label class="control-label col-sm-2">Indikator:</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" name="email" v-model='indikator.name'>
            </div>
            <div class="col-sm-1">
              <button type="button" class="btn btn-info" v-on:click="remove(idx)">-</button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
  export default {
    props: ['tujuanId', 'indikators', 'tujuanName'],
    name: 'IndikatorForm',
    data() {
      return {
      };
    },
    methods: {
      add() {
        console.log(this.indikators)
        this.indikators.push({'name': '', 'id': '', 'kegiatans': []})
      },
      remove(index) {
        console.log(this.indikators)
        this.indikators.splice(index, 1)
      }
    }
  };
</script>
<style type="text/css">
  .panel-footer {
    text-align: right !important;
  }
</style>
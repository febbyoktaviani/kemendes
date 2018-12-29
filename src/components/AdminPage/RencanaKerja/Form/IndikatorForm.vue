<template>
  <div class='indikator-form'>
    <b-form>
      <h4>Indikator   <b-button variant="info" size="sm" v-on:click="add()">+</b-button></h4>
        <br>
        <b-input-group prepend="Indikator" v-for="(indikator, idx) in indikators" class="mb-4">
          <b-form-input v-model="indikator.name" type="text">
          </b-form-input>
          <b-input-group-append>
            <b-btn variant="outline-success" v-on:click="remove(idx)">-</b-btn>
          </b-input-group-append>
        </b-input-group>
    </b-form>
  </div>
</template>
<script>
export default {
  props: ['indikators', 'tujuanName'],
  name: 'IndikatorForm',
  data() {
    return {
    };
  },
  methods: {
    add() {
      console.log(this.indikators);
      this.indikators.push({ name: '', id: '', kegiatans: [] });
    },
    remove(index) {
      console.log(this.indikators);
      this.indikators.splice(index, 1);
    },
  },
};
</script>
<style type="text/css">
  .panel-footer {
    text-align: right !important;
  }
</style>

<template>
  <div class='kegiatan-form'>
    <b-form>
      <h4>Kegiatan</h4>
      <br>
      <b-form v-for="(indikator, idx) in indikators" class="mb-4">
        <b-input-group prepend="Indikator">
          <b-form-input v-model="indikator.name" type="text" disabled>
          </b-form-input>
          <b-input-group-append>
            <b-btn variant="outline-info" v-on:click="add(idx)">+</b-btn>
          </b-input-group-append>
        </b-input-group>
        <b-container class="p-1">
          <b-input-group prepend="Kegiatan"
                         v-for="(kegiatan, k_idx) in indikator.kegiatans"
                         class="p-2">
            <b-form-input v-model="kegiatan.name" type="text">
            </b-form-input>
            <b-input-group-append>
              <b-btn variant="outline-danger" v-on:click="remove(idx, k_idx)">-</b-btn>
            </b-input-group-append>
          </b-input-group>
        </b-container>
      </b-form>
    </b-form>
  </div>
</template>
<script>
  export default {
    props: ['indikators', 'tujuanName'],
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
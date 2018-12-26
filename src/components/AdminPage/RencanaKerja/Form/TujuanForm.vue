<template>
  <div class='tujuan-form'>
    <b-form>
      <h5> Tujuan </h5>
      <b-form-group horizontal :label-cols="3" label="Tujuan">
        <b-form-input v-model="tujuan.name" type="text">
        </b-form-input>
      </b-form-group>
      <b-form-group horizontal :label-cols="3" label="Unit Pemilik Resiko">
        <b-form-input v-model="tujuan.unit_pemilik_resiko" type="text">
        </b-form-input>
      </b-form-group>
      <b-form-group horizontal :label-cols="3" label="Unit Eselon III/IV">
        <b-form-input v-model="tujuan.unit_eselon" type="text">
        </b-form-input>
      </b-form-group>
      <b-form-group horizontal :label-cols="3" label="Periode">
        <b-form-input v-model="tujuan.periode" type="text">
        </b-form-input>
      </b-form-group>
      <b-form-group horizontal :label-cols="3" label="Kegiatan">
        <b-form-input v-model="tujuan.kegiatan" type="text">
        </b-form-input>
      </b-form-group>
    </b-form>
  </div>
</template>
<script>
  export default {
    props: ['tujuan'],
    name: 'TujuanForm',
    data() {
      return {
        name: this.tujuan.name,
        unit_pemilik_resiko: this.tujuan.unit_pemilik_resiko,
        unit_eselon: this.tujuan.unit_eselon,
        kegiatan: this.tujuan.kegiatan
      };
    },
  };
</script>
<style type="text/css">
  .panel-footer {
    text-align: right !important;
  }
</style>
<template>
  <div class="unit-kerja-add">
    <b-container class="text-left">
      <h4>Add Unit Kerja</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Unit Kerja"
                        :label-cols="2"
                        horizontal>
            <b-form-input type="text" v-model="unitkerja.name"></b-form-input>
          </b-form-group>
          <b-form-group label="Profil"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-textarea type="text" v-model="unitkerja.profil" :rows="5"></b-form-textarea>
          </b-form-group>
          <b-form-group label="Bagan"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-file v-model="unitkerja.bagan"
                         v-on:change="onFileChanged(image)"
                         placeholder="Choose a file..."></b-form-file>
            <div class="mt-3">Selected image: {{ bagan && bagan.name}}</div>
            <b-img :src="bagan && getImageUrl(bagan)" fluid/>
          </b-form-group>
          <br>
          <b-form-group class="text-right">
            <b-button variant="info" v-on:click="onUpload()">Save</b-button>
          </b-form-group>
        </b-form>
      </b-card>
    </b-container>
  </div>
</template>
<script>
import Editor from '@tinymce/tinymce-vue';
import swal from 'sweetalert';

export default {
  props: [],
  name: 'UnitKerjaAdd',
  components: { editor: Editor },
  data() {
    return {
      unitkerja: {
        name: '',
        profil: '',
      },
      bagan: null,
    };
  },
  methods: {
    onFileChanged(event) {
      const file = event.target.files[0];
      this.bagan = file;
      console.log(file);
    },
    onUpload() {
      if (!this.bagan) {
        swal({
          title: 'Error Upload!',
          text: 'bagan could not be empty!!',
          icon: 'error',
          button: 'OK',
        });
      }
      const formData = new FormData();
      formData.append('bagan', this.bagan, this.bagan.name);
      formData.append('name', this.unitkerja.name);
      formData.append('profil', this.unitkerja.profil);
      console.log('frm', formData);
      this.$store.dispatch('uploadUnitKerja', formData);
    },
    getImageUrl(image) {
      return URL.createObjectURL(image);
    },
  },
};
</script>
<style type="text/css">
  .container-table {
    min-width: 80%;
    margin-left: 10%;
    margin-right: 70%;
  }
</style>

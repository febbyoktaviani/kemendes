<template>
  <div class="unit-kerja-edit">
    <b-container class="text-left">
      <h4>Edit Unit Kerja</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Unit Kerja"
                        :label-cols="2"
                        size="lg"
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
            <div class="mt-3">Selected image: {{unitkerja.bagan ? unitkerja.bagan : bagan && bagan.name}}</div>
            <b-img :src="bagan ? getImageUrl(bagan) : getImageUrl(unitkerja.bagan)" fluid/>
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
  import { mapGetters } from 'vuex';
  import { getImageUrl } from '@/helpers/util';
  export default {
    props: ['unitkerjaId'],
    name: 'UnitKerjaEdit',
    components: {'editor': Editor},
    data() {
      return {
        bagan: null,
        url_new: URL.createObjectURL(this.unitkerja.bagan),
      };
    },
    methods: {
      onFileChanged(event) {
        const file = event.target.files[0]
        this.bagan = file
        console.log(file)
        this.url_new = URL.createObjectURL(file)

      },
      onUpload() {
        const formData = new FormData()
        formData.append('bagan', this.bagan, this.bagan.name)
        formData.append('id', this.unitkerja._id.$oid)
        formData.append('name', this.unitkerja.name)
        formData.append('profil', this.unitkerja.profil)
        console.log('frm', formData)
        this.$store.dispatch('uploadUnitKerja', formData)

      },
      getImageUrl(filepath) {
        return getImageUrl(filepath)
      }
    },
    created() {
      this.$store.dispatch('fetchUnitKerja', this.unitkerjaId)
    },
    computed: {
      ...mapGetters({
        unitkerja: 'unitKerja'
      })
    },
  };
</script>
<style type="text/css">
  .container-table {
    min-width: 90%;
    margin-left: 5%;
    margin-right: 95%;
  }
  .holder {
    width: 80%;
    height: auto;
  }
</style>
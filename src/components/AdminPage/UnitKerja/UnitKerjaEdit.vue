<template>
  <div class="unit-kerja-edit">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          Unit Kerja
        </div>
        <div class="panel-body">
          <form class="form-horizontal">
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Unit Kerja:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="email" v-model='unitkerja.name'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Profil:</label>
                <div class="col-sm-9">
                  <editor :init="{plugins: 'wordcount'}" v-model="unitkerja.profil"></editor>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Bagan:</label>
                <div class="col-sm-5">
                  <input class="form-control" type="file" v-on:change="onFileChanged" />
                  <span> {{ unitkerja.bagan }} </span><br/>
                  <img :src="url_new ? url_new : getImageUrl(unitkerja.bagan)" class="holder"/>
                </div>
                <div class="col-sm-4">
                  <button type="button" class="btn btn-success" v-on:click="onUpload">Upload!</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import Editor from '@tinymce/tinymce-vue';
  import { mapGetters } from 'vuex';
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
        const file_folder = filepath.split('/')
        const image_url = `/${file_folder[4]}/${file_folder[5]}`
        return image_url
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
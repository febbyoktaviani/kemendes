<template>
  <div class="unit-kerja-add">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          <h4>Input Unit Kerja</h4>
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
                  <input class="form-control" type="file" v-on:change="onFileChanged">
                </div>
                <div class="col-sm-4">
                  <button type="button" class="btn btn-success" v-on:click="onUpload()">Upload!</button>
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
  export default {
    props: [],
    name: 'UnitKerjaAdd',
    components: {'editor': Editor},
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
        const file = event.target.files[0]
        this.bagan = file
        console.log(file)
      },
      onUpload() {
        const formData = new FormData()
        formData.append('bagan', this.bagan, this.bagan.name)
        formData.append('name', this.unitkerja.name)
        formData.append('profil', this.unitkerja.profil)
        console.log('frm', formData)
        this.$store.dispatch('uploadUnitKerja', formData)
      }
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
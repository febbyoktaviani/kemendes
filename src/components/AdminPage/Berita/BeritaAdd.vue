<template>
  <div class="berita-add">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          <h4>Input Berita</h4>
        </div>
        <div class="panel-body">
          <form class="form-horizontal">
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Judul:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="email" v-model='berita.judul'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Content:</label>
                <div class="col-sm-9">
                  <editor :init="{plugins: 'wordcount'}" v-model="berita.content"></editor>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Image:</label>
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
    name: 'BeritaAdd',
    components: {'editor': Editor},
    data() {
      return {
        berita: {
          judul: '',
          content: '',
        },
        image: null,
      };
    },
    methods: {
      onFileChanged(event) {
        const file = event.target.files[0]
        this.image = file
        console.log(file)
      },
      onUpload() {
        const formData = new FormData()
        formData.append('image', this.image, this.image.name)
        formData.append('data', this.berita)
        console.log(formData)
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
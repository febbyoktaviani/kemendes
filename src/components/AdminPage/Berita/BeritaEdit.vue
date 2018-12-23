<template>
  <div class="berita-edit">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          Berita
        </div>
        <div class="panel-body">
          <form class="form-horizontal">
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Judul:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="email" v-model='berita.title'>
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
                  <input class="form-control" type="file" v-on:change="onFileChanged" />
                  <span> {{ berita.image }} </span><br/>
                  <img :src="getImageUrl(berita.image)" width="200px" height="200px"/>
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
    props: ['beritaId'],
    name: 'BeritaEdit',
    components: {'editor': Editor},
    data() {
      return {
        judul: '',
        content: '',
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
        formData.append('id', this.berita._id.$oid)
        formData.append('title', this.berita.title)
        formData.append('content', this.berita.content)
        console.log('frm', formData)
        this.$store.dispatch('uploadBerita', formData)

      },
      getImageUrl(filepath) {
        const file_folder = filepath.split('/')
        const image_url = `/${file_folder[4]}/${file_folder[5]}`
        return image_url
      }
    },
    created() {
      this.$store.dispatch('fetchBerita', this.beritaId)
    },
    computed: {
      ...mapGetters({
        berita: 'berita'
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
</style>
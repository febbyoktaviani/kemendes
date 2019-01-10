<template>
  <div class="download-add">
    <b-container class="text-left">
      <h4>Add Download File</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Name"
                        :label-cols="2"
                        horizontal>
            <b-form-input type="text" v-model="download.name"></b-form-input>
          </b-form-group>
          <b-form-group label="Description"
                        :label-cols="2"
                        horizontal>
            <b-form-input type="text" v-model="download.description"></b-form-input>
          </b-form-group>
          <b-form-group label="File"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-file v-model="file"
                         v-on:change="onFileChanged(file)"
                         placeholder="Choose a file..."></b-form-file>
            <div class="mt-3">Selected file: {{ file && file.name}}</div>
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
    name: 'DownloadAdd',
    data() {
      return {
        download: {
          name: '',
          description: '',
        },
        file: null,
      };
    },
    methods: {
      onFileChanged(event) {
        const file = event.target.files[0]
        this.file = file
        console.log(file)
      },
      onUpload() {
        if (!this.file) {
          swal({
            title:'Error Upload!',
            text: 'file could not be empty!!',
            icon: 'error',
            button: 'OK',
          })
        } else {
          const formData = new FormData()
          formData.append('file', this.file, this.file.name)
          formData.append('name', this.download.name)
          formData.append('description', this.download.description)
          console.log('frm', formData)
          this.$store.dispatch('uploadDownload', formData)
        }
        
      },
      getImageUrl(file) {
        return URL.createObjectURL(file)
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
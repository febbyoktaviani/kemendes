<template>
  <div class="download-edit">
    <b-container class="text-left">
      <h4>Edit Download File</h4>
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
            <div class="mt-3">Selected image: {{download.file ? download.file : file && file.name}}</div>
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
import { mapGetters } from 'vuex';
import swal from 'sweetalert';
import { getImageUrl } from '@/helpers/util';
export default {
  props: ['downloadId'],
  name: 'DownloadEdit',
  data() {
    return {
      file: null,
    };
  },
  created() {
    this.$store.dispatch('fetchDownload', this.downloadId)
  },
  computed: {
    ...mapGetters({
      download: 'download'
    })
    
  },
  methods: {
    onFileChanged(event) {
      const file = event.target.files[0]
      this.file = file
      console.log(file)
    },
    onUpload() {
      const formData = new FormData()
      formData.append('id', this.imageId)
      if (this.file) {
        formData.append('file', this.file, this.file.name)
      }
      formData.append('name', this.download.title)
      formData.append('description', this.download.description)
      console.log('frm', formData)
      this.$store.dispatch('uploadDownload', formData)
    },
    getImageUrl(image) {
      return getImageUrl(image)
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
<template>
  <div class="download-edit">
    <b-container class="text-left">
      <h4>Edit Galery</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Name"
                        :label-cols="2"
                        horizontal>
            <b-form-input type="text" v-model="galery.title"></b-form-input>
          </b-form-group>
          <b-form-group :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-checkbox type="checkbox" v-model="galery.is_slider">slider</b-form-checkbox>
            <b-form-checkbox type="checkbox" v-model="galery.is_shown">tampilkan</b-form-checkbox>
          </b-form-group>
          <b-form-group label="Image"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-file v-model="image"
                         v-on:change="onFileChanged(image)"
                         placeholder="Choose a file..."></b-form-file>
            <div class="mt-3">Selected file: {{ galery.image_url ? getImageUrl(galery.image_url) : image && image.name}}</div>
            <b-img :src="galery.image_url ? getImageUrl(galery.image_url) : image && getImageUrl(image)" fluid/>
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
  props: ['imageId'],
  name: 'DownloadEdit',
  data() {
    return {
      image: null,
    };
  },
  created() {
    this.$store.dispatch('fetchGalery', this.imageId)
  },
  computed: {
    ...mapGetters({
      galery: 'galery'
    })
    
  },
  methods: {
    onFileChanged(event) {
      const file = event.target.files[0]
      this.image = file
      console.log(file)
    },
    onUpload() {
      const formData = new FormData()
      formData.append('id', this.imageId)
      if (this.image) {
        formData.append('image', this.image, this.image.name)
      }
      formData.append('title', this.galery.title)
      formData.append('is_slider', this.galery.is_slider)
      formData.append('is_shown', this.galery.is_shown)
      console.log('frm', formData)
      this.$store.dispatch('uploadGalery', formData)
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
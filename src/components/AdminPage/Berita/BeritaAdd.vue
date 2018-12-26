<template>
  <div class="berita-add">
    <b-container class="text-left">
      <h4>Add Berita</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Judul"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="text" v-model="berita.judul"></b-form-input>
          </b-form-group>
          <b-form-group label="Content"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-textarea type="text" v-model="berita.content" :rows="5"></b-form-textarea>
          </b-form-group>
          <b-form-group label="Image"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-file v-model="image"
                         v-on:change="onFileChanged(image)"
                         placeholder="Choose a file..."></b-form-file>
            <div class="mt-3">Selected image: {{image && image.name}}</div>
            <b-img :src="image && getImageUrl(image)" fluid/>
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
  import { getImageUrl } from '@/helpers/util';
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
        formData.append('title', this.berita.judul)
        formData.append('content', this.berita.content)
        console.log('frm', formData)
        this.$store.dispatch('uploadBerita', formData)
      },
      getImageUrl(image) {
        return URL.createObjectURL(image)
      }
    },
  };
</script>
<style type="text/css">
</style>
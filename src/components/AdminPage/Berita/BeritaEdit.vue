<template>
  <div class="berita-edit">
    <b-container class="text-left">
      <h4>Edit Berita</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Judul"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="text" v-model="berita.title"></b-form-input>
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
            <div class="mt-3">Selected image: {{berita.image ? berita.image : image && image.name}}</div>
            <b-img :src="image ? getImageUrl(image) : getImageUrl(berita.image)" fluid/>
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
    props: ['beritaId'],
    name: 'BeritaEdit',
    components: {'editor': Editor},
    data() {
      return {
        judul: '',
        content: '',
        image: null,
        url_new: null,
      };
    },
    methods: {
      onFileChanged(event) {
        const file = event.target.files[0]
        this.image = file
        console.log(file)
        this.url_new = URL.createObjectURL(file)

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
        return getImageUrl(filepath)
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
  .holder {
    width: 80%;
    height: auto;
  }
</style>
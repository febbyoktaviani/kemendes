<template>
  <div class="video-edit">
    <b-container class="text-left">
      <h4>Add Video</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Judul"
                        :label-cols="2"
                        horizontal>
            <b-form-input type="text" v-model="video.title"></b-form-input>
          </b-form-group>
          <b-form-group label="Deskripsi"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="text" v-model="video.description"></b-form-input>
          </b-form-group>
          <b-form-group label="Video Url"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="text" v-model="video.url"></b-form-input>
          </b-form-group>
          <b-form-group :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-checkbox type="checkbox" v-model="video.is_shown">tampilkan</b-form-checkbox>
          </b-form-group>
          <br>
          <b-form-group class="text-right">
            <b-button variant="info" v-on:click="onSave()">Save</b-button>
          </b-form-group>
        </b-form>
      </b-card>
    </b-container>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex';
  export default {
    props: ['videoId'],
    name: 'VideoEdit',
    data() {
      return {
      };
    },
    methods: {
      onSave() {
        const formData = new FormData()
        formData.append('id', this.video._id.$oid)
        formData.append('title', this.video.title)
        formData.append('description', this.video.description)
        formData.append('url', this.video.url)
        formData.append('is_shown', this.video.is_shown)
        this.$store.dispatch('uploadVideo', formData)
      }
    },
    created() {
      this.$store.dispatch('fetchVideo', this.videoId)
    },
    computed: {
      ...mapGetters({
        video: 'video'
      })
    }
  };
</script>
<style type="text/css">
  .container-table {
    min-width: 70%;
    margin-left: 15%;
    margin-right: 60%;
  }
  v-select.dropdown li a {
    padding: 10px 20px;
    display: flex;
    min-width: 100%;
    align-items: center;
    font-size: 1.25em;
  }
  v-select.dropdown {
    max-width: 100%;
  }
  .checkbox {
    display: block;
    position: relative;
    border-radius: 10em;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 22px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  .checkbox input {
    width: 1.5rem;
    height: 1.5rem;
  }
</style>
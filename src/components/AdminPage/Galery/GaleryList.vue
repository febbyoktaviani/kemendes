<template>
  <div class="galery-list">
    <b-container fluid>
      <b-card bg-variant="sand"
            text-variant="black"
            title="List Galery"
            class="text-left">

        <a href="/admin/galery/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-row>
          <b-col cols="3" v-for="galery in listGalery">
            <b-card title=""
                    :img-src="getImageUrl(galery.image_url)"
                    img-alt="Image"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2">
              <p class="card-text">
                {{ galery.title }}
              </p>
              <b-button :href="'/admin/galery/edit/'+galery._id.$oid" variant="primary">edit</b-button>
            </b-card>
          </b-col>
        </b-row>
      </b-card>
    </b-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import { getImageUrl } from '@/helpers/util';
export default {
  name: 'GaleryList',
  data() {
    return {
      image: null,
    };
  },
  created() {
    this.$store.dispatch('fetchListGalery')
  },
  computed: {
    ...mapGetters({
      listGalery: 'listGalery'
    })
    
  },
  methods: {
    onFileChanged(event) {
      const file = event.target.files[0]
      this.image = file
      console.log(file)
    },
    onUpload() {
      if (!this.image) {
        swal({
          title:'Error Upload!',
          text: 'image could not be empty!!',
          icon: 'error',
          button: 'OK',
        })
      }
      const formData = new FormData()
      formData.append('image', this.image, this.image.name)
      formData.append('name', this.galery.name)
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
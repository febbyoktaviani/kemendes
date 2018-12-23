<template>
  <div class="user-edit">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          Edit User
        </div>
        <div class="panel-body">
          <form class="form-horizontal">
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Username:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="" v-model='userData.username'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Password:</label>
                <div class="col-sm-9">
                  <input type="password" class="form-control" name="" v-model='userData.password'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Email:</label>
                <div class="col-sm-9">
                  <input type="email" class="form-control" name="email" v-model='userData.email'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="button-group text-center">
                <button class="btn btn-success"> Save </button>
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
    props: ['userId'],
    name: 'UserEdit',
    data() {
      return {
      };
    },
    methods: {
      onSave() {

      },
      onFileChanged(event) {
        const file = event.target.files[0]
        this.bagan = file
        console.log(file)

      },
      onUpload() {
        const formData = new FormData()
        formData.append('bagan', this.bagan, this.bagan.name)
        formData.append('id', this.unitkerja._id.$oid)
        formData.append('name', this.unitkerja.name)
        formData.append('profil', this.unitkerja.profil)
        console.log('frm', formData)
        this.$store.dispatch('uploadUnitKerja', formData)

      },
      getImageUrl(filepath) {
        const file_folder = filepath.split('/')
        const image_url = `/${file_folder[4]}/${file_folder[5]}`
        return image_url
      }
    },
    created() {
      this.$store.dispatch('fetchUser', this.userId)
    },
    computed: {
      ...mapGetters({
        userData: 'userData'
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
<template>
  <div class="video-add">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          <h4>Add Video</h4>
        </div>
        <div class="panel-body">
          <form class="form-horizontal">
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Title:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="" v-model='video.title'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Description:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="" v-model='video.description'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Video Url:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="email" v-model='video.video_url'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">is Shown:</label>
                <div class="col-sm-9">
                  <div class="checkbox">
                    <label><input type="checkbox" v-model="video.is_shown"></label>
                  </div>
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
  import { mapGetters, mapActions } from 'vuex';
  export default {
    props: [],
    name: 'VideoAdd',
    data() {
      return {
        video: {
          title: '',
          description: '',
          video_url: '',
          is_shown: '',
        },
      };
    },
    methods: {
      onSave() {

      }
    },
    created() {
    },
    computed: {
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
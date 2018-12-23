<template>
  <div class="user-add">
    <div class="container-table text-left">
      <div class="panel panel-success">
        <div class="panel-heading">
          <h4>Add User</h4>
        </div>
        <div class="panel-body">
          <form class="form-horizontal">
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Username:</label>
                <div class="col-sm-9">
                  <input type="text" class="form-control" name="" v-model='user.username'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Password:</label>
                <div class="col-sm-9">
                  <input type="password" class="form-control" name="" v-model='user.password'>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="form-group">
                <label class="control-label col-sm-2">Email:</label>
                <div class="col-sm-9">
                  <input type="email" class="form-control" name="email" v-model='user.email'>
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
  export default {
    props: [],
    name: 'UserAdd',
    data() {
      return {
        user: {
          username: '',
          password: '',
          email: '',
          role: '',
        },
        bagan: null,
      };
    },
    methods: {
      onSave() {

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
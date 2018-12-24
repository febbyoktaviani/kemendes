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
              <div class="form-group">
                <label class="control-label col-sm-2">Role:</label>
                <div class="col-sm-9">
                  <v-select :options="listRole" label="name" v-model="user.role">
                    <template slot="option" slot-scope="option">
                      {{ option.name }}
                    </template>      
                  </v-select>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="button-group text-center">
                <button type="button" class="btn btn-success" v-on:click="onSave()"> Save </button>
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
  import swal from 'sweetalert';
  export default {
    props: [],
    name: 'UserAdd',
    data() {
      return {
        user: {
          username: '',
          password: '',
          email: '',
          role: null,
        },
        bagan: null,
      };
    },
    methods: {
      onSave() {
        if (!this.user.role) {
          swal({
            title: 'Warning',
            text: 'please select user role!!',
            icon: 'warning',
            dangerMode: true,
            button: 'OK'
          });
        }
        const formData = new FormData()
        formData.append('username', this.user.username)
        formData.append('password', this.user.password)
        formData.append('email', this.user.email)
        formData.append('role', this.user.role._id.$oid)
        this.$store.dispatch('createUser', formData)
      }
    },
    created() {
      this.$store.dispatch('fetchListRole')
    },
    computed: {
      ...mapGetters({
        listRole: 'listRole'
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
</style>
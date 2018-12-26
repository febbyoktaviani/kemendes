<template>
  <div class="user-add">
    <b-container class="text-left">
      <h4>Add User</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Username"
                        :label-cols="2"
                        horizontal>
                        {{ username }}
            <b-form-input type="text" v-model="username" value=""></b-form-input>
          </b-form-group>
          <b-form-group label="Password"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="password" v-model="password"></b-form-input>
          </b-form-group>
          <b-form-group label="Email"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="email" v-model="email"></b-form-input>
          </b-form-group>
          <b-form-group label="Role"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-select v-model="role" :options="listRole">
            </b-form-select>
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
  import swal from 'sweetalert';
  export default {
    props: [],
    name: 'UserAdd',
    data() {
      return {
          username: null,
          password: null,
          email: null,
          role: null,
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
        formData.append('username', this.username)
        formData.append('password', this.password)
        formData.append('email', this.email)
        formData.append('role', this.role)
        this.$store.dispatch('createUser', formData)
      }
    },
    created() {
      this.$store.dispatch('fetchListRole')
      this.username = null;
      this.password = null;
      this.email = null;
      this.role = null;
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
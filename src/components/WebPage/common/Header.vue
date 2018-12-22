<template>
  <div class='header'>
    <header class="container-fluid text-left">
      <div class="container-fluid col-sm-6 text-left">
        <p><i class="fas fa-map-marker-alt"></i>&nbsp;&nbsp;<b>Jl. TMP Kalibata No.17, DKI Jakarta</b></p>
        <p>
            <i class="fas fa-phone-volume"></i>&nbsp;&nbsp;<b>+6251 878767</b>
            &nbsp;&nbsp;&nbsp;
            <i class="fas fa-envelope"></i>&nbsp;&nbsp;<b>contact@kemendesa.go.id</b>
        </p>
      </div>
      <div class="container-fluid col-sm-6 text-right" v-if="!user">
        <form class="form-horizontal">
          <div class="row">
            <div class="form-group col-sm-5">
              <label class="control-label col-sm-3">Username:</label>
              <div class="col-sm-8">
                <input type="text" class="form-control" name="email" v-model='username'>
              </div>
            </div>
            <div class="form-group col-sm-5">
              <label class="control-label col-sm-3">Password:</label>
              <div class="col-sm-8">
                <input type="password" class="form-control" name="password" v-model='password'>
              </div>
            </div>
            <div class="form-group col-sm-2">
              <button
                type="button"
                class="btn btn-success"
                v-on:click="login()">
                Login
              </button>
            </div>
          </div>
        </form>
      </div>
      <div class="container-fluid col-sm-6 text-right" v-else>
        <button
          type="button"
          class="btn btn-warning"
          v-on:click="logout()">
          Logout
        </button>
      </div>
    </header>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
    name: 'Header',
    data() {
        return {
            username: '',
            password: '',
            isLoggedin: false,
            submitted: false,

        };
    },
    computed: {
        ...mapGetters({
          user: 'user'
        })
    },
    created () {
        // reset login status
        // this.logout();
    },
    methods: {
      login() {
          this.submitted = true;
          if (this.username && this.password) {
            const userdata = {
              'username': this.username,
              'password': this.password
            } 
            this.$store.dispatch('login', userdata)
          }
      },
      logout() {
        this.$store.dispatch('logout')
      }
    }
};
</script>
<template>
  <div class='header'>
    <b-container fluid class="bg-mintleaf text-light p-3">
      <b-row>
        <b-col cols="6">
          <p><i class="fas fa-map-marker-alt"></i>&nbsp;&nbsp;<b>Jl. TMP Kalibata No.17, DKI Jakarta</b></p>
          <p>
              <i class="fas fa-phone-volume"></i>&nbsp;&nbsp;<b>+6251 878767</b>
              &nbsp;&nbsp;&nbsp;
              <i class="fas fa-envelope"></i>&nbsp;&nbsp;<b>contact@kemendesa.go.id</b>
          </p>
        </b-col>
        <b-col cols="6" v-if="!user">
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
                <br>
                <button
                  type="button"
                  class="btn btn-success"
                  v-on:click="login()">
                  Login
                </button>
              </div>
            </div>
          </form>
        </b-col>
        <b-col cols="6" class="text-right" v-else>
          <br>
          <a
            v-if="!isAdminPage()"
            title="admin page"
            data-toggle="tooltip"
            class="white text-center"
            href="/admin">
            <i class="fas fa-dungeon fa-2x"></i>
          </a>&nbsp;&nbsp;&nbsp;
          <a
            title="logout"
            data-toggle="tooltip"
            class="red text-center"
            href="#"
            v-on:click="logout()">
            <i class="fas fa-power-off fa-2x"></i>
          </a>
          <br>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';

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
      user: 'user',
    }),
  },
  created() {
    // reset login status
    // this.logout();
  },
  methods: {
    login() {
      this.submitted = true;
      if (this.username && this.password) {
        const userdata = {
          username: this.username,
          password: this.password,
        };
        this.$store.dispatch('login', userdata);
      }
    },
    logout() {
      this.$store.dispatch('logout');
    },
    isAdminPage() {
      return this.$route.path.includes('admin');
    },
  },
};
</script>
<style type="text/css">
  .red {
    color: red;
  }
  .white {
    color: white;
  }
  .bg-mintleaf {
    background-color: #479c96;
  }
</style>

<template>
  <div class="header" :style="{backgroundColor:'#0b5445'}">
    <div>
      <b-container class="text-light p-3">
        <b-row class="header-top">
          <b-col md="1" sm="12">
            <router-link to="/">
              <b-navbar-brand class="mx-auto">
                <img src="/static/logo-kemendesa.png" :style="{maxWidth:'100px'}">
              </b-navbar-brand>
            </router-link>
          </b-col>
          <b-col md="6" sm="12">
            <div class="mx-auto">
              <p class="text-vertical-center">
                Kementerian Desa, Pembangunan Daerah Tertinggal
                Dan Transmigrasi Republik Indonesia
              </p>
            </div>
          </b-col>
          <b-col md="3" sm="0"/>
          <b-col md="2" sm="12" v-if="!user">
            <div class="row desktop">
              <a href="#" id="loginButton" @click="popoverShow = !popoverShow" :disabled="popoverShow" class="text-vertical-center">
                Masuk
                &nbsp;
                <font-awesome-icon v-if="popoverShow" icon="angle-up" size="x" class="icon"></font-awesome-icon>
                <font-awesome-icon v-else icon="angle-down" size="x" class="icon"></font-awesome-icon>
              </a>
            </div>
            <b-popover
              target="loginButton"
              triggers="click"
              :show.sync="popoverShow"
              placement="auto"
              container="myContainer"
              ref="popover"
              @show="onShow"
              @shown="onShown"
              @hidden="onHidden"
            >
              <template slot="title">
                Selamat Datang
              </template>
              <div class="login-box">
                <div class="form-group">
                  <label class="control-label">Alamat Email</label>
                  <div>
                    <input type="text" class="form-control" name="email" v-model='username'>
                  </div>
                </div>
                <div class="form-group">
                  <label class="control-label">Kata Sandi</label>
                  <div>
                    <input type="password" class="form-control" name="password" v-model='password'>
                  </div>
                </div>
                <a href="#" class="red">Lupa Kata Sandi?</a>
                <div class="form-group">
                  <button
                    type="button"
                    class="btn btn-login text-light"
                    v-on:click="login()">
                    Masuk
                  </button>
                </div>
              </div>
            </b-popover>
          </b-col>
          <b-col cols="2" v-else>
            <div class="row desktop">
              <a
                v-if="!isAdminPage()"
                title="admin page"
                data-toggle="tooltip"
                class="white text-center"
                href="/admin"
              >
                Dashboard
              </a>
              <a
                v-else
                title="admin page"
                data-toggle="tooltip"
                class="white text-center"
                href="/"
              >
                Beranda
              </a>
              &nbsp;&nbsp;
              <p>|</p>
              &nbsp;&nbsp;
              Hi, {{user.username}}
              <a href="#" id="header-menu" @click="show = !show">
              &nbsp;
                <font-awesome-icon v-if="show" icon="angle-up" size="x" class="icon"></font-awesome-icon>
                <font-awesome-icon v-else icon="angle-down" size="x" class="icon"></font-awesome-icon>
              </a>
              <b-popover :show.sync="show" target="header-menu" placement="bottom" title="Pengaturan">
                <a title="logout"
                    data-toggle="tooltip"
                    class="text-center"
                    href="#"
                    v-on:click="logout()">
                  Keluar
                </a>
              </b-popover>                          
            </div>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div class="mobile">
      <b-card no-body class="mb-1 full">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-btn v-if="!user" class="bg-tosca" block href="#" v-b-toggle.accordion1>Masuk</b-btn>
          <b-btn v-else class="bg-tosca" block href="#" v-b-toggle.accordion1>Hi, {{user.username}}</b-btn>
        </b-card-header>
        <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <ul v-if="user" class="list-none">
              <a href="#" v-on:click="logout()">
                <li>
                  <a
                    v-if="!isAdminPage()"
                    title="admin page"
                    data-toggle="tooltip"
                    href="/admin"
                  >
                    Dashboard
                  </a>
                  <a
                    v-else
                    title="admin page"
                    data-toggle="tooltip"
                    href="/"
                  >
                    Beranda
                  </a>
                </li>
                <li>
                  <a title="logout"
                    data-toggle="tooltip"
                    class="text-center"
                    href="#"
                    v-on:click="logout()">
                    Keluar
                  </a>
                </li>
              </a>
            </ul>
            <div v-else class="login-box">
              <div class="form-group">
                <label class="control-label">Alamat Email</label>
                <div>
                  <input type="text" class="form-control" name="email" v-model='username'>
                </div>
              </div>
              <div class="form-group">
                <label class="control-label">Kata Sandi</label>
                <div>
                  <input type="password" class="form-control" name="password" v-model='password'>
                </div>
              </div>
              <a href="#" class="red">Lupa Kata Sandi?</a>
              <div class="form-group">
                <button
                  type="button"
                  class="btn btn-login text-light"
                  v-on:click="login()">
                  Masuk
                </button>
              </div>
            </div>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "Header",
  data() {
    return {
      username: "",
      password: "",
      isLoggedin: false,
      submitted: false,
      popoverShow: false,
      show: false
    };
  },
  computed: {
    ...mapGetters({
      user: "user"
    })
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
          password: this.password
        };
        this.$store.dispatch("login", userdata);
      }
    },
    logout() {
      this.$store.dispatch("logout");
    },
    isAdminPage() {
      return this.$route.path.includes("admin");
    }
  }
};
</script>
<style type="text/css">
.red {
  color: red;
}
.white {
  color: white;
}
.bg-tosca {
  background-color: #0b5445;
}

.bg-tosca:hover {
  background-color: #0b5445;
}
.bg-mintleaf {
  background-color: #479c96;
}
.text-vertical-center {
  padding-top: 3%;
}
.header .header-top {
  position: relative;
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
}
.btn-login {
  width: 100%;
  background-color: #0b5445;
}

@media only screen and (min-width: 576px) {
  .mobile {
    display: none;
  }
}
@media only screen and (max-width: 576px) {
  .desktop {
    display: none;
  }

}
</style>

<template>
    <div class="admin-menu">
      <nav class="navbar navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <!-- <a class="navbar-brand" href="#"> -->
            <a href="/">
              <img src="/static/logo-kemendesa.png" width="180px" height="100px" />
            </a>
            <!-- </a> -->
          </div>
          <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
              <li>
                <a href="/admin/rencana-kerja/list" v-on:click="navActive('rk')">
                    <i class="fas fa-swatchbook fa-2x"></i>
                    <h4>Rencana Kerja</h4>
                </a>
              </li>
              <li>
                <a href="/admin/berita/list">
                    <i class="fas fa-volume-up fa-2x"></i>
                    <h4>Berita</h4>
                </a>
              </li>
              <li>
                <a href="/admin">
                    <i class="fas fa-sitemap fa-2x"></i>
                    <h4>Struktur Organisasi</h4>
                </a>
              </li>
              <li>
                <a href="/admin/unit-kerja/list">
                    <i class="fas fa-building fa-2x"></i>
                    <h4>Unit kerja</h4>
                </a>
              </li>
              <li>
                <a href="/admin/list-tujuan">
                    <i class="fas fa-file-download fa-2x"></i>
                    <h4>Document</h4>
                </a>
              </li>
              <li>
                <a href="/admin/video/list">
                    <i class="fas fa-video fa-2x"></i>
                    <h4>Video</h4>
                </a>
              </li>
              <li>
                <a href="/admin/list-tujuan">
                    <i class="fas fa-camera fa-2x"></i>
                    <h4>Galery</h4>
                </a>
              </li>
              <li>
                <a href="/admin/user/list">
                    <i class="fas fa-users-cog fa-2x"></i>
                    <h4>User</h4>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
</template>
<script>
import {base_url} from '@/store/config'

export default {
  name: 'AdminMenu',
  data() {
    return {
      active: '',
      menus: ['Rencana Kerja', 'Berita', 'Unit Kerja']
    };
  },
  created() {
  },
  methods: {
    navActive(menu) {
      this.active = menu
    }
  },
};
</script>
<style type="text/css">
  .navbar {
    width: 80%;
    align-self: center;
    margin-left: auto;
    margin-right: auto;
  }
  .navbar-nav {
    margin-top: 1%;
    padding-left: 40px;
  }
  .navbar-nav>a:hover {
    color: white;
  }
</style>


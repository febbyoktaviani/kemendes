<template>
  <div class="admin-menu">
    <b-container fluid>
      <b-navbar toggleable="lg" type="muted" variant="tosca" class="text-boldtosca text-center">
        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-navbar-brand href="#">
          <a href="/">
            <img src="/static/logo-kemendesa.png" width="180px" height="100px" />
          </a>
        </b-navbar-brand>
        <b-collapse is-nav id="nav_collapse">
          <b-nav pills>
            <b-nav-item href="/admin/rencana-kerja/list">
              <i class="fas fa-swatchbook fa-2x"></i>
              <h5>Rencana Kerja</h5>
            </b-nav-item>
            <b-nav-item href="/admin/berita/list">
              <i class="fas fa-volume-up fa-2x"></i>
              <h5>Berita</h5>
            </b-nav-item>
            <b-nav-item href="/admin">
              <i class="fas fa-sitemap fa-2x"></i>
              <h5>Struktur Organisasi</h5>
            </b-nav-item>
            <b-nav-item href="/admin/unit-kerja/list">
              <i class="fas fa-building fa-2x"></i>
              <h5>Unit kerja</h5>
            </b-nav-item>
            <b-nav-item href="/admin">
              <i class="fas fa-file-download fa-2x"></i>
              <h5>Document</h5>
            </b-nav-item>
            <b-nav-item href="/admin/video/list">
              <i class="fas fa-video fa-2x"></i>
              <h5>Video</h5>
            </b-nav-item>
            <b-nav-item href="/admin/galery/list">
              <i class="fas fa-camera fa-2x"></i>
              <h5>Galery</h5>
            </b-nav-item>
            <b-nav-item href="/admin/user/list">
              <i class="fas fa-users fa-2x"></i>
              <h5>User</h5>
            </b-nav-item>
          </b-nav>
        </b-collapse>
      </b-navbar>
    </b-container>
  </div>
</template>
<script>
import { base_url } from '@/store/config';

export default {
  name: 'AdminMenu',
  data() {
    return {
      active: '',
      menus: ['Rencana Kerja', 'Berita', 'Unit Kerja'],
    };
  },
  created() {
  },
  methods: {
    navActive(menu) {
      this.active = menu;
    },
  },
};
</script>
<style type="text/css">
  .bg-tosca {
    background-color: #f3faf2;
  }
  .text-boldtosca {
    color: #008080;
  }
  .navbar {
    width: 100%;
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


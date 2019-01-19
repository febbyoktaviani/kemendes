<template>
  <div id="admin-menu">
    <b-container>
      <div class="row desktop">
          <nav class="navbar">
            <ul class="ul-list-none">
              <router-link to="/admin/rencana-kerja/list" class="nav-item">
                <li class="nav-items">
                  <p>Rencana Kerja</p>
                </li>
              </router-link>
              <router-link to="/admin/berita/list" class="nav-item">
                <li class="nav-items">
                  <p>Berita</p>
                </li>
              </router-link>
              <router-link to="/admin" class="nav-item">
                <li class="nav-items">
                  <p>Struktur Organisasi</p>
                </li>
              </router-link>
              <router-link to="/admin/unit-kerja/list" class="nav-item">
                <li class="nav-items">
                  <p>Unit Kerja</p>
                </li>
              </router-link>
              <router-link to="/admin/download/list" class="nav-item">
                <li class="nav-items">
                  <p>Dokumen</p>
                </li>
              </router-link>
              <router-link to="/admin/video/list" class="nav-item">
                <li class="nav-items">
                  <p>Vidio</p>
                </li>
              </router-link>
              <router-link to="/admin/galery/list" class="nav-item">
                <li class="nav-items">
                  <p>Galeri</p>
                </li>
              </router-link>
              <router-link to="/admin/user/list" class="nav-item">
                <li class="nav-items">
                  <p>User</p>
                </li>
              </router-link>
            </ul>
          </nav>
      </div>
      <div class="row mobile">
        <b-card no-body class="mb-1 full">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-btn class="bg-tosca" block href="#" v-b-toggle.accordion1>Menu</b-btn>
          </b-card-header>
          <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
            <b-card-body>
              <ul class="list-none">
                <router-link to="/admin/rencana-kerja/list">
                  <li>
                    <p>Rencana Kerja</p>
                  </li>
                </router-link>
                <router-link to="/admin/berita/list">
                  <li>
                    <p>Berita</p>
                  </li>
                </router-link>
                <router-link to="/admin">
                  <li>
                    <p>Struktur Organisasi</p>
                  </li>
                </router-link>
                <router-link to="/admin/unit-kerja/list">
                  <li>
                    <p>Unit Kerja</p>
                  </li>
                </router-link>
                <router-link to="/admin/download/list">
                  <li>
                    <p>Dokumen</p>
                  </li>
                </router-link>
                <router-link to="/admin/video/list">
                  <li>
                    <p>Vidio</p>
                  </li>
                </router-link>
                <router-link to="/admin/galery/list">
                  <li>
                    <p>Galeri</p>
                  </li>
                </router-link>
                <router-link to="/admin/user/list">
                  <li>
                    <p>User</p>
                  </li>
                </router-link>
              </ul>
            </b-card-body>
          </b-collapse>
        </b-card>
      </div>
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
a {
  color: inherit;
}

.bg-tosca {
  background-color: #0b5445;
}

.bg-tosca:hover {
  background-color: #0b5445;
}

.text-boldtosca {
  color: #008080;
}

#menu {
  -webkit-box-shadow: 0 8px 6px -6px grey;
       -moz-box-shadow: 0 8px 6px -6px grey;
            box-shadow: 0 8px 6px -6px grey;
}

.navbar {
  padding: 0 0;
}

.full {
  width: 100%;
}

.list-none {
    list-style-type: none;
}

.ul-list-none {
    display: flex;
    margin: 0;
    padding: 0;
    width: 80%;
    justify-content: space-between;
    list-style-type: none;
}

.nav-items {
    display: inline-block;
    color: #000;
    text-decoration: none;
}

.nav-items::after {
    content: '';
    display: block;
    width: 0;
    height: 2px;
    background: rgb(207, 5, 5);
    transition: width .3s;
}

.nav-items:hover::after {
    width: 100%;
}



@media only screen and (min-width: 576px) {
  .navbar {
    width: 80%;
  }
  .nav-item > * {
    margin-top: 1rem;
    margin-bottom: 0rem;
  }
  .mobile {
    display: none;
  }
}
@media only screen and (max-width: 576px) {
  .navbar-nav {
    display: flex;
  }
  .nav-item > * {
    margin-top: 1rem;
    margin-bottom: 0.5rem;
  }
  .desktop {
    display: none;
  }

}
</style>


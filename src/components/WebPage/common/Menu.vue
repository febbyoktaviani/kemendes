<template>
  <div id="menu">
    <b-container>
      <div class="row desktop">
          <nav class="navbar">
            <ul class="ul-list-none">
              <router-link to="/" class="nav-item">
                <li class="nav-items">
                  <p>Beranda</p>
                </li>
              </router-link>
              <router-link to="/about" class="nav-item">
                <li class="nav-items">
                  <p>Tentang DitjenPKP</p>
                </li>
              </router-link>
              <router-link to="/unitkerja" class="nav-item">
                <li class="nav-items">
                  <p>Unit Kerja</p>
                </li>
              </router-link>
              <router-link to="/berita" class="nav-item">
                <li class="nav-items">
                  <p>Berita</p>
                </li>
              </router-link>
              <router-link to="/about" class="nav-item">
                <li class="nav-items">
                  <p>Layanan</p>
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
                <router-link to="/">
                  <li>
                    <p>Beranda</p>
                  </li>
                </router-link>
                <router-link to="/about">
                  <li>
                    <p>Tentang DitjenPKP</p>
                  </li>
                </router-link>
                <router-link to="/unitkerja">
                  <li>
                    <p>Unit Kerja</p>
                  </li>
                </router-link>
                <router-link to="/berita">
                  <li>
                    <p>Berita</p>
                  </li>
                </router-link>
                <router-link to="/about">
                  <li>
                    <p>Layanan</p>
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
import { base_url } from "@/store/config";
// import { getListBerita } from "@/api/berita";
// import { getListUnitKerja } from "@/api/unitkerja";
import { mapActions, mapState } from "vuex";

export default {
  name: "Menu",
  data() {
    return {
      msg: "",
      username: "",
      password: ""
    };
  },
  computed: mapState({
    berita: state => state.berita.listBerita,
    unitKerja: state => state.unitKerja.unitKerjaList
  }),
  methods: {
    ...mapActions({
      fetchUnitKerja: "fetchListUnitKerja", // map `this.increment()` to `this.$store.dispatch('increment')`
      fetchBerita: "fetchListBerita"
    })
  },
  async mounted() {
    await Promise.all([this.fetchUnitKerja(), this.fetchBerita()]);
    // await this.fetchUnitKerja();
    // await this.fetchBerita();
  }
};
</script>
<style>
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
    width: 60%;
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
  .desktop {
    display: block;
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
  .mobile {
    display: block;
  }
  .desktop {
    display: none;
  }

}
</style>


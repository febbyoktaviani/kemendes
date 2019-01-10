<template>
  <div class="menu">
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <!-- <a class="navbar-brand" href="#"> -->
          <!-- </a> -->
        </div>

        <b-navbar toggleable="md" type="muted" variant="tosca" class="navbar text-boldtosca text-center">
          <b-navbar-toggle target="nav_collapse">
            <b>MENU</b>
          </b-navbar-toggle>

          <router-link to="/">
            <b-navbar-brand>
              <img src="/static/logo-kemendesa.png" width="200px" height="140px">
            </b-navbar-brand>
          </router-link>

          <b-collapse is-nav id="nav_collapse">
            <b-navbar-nav class="navbar-nav">
              <b-nav-item>
                <router-link to="/" class="nav-item">
                  <font-awesome-icon icon="home" size="4x"></font-awesome-icon>
                  <h4>BERANDA</h4>
                </router-link>
              </b-nav-item>
              <b-nav-item>
                <router-link to="/about" class="nav-item">
                  <font-awesome-icon icon="cog" size="4x"></font-awesome-icon>
                  <h4>TENTANG
                    <br>DITJENPKP
                  </h4>
                </router-link>
              </b-nav-item>
              <b-nav-item>
                <router-link to="/unitkerja" class="nav-item" slot="button-content">
                  <font-awesome-icon icon="pen" size="4x"></font-awesome-icon>
                  <h4>UNIT KERJA</h4>
                </router-link>
              </b-nav-item>
              <b-nav-item>
                <router-link class="nav-item" to="/berita">
                  <font-awesome-icon icon="lightbulb" size="4x"></font-awesome-icon>
                  <h4>BERITA</h4>
                </router-link>
              </b-nav-item>
              <b-nav-item-dropdown href="#">
                <div slot="button-content" class="nav-item">
                  <font-awesome-icon icon="concierge-bell" size="4x"></font-awesome-icon>
                  <h4>LAYANAN</h4>
                </div>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </div>
    </nav>
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
  background-color: #f3faf2;
}
.text-boldtosca {
  color: #008080;
}

@media only screen and (min-width: 576px) {
  .navbar {
    width: 80%;
    align-self: center;
    margin-left: auto;
    margin-right: auto;
  }
  .navbar-nav {
    display: flex;
    align-items: flex-start;
    justify-content: space-evenly;
    width: 100%;
  }
  .nav-item {
    justify-content: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .nav-item > * {
    margin-top: 0.5rem;
  }
}
@media only screen and (max-width: 576px) {
  .navbar-nav {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    width: 100%;
  }
  .nav-item {
    justify-content: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .nav-item > * {
    margin-top: 0.5rem;
  }
}
</style>


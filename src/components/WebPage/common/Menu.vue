<template>
  <div class="menu">
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <!-- <a class="navbar-brand" href="#"> -->
          <!-- </a> -->
        </div>

        <b-navbar toggleable="md" type="dark" variant="info" class="navbar">
          <b-navbar-toggle target="nav_collapse">
            <b>MENU</b>
          </b-navbar-toggle>

          <b-navbar-brand href="#">
            <img src="/static/logo-kemendesa.png" width="200px" height="140px">
          </b-navbar-brand>

          <b-collapse is-nav id="nav_collapse">
            <b-navbar-nav class="navbar-nav">
              <b-nav-item href="#">
                <div class="nav-item">
                  <font-awesome-icon icon="home" size="4x"></font-awesome-icon>
                  <h4>BERANDA</h4>
                </div>
              </b-nav-item>
              <b-nav-item href="#">
                <div class="nav-item">
                  <font-awesome-icon icon="cog" size="4x"></font-awesome-icon>
                  <h4>TENTANG
                    <br>DITJENPKP
                  </h4>
                </div>
              </b-nav-item>
              <b-nav-item href="#">
                <div class="nav-item">
                  <font-awesome-icon icon="pen" size="4x"></font-awesome-icon>
                  <h4>UNIT KERJA</h4>
                </div>
              </b-nav-item>
              <b-nav-item-dropdown href="#">
                <div class="nav-item" slot="button-content">
                  <font-awesome-icon icon="lightbulb" size="4x"></font-awesome-icon>
                  <h4>BERITA</h4>
                </div>
              </b-nav-item-dropdown>
              <b-nav-item-dropdown href="#">
                <div slot="button-content" class="nav-item">
                  <font-awesome-icon icon="concierge-bell" size="4x"></font-awesome-icon>
                  <h4>LAYANAN</h4>
                </div>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <!-- <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav">
            <li class="active">
              <a href="#">
                <font-awesome-icon icon="home" size="4x"></font-awesome-icon>
                <h4>BERANDA</h4>
              </a>
            </li>
            <li>
              <a href="#">
                <div class="dropdown">
                  <font-awesome-icon icon="cog" size="4x"></font-awesome-icon>
                  <h4>TENTANG DITJENPKP</h4>
                  <div class="dropdown-content text-left">
                    <h4>TUGAS & FUNGSI</h4>
                    <h4>STRUKTUR ORGANISASI</h4>
                  </div>
                </div>
              </a>
            </li>
            <li>
              <a href="#">
                <div class="dropdown">
                  <font-awesome-icon icon="pen" size="4x"></font-awesome-icon>
                  <h4>UNIT KERJA</h4>
                  <div class="dropdown-content text-left">
                    <h4 v-for="unit in unitKerja">{{ unit['name'] }}</h4>
                  </div>
                </div>
              </a>
            </li>
            <li>
              <a href="#">
                <div class="dropdown">
                  <font-awesome-icon icon="lightbulb" size="4x"></font-awesome-icon>
                  <h4>BERITA</h4>
                  <div class="dropdown-content text-left">
                    <h4 v-for="itemBerita in berita">{{ itemBerita['title'] }}</h4>
                  </div>
                </div>
              </a>
            </li>
            <li>
              <a href="#">
                <div class="dropdown">
                  <font-awesome-icon icon="concierge-bell" size="4x"></font-awesome-icon>
                  <h4>LAYANAN</h4>
                  <div class="dropdown-content text-left">
                    <h4>DOWNLOAD</h4>
                    <h4>GALERI</h4>
                  </div>
                </div>
              </a>
            </li>
          </ul>
        </div>-->
      </div>
    </nav>
  </div>
</template>
<script>
import { base_url } from '@/store/config';

export default {
  name: 'Menu',
  data() {
    return {
      msg: '',
      berita: [
        {
          title: 'Berita 1',
          image: '',
          content: 'content berita 1',
        },
        {
          title: 'Berita 2',
          image: '',
          content: 'content berita 2',
        },
      ],
      unitKerja: [],
      username: '',
      password: '',
    };
  },
  created() {
    const opt = {
      method: 'GET',
      headers: new Headers({
        Accept: 'application/json',
        'Access-Control-Allow-Origin': '*',
        mode: 'no-cors',
      }),
    };
    fetch(`${base_url}/title-berita`, opt)
      .then((response) => {
        if (response.status == 200) {
          return response.json();
        }
      })
      .then((res) => {
        console.log(res);
        this.berita = res;
      })
      .catch((err) => {
        console.log('err', err);
      });

    fetch(`${base_url}/title-unitkerja`, opt)
      .then((response) => {
        if (response.status == 200) {
          return response.json();
        }
      })
      .then((res) => {
        console.log(res);
        this.unitKerja = res;
      })
      .catch((err) => {
        console.log('err', err);
      });
  },
};
</script>
<style>
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


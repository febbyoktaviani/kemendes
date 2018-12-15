<template>
    <div class="menu">
      <nav class="navbar navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <!-- <a class="navbar-brand" href="#"> -->
              <img src="/static/logo-kemendesa.png" width="200px" height="140px" />
            <!-- </a> -->
          </div>
          <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
              <li class="active">
                <a href="#">
                    <font-awesome-icon icon="home" size="4x"></font-awesome-icon>
                    <h4>Beranda</h4>
                </a>
              </li>
              <li>
                <a href="#">
                  <div class="dropdown">
                    <font-awesome-icon icon="cog" size="4x"></font-awesome-icon>
                    <h4>Tentang DitjenPKP</h4>
                    <div class="dropdown-content">
                      <h4>Tugas & Fungsi</h4>
                      <h4>Struktur Organisasi</h4>
                    </div>
                  </div>
                </a>
              </li>
              <li>
                <a href="#">
                    <font-awesome-icon icon="pen" size="4x"></font-awesome-icon>
                    <h4>Unit kerja</h4>
                </a>
              </li>
              <li>
                <a href="#">
                  <div class="dropdown">
                    <font-awesome-icon icon="lightbulb" size="4x"></font-awesome-icon>
                    <h4>Berita</h4>
                    <div class="dropdown-content">
                        <h4 v-for="itemBerita in berita">
                        {{ itemBerita['title'] }}
                        </h4>
                    </div>
                  </div>
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="concierge-bell" size="4x"></font-awesome-icon>
                  <h4>Layanan</h4>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
</template>
<script>
export default {
  name: 'Menu',
  data() {
    return {
      msg: '',
      berita: [
        {
            "title": "Berita 1",
            "image": "",
            "content": "content berita 1"
        },
        {
            "title": "Berita 2",
            "image": "",
            "content": "content berita 2"
        }
    ],

    };
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
</style>


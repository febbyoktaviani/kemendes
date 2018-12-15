<template>
  <div id="app">
    <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>                        
          </button>
          <a class="navbar-brand" href="#">Logo</a>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav">
            <li class="active">
              <a href="#">
                <font-awesome-icon icon="home" size="3x"></font-awesome-icon>
                <h4>Beranda</h4>
              </a>
            </li>
            <li>
              <a href="#">
                <div class="dropdown">
                  <font-awesome-icon icon="cog" size="3x"></font-awesome-icon>
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
                <font-awesome-icon icon="pen" size="3x"></font-awesome-icon>
                <h4>Unit kerja</h4>
              </a>
            </li>
            <li>
              <a href="#">
                <font-awesome-icon icon="lightbulb" size="3x"></font-awesome-icon>
                <h4>Berita</h4>
              </a>
            </li>
            <li>
              <a href="#">
                <font-awesome-icon icon="concierge-bell" size="3x"></font-awesome-icon>
                <h4>Layanan</h4>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

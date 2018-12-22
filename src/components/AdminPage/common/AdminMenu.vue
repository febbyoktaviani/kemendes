<template>
    <div class="admin-menu">
      <nav class="navbar navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <!-- <a class="navbar-brand" href="#"> -->
              <img src="/static/logo-kemendesa.png" width="180px" height="100px" />
            <!-- </a> -->
          </div>
          <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
              <li class="active">
                <a href="/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Rencana Kerja</h4>
                </a>
              </li>
              <li>
                <a href="/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Berita</h4>
                </a>
              </li>
              <li>
                <a href="/#/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Struktur Organisasi</h4>
                </a>
              </li>
              <li>
                <a href="/#/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Unit kerja</h4>
                </a>
              </li>
              <li>
                <a href="/#/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Download</h4>
                </a>
              </li>
              <li>
                <a href="/#/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Video</h4>
                </a>
              </li>
              <li>
                <a href="/#/admin/list-tujuan">
                    <font-awesome-icon icon="cog" size="2x"></font-awesome-icon>
                    <h4>Galery</h4>
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
      msg: '',
      berita: [
        {
            'title': 'Berita 1',
            'image': '',
            'content': 'content berita 1'
        },
        {
            'title': 'Berita 2',
            'image': '',
            'content': 'content berita 2'
        },
    ],
    unitKerja: [],
    username: '',
    password: ''

    };
  },
  created() {
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


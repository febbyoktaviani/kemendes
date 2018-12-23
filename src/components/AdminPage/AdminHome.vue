<template>
  <div class="admin-home">
    <AdminMenu />
    <div class="container-fluid" v-if="$route.path == '/admin'">
      <div class="container-table">
        <div class="panel panel-success">
          <div class="panel-body">
            <div class="row">
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <i class="fas fa-swatchbook fa-3x"></i>
                  <h4>Rencana Kerja</h4>
                </div>
              </div>
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <a href="/admin/berita/list">
                    <i class="fas fa-volume-up fa-3x"></i>
                    <h4>Berita</h4>
                  </a>
                </div>
              </div>
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <i class="fas fa-swatchbook fa-3x"></i>
                  <h4>Rencana Kerja</h4>
                </div>
              </div>
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <a href="/admin">
                    <i class="fas fa-sitemap fa-3x"></i>
                    <h4>Struktur Organisasi</h4>
                </a>
                </div>
              </div>
            </div>
            <br>
            <div class="row">
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <i class="fas fa-swatchbook fa-3x"></i>
                  <h4>Rencana Kerja</h4>
                </div>
              </div>
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <a href="/admin/berita/list">
                    <i class="fas fa-volume-up fa-3x"></i>
                    <h4>Berita</h4>
                  </a>
                </div>
              </div>
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <i class="fas fa-swatchbook fa-3x"></i>
                  <h4>Rencana Kerja</h4>
                </div>
              </div>
              <div class="col-sm-3 text-center">
                <div class="container-fluid blue">
                  <a href="/admin">
                    <i class="fas fa-sitemap fa-3x"></i>
                    <h4>Struktur Organisasi</h4>
                </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>
<script>
import AdminMenu from '@/components/AdminPage/common/AdminMenu';
import ListTujuan from '@/components/AdminPage/ListTujuan';
import RiskForm from '@/components/AdminPage/RiskForm';
export default {
  props: ['page', 'id'],
  name: 'AdminHome',
  components: {
    AdminMenu,
    ListTujuan,
    RiskForm
  },
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
        }
    ],

    };
  },
};
</script>
<style type="text/css">
  .blue {
    color: #5da78f;
    width: 200px;
    height: 150px;
    border-style: dashed;
    border-color: #f2c888;
    padding-top: 15%;
  }
  .blue>a {
    color: #5da78f;
  }
  .container-table {
    min-width: 70%;
    margin-left: 15%;
    margin-right: 65%;
  }
</style>
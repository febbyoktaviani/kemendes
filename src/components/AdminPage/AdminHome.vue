<template>
  <div class="admin-home">
    <AdminMenu />
    <br/><br />
    <b-container v-if="$route.path == '/admin'">
      <b-row>
        <b-col>
          <b-card class="text-center"
                  border-variant="sand"
                  text-variant="boldtosca">
            <i class="fas fa-swatchbook fa-3x"></i>
            <h4>Rencana Kerja</h4>
          </b-card>
        </b-col>
        <b-col>
          <b-card class="text-center"
                  border-variant="sand"
                  text-variant="boldtosca">
            <i class="fas fa-volume-up fa-3x"></i>
            <h4>Berita</h4>
          </b-card>
        </b-col>
        <b-col>3 of 3</b-col>
        <b-col>4 of 4</b-col>
      </b-row>
    </b-container>
    <router-view></router-view>
  </div>
</template>
<script>
import AdminMenu from '@/components/AdminPage/common/AdminMenu';

export default {
  props: ['page', 'id'],
  name: 'AdminHome',
  components: {
    AdminMenu,
  },
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
  .border-sand {
    border-style: dashed;
    border-width: 0.5rem;
    border-color: #f2c888;
  }
  .container-table {
    min-width: 70%;
    margin-left: 15%;
    margin-right: 65%;
  }
  .bg-sand {
    background-color: #f3faf2;
  }
  .danger {
    color: #EB5A5F;
  }
  .danger>a:hover {
    color: red;
  }
  .green {
    color: #3ea76a;
  }
  .green>a:hover {
    color: green;
  }
  .ocean {
    color: #3a8ba2;
  }
  .ocean>a:hover {
    color: #0a6e8b;
  }
</style>

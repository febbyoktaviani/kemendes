<template>
  <div class="admin-home">
    <AdminMenu />
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
<template>
  <div class="admin-home">
    <AdminMenu/>
  </div>
</template>
<script>
import AdminMenu from '@/components/AdminPage/common/AdminMenu'
export default {
  name: 'AdminHome',
  components: {AdminMenu},
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
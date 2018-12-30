import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/WebPage/Home';
import AdminHome from '@/components/AdminPage/AdminHome';
// Rencana Kerja
import RencanaKerjaList from '@/components/AdminPage/RencanaKerja/RencanaKerjaList';
import RencanaKerjaDetail from '@/components/AdminPage/RencanaKerja/RencanaKerjaDetail';
import RencanaKerjaEdit from '@/components/AdminPage/RencanaKerja/RencanaKerjaEdit';
import RencanaKerjaAdd from '@/components/AdminPage/RencanaKerja/RencanaKerjaAdd';
// Berita
import BeritaList from '@/components/AdminPage/Berita/BeritaList';
import BeritaEdit from '@/components/AdminPage/Berita/BeritaEdit';
import BeritaAdd from '@/components/AdminPage/Berita/BeritaAdd';
// Unit Kerja
import UnitKerjaList from '@/components/AdminPage/UnitKerja/UnitKerjaList';
import UnitKerjaEdit from '@/components/AdminPage/UnitKerja/UnitKerjaEdit';
import UnitKerjaAdd from '@/components/AdminPage/UnitKerja/UnitKerjaAdd';
// User
import UserList from '@/components/AdminPage/User/UserList';
import UserAdd from '@/components/AdminPage/User/UserAdd';
import UserEdit from '@/components/AdminPage/User/UserEdit';
// Video
import VideoList from '@/components/AdminPage/Video/VideoList';
import VideoAdd from '@/components/AdminPage/Video/VideoAdd';
import VideoEdit from '@/components/AdminPage/Video/VideoEdit';
// Galery
import GaleryList from '@/components/AdminPage/Galery/GaleryList';
import GaleryEdit from '@/components/AdminPage/Galery/GaleryEdit';
import GaleryAdd from '@/components/AdminPage/Galery/GaleryAdd';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/admin',
      name: 'AdminHome',
      component: AdminHome,
      children: [
        {
          path: 'rencana-kerja/list',
          component: RencanaKerjaList,
        },
        {
          path: 'rencana-kerja/edit/:tujuanId',
          component: RencanaKerjaEdit,
          props: true,
        },
        {
          path: 'rencana-kerja/detail/:tujuanId',
          component: RencanaKerjaDetail,
          props: true,
        },
        {
          path: 'rencana-kerja/add',
          component: RencanaKerjaAdd,
          props: true,
        },
        // Beirta Route
        {
          path: 'berita/list',
          component: BeritaList,
        },
        {
          path: 'berita/edit/:beritaId',
          component: BeritaEdit,
          props: true,
        },
        {
          path: 'berita/add',
          component: BeritaAdd,
        },
        // Unit Kerja
        {
          path: 'unit-kerja/list',
          component: UnitKerjaList,
        },
        {
          path: 'unit-kerja/edit/:unitkerjaId',
          component: UnitKerjaEdit,
          props: true,
        },
        {
          path: 'unit-kerja/add',
          component: UnitKerjaAdd,
        },
        // User
        {
          path: 'user/list',
          component: UserList,
        },
        {
          path: 'user/edit/:userId',
          component: UserEdit,
          props: true,
        },
        {
          path: 'user/add',
          component: UserAdd,
        },
        // Video
        {
          path: 'video/list',
          component: VideoList,
        },
        {
          path: 'video/edit/:videoId',
          component: VideoEdit,
          props: true,
        },
        {
          path: 'video/add',
          component: VideoAdd,
        },
        // Galery
        {
          path: 'galery/list',
          component: GaleryList,
        },
        {
          path: 'galery/edit/:imageId',
          component: GaleryEdit,
          props: true,
        },
        {
          path: 'galery/add',
          component: GaleryAdd,
        },
      ],
    },
  ],
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next('/');
  }

  next();
});

export default router;

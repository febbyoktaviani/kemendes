import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/WebPage/Home';
import AdminHome from '@/components/AdminPage/AdminHome';
import RiskForm from '@/components/AdminPage/RiskForm';
import TujuanDetail from '@/components/AdminPage/TujuanDetail';
import ListTujuan from '@/components/AdminPage/ListTujuan';
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
          path: 'list-tujuan',
          component: ListTujuan
        },
        {
          path: 'riskform/:tujuanId',
          component: RiskForm,
          props: true,
        },
        {
          path: 'tujuan/:tujuanId',
          component: TujuanDetail,
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
      ]
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
})

export default router;

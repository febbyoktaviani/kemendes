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
        {
          path: 'berita/list',
          component: BeritaList,
        },
        {
          path: 'berita/edit/:beritaId',
          component: BeritaEdit,
          props: true,
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

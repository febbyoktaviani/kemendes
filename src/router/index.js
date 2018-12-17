import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import RiskForm from '@/components/admin/RiskForm';
import TujuanDetail from '@/components/admin/TujuanDetail';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/admin/riskform/:tujuanId',
      name: 'RiskForm',
      component: RiskForm,
      props: true
    },
    {
      path: '/admin/tujuan/:tujuanId',
      name: 'TujuanDetail',
      component: TujuanDetail,
      props: true,
    },
  ],
});

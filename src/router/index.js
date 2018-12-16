import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import RiskForm from '@/components/admin/RiskForm';
import TujuanForm from '@/components/admin/TujuanForm';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/admin/riskform',
      name: 'RiskForm',
      component: RiskForm,
    },
    {
      path: '/admin/tujuan/:tujuanId',
      name: 'TujuanForm',
      component: TujuanForm,
      props: true,
    },
  ],
});

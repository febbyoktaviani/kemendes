import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import RiskForm from '@/components/admin/RiskForm';

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
  ],
});

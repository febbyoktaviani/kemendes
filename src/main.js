// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import vSelect from 'vue-select';
import App from './App';
import Header from './components/WebPage/common/Header'
import store from './store';
import router from './router';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faCoffee,
         faDesktop,
         faClock,
         faGlobe,
         faHome,
         faCog,
         faPen,
         faLightbulb,
         faConciergeBell,
         faMapMaredAlt,
         faEnvelopO,
         faPhoneVolume } from '@fortawesome/free-solid-svg-icons';

library.add(faCoffee,
            faDesktop,
            faClock,
            faGlobe,
            faHome,
            faCog,
            faPen,
            faLightbulb,
            faConciergeBell);

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('v-select', vSelect);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>',
});

new Vue({
  el: '#header',
  store,
  router,
  components: { Header },
  template: '<Header/>',
});

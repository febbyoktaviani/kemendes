import Vue from 'vue';
import Vuex from 'vuex';
import RiskModule from './modules/risk';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    risk: RiskModule,
  },
});
import Vue from 'vue'
import Vuex from 'vuex'
import RiskModule from './modules/risk'
import UnitKerjaModule from './modules/unitkerja'
import AccountModule from './modules/account'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    risk: RiskModule,
    unitKerja: UnitKerjaModule,
    account: AccountModule,
  }
})

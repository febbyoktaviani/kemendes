import Vue from 'vue';
import Vuex from 'vuex';
import RiskModule from './modules/risk';
import UnitKerjaModule from './modules/unitkerja';
import AccountModule from './modules/account';
import BeritaModule from './modules/berita';
import UserModule from './modules/user';
import VideoModule from './modules/video';
import GaleryModule from './modules/galery';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    risk: RiskModule,
    unitKerja: UnitKerjaModule,
    account: AccountModule,
    berita: BeritaModule,
    user: UserModule,
    video: VideoModule,
    galery: GaleryModule
  },
});

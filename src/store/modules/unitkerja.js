import { getListUnitKerja, getUnitKerja, postUnitKerja, getTitlesUnitKerja } from '@/api/unitkerja';
import router from '@/router';

const state = {
  unitKerjaList: [],
  unitKerjaTitles: [],
  unitKerja: {},
  isUnitKerjaUploaded: false,
};

const mutations = {
  unitKerjaList(state, list) {
    state.unitKerjaList = list;
  },
  unitKerja(state, res) {
    state.unitKerja = res;
  },
  unitKerjaTitles(state, titles) {
    state.unitKerjaTitles = titles;
  },
  uploadUnitKerja(state, res) {
    state.isUploaded = true;
  },
};

const actions = {
  async fetchListUnitKerja(context) {
    const unitKerjaList = await getListUnitKerja();
    context.commit('unitKerjaList', unitKerjaList);
  },
  async fetchTitlesUnitKerja(context) {
    const unitKerjaTitles = await getTitlesUnitKerja();
    context.commit('unitKerjaTitles', unitKerjaTitles);
  },
  async fetchUnitKerja(context, unitkerja_id) {
    const res = await getUnitKerja(unitkerja_id);
    context.commit('unitKerja', res);
  },
  async uploadUnitKerja(context, formData) {
    const res = await postUnitKerja(formData);
    console.log('upload unitkerja', res);
    context.commit('uploadUnitKerja', res);
    router.push('/admin/unit-kerja/list');
  },
};

const getters = {
  unitKerjaList(state) {
    return state.unitKerjaList;
  },
  unitKerja(state) {
    return state.unitKerja;
  },
};

export default { state, mutations, actions, getters };

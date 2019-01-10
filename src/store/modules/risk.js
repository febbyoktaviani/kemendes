import { base_url, staticToken } from '../config';
import { getListRencanaKerja, getRencanaKerja, deleteRencanaKerja } from '@/api/rencanakerja';
import router from '@/router';

const state = {
  tujuan: { id: '', indikators: [{ kegiatans: [] }] },
  token: staticToken,
  riskFormList: [
    'sumber_resiko',
    'kategori_resiko',
    'resiko',
    'penyebab_resiko',
    'dampak_resiko',
    'pengendalian_uraian',
    'pengendalian_kategori',
    'resiko_residual',
    'pemilik_resiko',
    'kemungkinan',
    'dampak',
    'status_resiko',
    'level_resiko',
    'peringkat_resiko',
    'rtp',
    'penanggung_jawab',
    'target_waktu',
    'komunikasi',
    'rencana_pemantauan',
  ],
  kemungkinan_dropdown: [
    { text: 'Sangat jarang', value: 1 },
    { text: 'Jarang', value: 2 },
    { text: 'Kadang-kadang/ mungkin', value: 3 },
    { text: 'Hampir Pasti', value: 4 },
    { text: 'Pasti Terjadi/ sangat Sering', value: 5 },
  ],
  listTujuan: [],
  rkDeleted: false,
};

const actions = {
  async getTujuan({ commit }, tujuanId) {
    const res = await getRencanaKerja(tujuanId);
    commit('TUJUAN', res);
  },
  async getListTujuan({ commit }) {
    const res = await getListRencanaKerja();
    commit('LIST_TUJUAN', res);
  },
  async removeRencanaKerja(context, tujuanId) {
    const res = await deleteRencanaKerja(tujuanId);
    context.commit('DELETE_RENCANA_KERJA', res)
    router.go()
  }
};

const mutations = {
  TUJUAN: (state, res) => {
    state.tujuan = res;
  },
  LIST_TUJUAN: (state, res) => {
    state.listTujuan = JSON.parse(res);
  },
  DELETE_RENCANA_KERJA: (state, res) => {
    router.go()
  } 
};

const getters = {
  tujuan(state) {
    return state.tujuan;
  },
  riskFormList(state) {
    return state.riskFormList;
  },
  listTujuan(state) {
    return state.listTujuan;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};

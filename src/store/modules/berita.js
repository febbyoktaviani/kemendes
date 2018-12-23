import { getListBerita, getBerita, postBerita } from '@/api/berita';


const state = {
  listBerita: [],
  berita: {},
  is_uploaded: false,
}

const mutations = {
  LIST_BERITA: (state, res) => {
    state.listBerita = res;
  },
  GET_BERITA: (state, res) => {
    state.berita = res;
  },
  UPLOAD_BERITA: (state, res) => {
    state.is_uploaded = true;
  }
}

const actions = {
  async fetchListBerita({ commit }) {
    let res = await getListBerita()
    commit('LIST_BERITA', res)
  },
  async fetchBerita({ commit }, berita_id) {
    let res = await getBerita(berita_id)
    console.log('berita', res)
    commit('GET_BERITA', res)
  },
  async uploadBerita(context, formData) {
    let res = await postBerita(formData)
    console.log('upload berita', res)
    context.commit('UPLOAD_BERITA', res)
  },
}

const getters = {
    listBerita(state){
        console.log('getters', state.listBerita)
        return state.listBerita
    },
    berita(state) {
        return state.berita
    },
    isUploaded(state) {
        return state.is_uploaded
    },
}

export default { state, mutations, actions, getters }

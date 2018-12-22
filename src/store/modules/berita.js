import { getListBerita, getBerita } from '@/api/berita';


const state = {
  listBerita: [],
  berita: {},
}

const mutations = {
  LIST_BERITA: (state, res) => {
    state.listBerita = res;
  },
  GET_BERITA: (state, res) => {
    state.berita = res;
  },
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
  }
}

const getters = {
    listBerita(state){
        console.log('getters', state.listBerita)
        return state.listBerita
    },
    berita(state) {
        return state.berita
    }
}

export default { state, mutations, actions, getters }

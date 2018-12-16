import { base_url, staticToken } from '../config'

const state = {
  tujuan: {},
  token: staticToken
}

const actions = {
  getTujuan: async function({ commit }, tujuanId) {
    console.log('url', base_url)
    let header = new Headers({
      Authorization: `Bearer ${state.token}`,
      Accept: 'application/json',
      'Access-Control-Allow-Origin': '*',
      mode: 'no-cors'
    })
    const opt = {
      method: 'GET',
      headers: header
    }

    const res = await fetch(
      `${base_url}/rencana-kerja/?tujuan_id=${tujuanId}`,
      opt
    ).then(response => response.json())
    commit('TUJUAN', res)
  }
}

const mutations = {
  TUJUAN: (state, res) => {
    state.tujuan = res
  }
}

const getters = {
  tujuan: function(state) {
    return state.tujuan
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}

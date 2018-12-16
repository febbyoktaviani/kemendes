import base_url from '../config';

const state = {
    tujuan: {},
    token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzY0NzczMjEsImlkZW50aXR5IjoiYWRtaW4iLCJpYXQiOjE1NDQ5NDEzMjEsImp0aSI6ImQzNTkyODQ0LWY4ODItNDNiMS1hMDcwLWQ2NzdlNGViZjdhMiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU0NDk0MTMyMX0.9zqJWoO7Fq9QOCzpvySDsLnGOVSlcwc4DxLR1s2wfLY'
}

const actions = {
    getTujuan: async function({ commit }, tujuanId) {
        console.log('url', base_url)
        let header = new Headers({
            'Authorization': `Bearer ${state.token}`,
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'mode': 'no-cors'
        });
        const opt = {
            method:'GET',
            headers: header
        };

        const res = await fetch(`${base_url}/rencana-kerja/?tujuan_id=${tujuanId}`,
            opt).then((response) => response.json());
        commit('TUJUAN', res);  
    },
}

const mutations = {
  TUJUAN: (state, res) => {
    state.tujuan = res;
  },
}


const getters = {
    tujuan : function (state) {
        return state.tujuan
    },
}

export default {
  state,
  getters,
  actions,
  mutations,
}

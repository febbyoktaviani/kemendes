import base_url from '../config';

const state = {
    tujuan: {},
    token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzY0NzczMjEsImlkZW50aXR5IjoiYWRtaW4iLCJpYXQiOjE1NDQ5NDEzMjEsImp0aSI6ImQzNTkyODQ0LWY4ODItNDNiMS1hMDcwLWQ2NzdlNGViZjdhMiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU0NDk0MTMyMX0.9zqJWoO7Fq9QOCzpvySDsLnGOVSlcwc4DxLR1s2wfLY',
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
        "kemungkinan",
        "dampak",
        "status_resiko",
        "level_resiko",
        "peringkat_resiko",
        'rtp',
        'penanggung_jawab',
        'target_waktu',
        'komunikasi',
        'rencana pemantauan'
    ],
    kemungkinan_dropdown: [
        {'text': 'Sangat jarang', 'value': 1},
        {'text': 'Jarang', 'value': 2 },
        {'text': 'Kadang-kadang/ mungkin', 'value': 3},
        {'text': 'Hampir Pasti', 'value': 4},
        {'text': 'Pasti Terjadi/ sangat Sering', 'value': 5}
    ]
}

const actions = {
    getTujuan: async function({ commit }, tujuanId) {
        console.log('url', base_url)
        let header = new Headers({
            // 'Authorization': `Bearer ${state.token}`,
            'Accept': 'application/json'
        });

        const opt = {
            method:'GET',
            headers: header
        };

        const res = await fetch(`${base_url}/rencana-kerja?tujuan_id=${tujuanId}`,
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
    riskFormList: function (state) {
        return state.riskFormList
    }
}

export default {
  state,
  getters,
  actions,
  mutations,
}

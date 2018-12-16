import { getUnitKerjas } from '@/api/unitkerja'

const state = {
  unitKerjaList: []
}

const mutations = {
  unitKerjaList(state, list) {
    state.unitKerjaList = list
  }
}

const actions = {
  async fetchUnitKerjaList(context) {
    let unitKerjaList = await getUnitKerjas()
    context.commit('unitKerjaList', unitKerjaList)
  }
}

export default { state, mutations, actions }

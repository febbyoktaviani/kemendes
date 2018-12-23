import { getListUser, getUser, postUser } from '@/api/user'
import router from '@/router';

const state = {
    listUser: [],
}

const mutations = {
  listUser: (state, res) => {
    state.listUser = res;
  },
}

const actions = {
  async fetchListUser(context) {
    let res = await getListUser()
    context.commit('listUser', res)
  },
}

const getters = {
    listUser(state){
        return state.listUser
    },
}

export default { state, mutations, actions, getters }
import { getListUser, getUser, postUser } from '@/api/user'
import router from '@/router';

const state = {
    listUser: [],
    userData: {}
}

const mutations = {
  listUser: (state, res) => {
    state.listUser = res;
  },
  user: (state, res) => {
    state.userData = res
  }
}

const actions = {
  async fetchListUser(context) {
    let res = await getListUser()
    context.commit('listUser', res)
  },
  async fetchUser(context, user_id) {
    let res = await getUser(user_id)
    context.commit('user', res)
  },
}

const getters = {
    listUser(state){
        return state.listUser
    },
    userData(state) {
        return state.userData
    }
}

export default { state, mutations, actions, getters }
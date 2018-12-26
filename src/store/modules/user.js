import { getListUser, getUser, postUser, getListRole } from '@/api/user'
import router from '@/router';

const state = {
    listUser: [],
    userData: {},
    listRole: [],
}

const mutations = {
  listUser: (state, res) => {
    state.listUser = res;
  },
  user: (state, res) => {
    state.userData = res
  },
  listRole: (state, res) => {
    state.listRole = res
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
  async fetchListRole(context) {
    let res = await getListRole()
    context.commit('listRole', res)
  },
  async createUser(context, formData) {
    let res = await postUser(formData)
    // context.commit('user', res)
  }
}

const getters = {
    listUser(state){
        return state.listUser
    },
    userData(state) {
        return state.userData
    },
    listRole(state) {
        return state.listRole
    }
}

export default { state, mutations, actions, getters }
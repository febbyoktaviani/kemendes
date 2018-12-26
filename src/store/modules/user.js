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
    if (res.role) {
        res.role = res.role.$oid
    }
    state.userData = res
  },
  listRole: (state, res) => {
    let optRole = []
    for (const role of res) {
        optRole.push({'value': role._id.$oid, 'text': role.name})
    }
    state.listRole = optRole
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
    context.commit('user', res)
    router.push('/admin/user/list')
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
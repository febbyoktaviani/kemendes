import { base_url } from '../config';
import router from '@/router';

const user = JSON.parse(localStorage.getItem('user'));
const state = user
  ? { status: { loggedIn: true }, user }
  : { status: {}, user: null };

const actions = {
  async login({ commit }, userdata) {
    console.log('login-data', userdata);
    const header = new Headers({
      // 'Authorization': `Bearer ${state.token}`,
      Accept: 'application/json',
    });

    const opt = {
      method: 'POST',
      headers: header,
      body: JSON.stringify(userdata),
    };

    const res = await fetch(
      `${base_url}/user/login`,
      opt,
    ).then(response => response.json());
    commit('loginSuccess', res);
    localStorage.setItem('user', JSON.stringify(res));
    router.push('/admin');
  },
  logout({ commit }) {
    localStorage.setItem('user', null);
    commit('logout');
    router.push('/');
  },
};

const mutations = {
  loginRequest(state, user) {
    state.status = { loggingIn: true };
    state.user = user;
  },
  loginSuccess(state, user) {
    state.status = { loggedIn: true };
    state.user = user;
  },
  loginFailure(state) {
    state.status = {};
    state.user = null;
  },
  logout(state) {
    state.status = {};
    state.user = null;
  },
};

const getters = {
  user(state) {
    return state.user;
  },
};

const AccountModule = {
  state,
  actions,
  getters,
  mutations,
};

export default AccountModule;

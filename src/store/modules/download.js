import { getListDownload, getDownload, postDownload, deleteDownload } from '@/api/download';
import router from '@/router';

const state = {
  listDownload: [],
  download: {},
};

const mutations = {
  listDownload: (state, res) => {
    state.listDownload = res;
  },
  download: (state, res) => {
    state.galery = res;
  },
};

const actions = {
  async fetchListDownload(context) {
    const res = await getListDownload();
    context.commit('listDownload', res);
  },
  async fetchDownload(context, document_id) {
    const res = await getDownload(document_id);
    context.commit('download', res);
  },
  async uploadDownload(context, formData) {
    const res = await postDownload(formData);
    // context.commit('isVideoUploaded', res)
    router.push('/admin/download/list');
  },
  async removeDownload(context, document_id) {
    const res = await deleteDownload(document_id);
  }
};

const getters = {
  listDownload(state) {
    return state.listDownload;
  },
  download(state) {
    return state.download;
  },
};

export default { state, mutations, actions, getters };

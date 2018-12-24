import { getListVideo, getVideo, postVideo } from '@/api/video';
import router from '@/router';

const state = {
    listVideo: [],
    video: {},
}

const mutations = {
  listVideo: (state, res) => {
    state.listVideo = res;
  },
  video: (state, res) => {
    state.video = res
  },
}

const actions = {
  async fetchListVideo(context) {
    let res = await getListVideo()
    context.commit('listVideo', res)
  },
  async fetchVideo(context, user_id) {
    let res = await getVideo(user_id)
    context.commit('video', res)
  },
  async fetchVideo(context, formData) {
    let res = await postVideo(formData)
    context.commit('isVideoUploaded', res)
    router.push('/admin/video/list')
  },
}

const getters = {
    listVideo(state){
        return state.listVideo
    },
    video(state) {
        return state.video
    },
}

export default { state, mutations, actions, getters }
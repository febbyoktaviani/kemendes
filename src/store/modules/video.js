import { getListVideo, getVideo, postVideo, deleteVideo } from '@/api/video';
import router from '@/router';

const state = {
  listVideo: [],
  video: {},
};

const mutations = {
  listVideo: (state, res) => {
    state.listVideo = res;
  },
  video: (state, res) => {
    state.video = res;
  },
};

const actions = {
  async fetchListVideo(context) {
    const res = await getListVideo();
    context.commit('listVideo', res);
  },
  async fetchVideo(context, video_id) {
    const res = await getVideo(video_id);
    context.commit('video', res);
  },
  async uploadVideo(context, formData) {
    const res = await postVideo(formData);
    // context.commit('isVideoUploaded', res)
    router.push('/admin/video/list');
  },
  async removeVideo(context, video_id) {
    const res = await deleteVideo(video_id)
    router.go()
  }
};

const getters = {
  listVideo(state) {
    return state.listVideo;
  },
  video(state) {
    return state.video;
  },
};

export default { state, mutations, actions, getters };

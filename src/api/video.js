import api from './index';

const getListVideo = async function () {
  const { data: ListVideo } = await api.get('/list-video');
  return ListVideo;
};

const getVideo = async function (video_id) {
  const { data: video } = await api.get(`/video/${video_id}`);
  return video;
};

const postVideo = async function (formData) {
  alert(formData);
  const { data: video } = await api.post('post-video', formData);
  alert(video);
  return video;
};


export { getListVideo, getVideo, postVideo };

import api from './index'

const getListVideo = async function() {
    let { data: ListVideo } = await api.get('/list-video')
    return ListVideo
  }

const getVideo = async function(video_id) {
    let { data: video } = await api.get(`/video/${video_id}`)
    return video
  }

const postVideo = async function(formData) {
    let { data: video } = await api.post('post-video', formData)
    return video
  }


export { getListVideo, getVideo, postVideo }
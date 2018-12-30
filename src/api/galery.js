import api from './index';

const getListGalery = async function() {
    let { data: ListGalery } = await api.get('/list-image')
    return ListGalery
  }

const getGalery = async function(image_id) {
    let { data: galery } = await api.get(`/image/${image_id}`)
    return galery
  }

const postGalery = async function(formData) {
    let { data: galery } = await api.post('post-image', formData)
    return galery
  }


export { getListGalery, getGalery, postGalery }
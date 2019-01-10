import api from './index';
import router from '@/router';

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

const deleteGalery = async function (image_id) {
  const response = await api.put(`/delete-image/${image_id}`);
  console.log('delete-image', response)
  if (response.status == 204) {
    console.log(router)
    router.go();
  }
};


export { getListGalery, getGalery, postGalery, deleteGalery }
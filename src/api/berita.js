import api from './index'

const getListBerita = async function() {
    console.log('api', api)
    let { data: ListBerita } = await api.get('/list-berita')
        console.log('api berita', ListBerita)
    return ListBerita
  }

const getBerita = async function(berita_id) {
    console.log('api', berita_id)
    let { data: berita } = await api.get(`/berita/${berita_id}`)
        console.log('api berita', berita)
    return berita
  }

const postBerita = async function(formData) {
    console.log('api post berita', formData)
    let { data: berita } = await api.post('post-berita', formData)
        console.log('api berita', berita)
    return berita
  }

export { getListBerita, getBerita, postBerita }
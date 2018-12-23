import api from './index'


const getUnitKerjas = async function() {
    let { data: unitKerjas } = await api.get('/list-unitkerja')
    return unitKerjas
}

const getUnitKerja = async function(unitkerja_id) {
    let { data: unitKerja } = await api.get(`/unitkerja/${unitkerja_id}`)
    return unitKerja
  }

const postUnitKerja = async function(formData) {
    let { data: unitKerja } = await api.post('post-unitkerja', formData)
        console.log('api unitkerja', unitKerja)
    return unitKerja
  }


export { getUnitKerjas, postUnitKerja, getUnitKerja }


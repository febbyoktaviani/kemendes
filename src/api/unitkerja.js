import swal from 'sweetalert';
import api from './index';
import router from '@/router';


const getUnitKerjas = async function() {
    let { data: unitKerjas } = await api.get('/list-unitkerja')
    return unitKerjas
}

const getUnitKerja = async function(unitkerja_id) {
    try {
        let { data: unitKerja } = await api.get(`/unitkerja/${unitkerja_id}`)
        return unitKerja
    } catch(error) {
        swal({
            title: "Not Found Error!",
            text: "Unit Kerja Not Found!",
            icon: "error"
        }).then(router.push('/admin/unit-kerja/list'))
    }
  }

const postUnitKerja = async function(formData) {
    try {
        let { data: unitKerja } = await api.post('post-unitkerja', formData)
            console.log('api unitkerja', unitKerja)
        return unitKerja
    } catch(error) {
        swal({
            title: "Error Saving Unit Kerja",
            text: error,
            icon: "error"
        })
    }
  }


export { getUnitKerjas, postUnitKerja, getUnitKerja }


import swal from 'sweetalert';
import api from './index'

const getListUser = async function() {
    let { data: ListUser } = await api.get('/list-user')
    return ListUser
  }

const getUser = async function(user_id) {
    let { data: user } = await api.get(`/user/${user_id}`)
    return user
  }

const postUser = async function(formData) {
    try {
        let { data: user } = await api.post('post-user', formData)
        return user
    }  catch(error) {
        swal({
            title: "Error Saving User",
            text: error,
            icon: "error",
            button: "OK"
        })
    }
  }

const getListRole = async function() {
    let { data: ListRole } = await api.get('/list-role')
    return ListRole
  }

export { getListUser, getUser, postUser, getListRole }
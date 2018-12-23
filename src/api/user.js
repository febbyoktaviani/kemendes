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
    let { data: user } = await api.post('post-user', formData)
    return user
  }

export { getListUser, getUser, postUser }
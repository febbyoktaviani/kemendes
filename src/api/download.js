import api from './index';

const getListDownload = async function() {
    let { data: ListDownload } = await api.get('/list-download')
    return ListDownload
  }

const getDownload = async function(document_id) {
    let { data: downloadFile } = await api.get(`/download/${document_id}`)
    return downloadFile
  }

const postDownload = async function(formData) {
    let { data: download } = await api.post('post-download', formData)
    return download
  }

const deleteDownload = async function (document_id) {
  const { data: message } = await api.put(`/delete-unitkerja/${document_id}`);
  return message;
};


export { getListDownload, getDownload, postDownload, deleteDownload }
import api from './index';

const getListRencanaKerja = async function () {
  console.log('api', api);
  const { data: ListRencanaKerja } = await api.get('/list-rencana-kerja');
  console.log('api rencan kerja', ListRencanaKerja);
  return ListRencanaKerja;
};

const getRencanaKerja = async function (tujuan_id) {
  const { data: rencanaKerja } = await api.get(`/rencana-kerja?tujuan_id=${tujuan_id}`);
  return rencanaKerja;
};

const deleteRencanaKerja = async function (tujuan_id) {
  const { data: message } = await api.put(`/delete-rencana-kerja/${tujuan_id}`);
  return message;
};

export { getListRencanaKerja, getRencanaKerja, deleteRencanaKerja };

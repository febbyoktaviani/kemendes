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

const postBerita = async function (formData) {
  console.log('api post berita', formData);
  const { data: berita } = await api.post('post-berita', formData);
  console.log('api berita', berita);
  return berita;
};

export { getListRencanaKerja, getRencanaKerja, postBerita };

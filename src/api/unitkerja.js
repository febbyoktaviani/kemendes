import api from './index'

export default {
  async getUnitKerja() {
    let { data: unitKerjas } = await api.get('/unitkerja')
    return unitKerjas
  }
}

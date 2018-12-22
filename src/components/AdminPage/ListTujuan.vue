<template>
  <div class="list-tujuan">
    <div class="container text-left">    
      <br>
      <div class="row">
        <div class="col-sm-12 linkapp-container">
          <div class="container text-left">    
            <br>
            <div class="row">
              <div class="col-sm-12 linkapp-container">
                <div class="panel panel-success">
                  <!-- Content Here -->
                  <div class="panel-heading">
                    <h3> List Tujuan </h3>
                  </div>
                  <div class="panel-body">
                    <button class="btn-success">
                      Add <i class="fas fa-plus-circle fa-lg"></i>
                    </button>
                    <br/><br>
                    <div class="table-responsive">
                      <table class="table">
                        <thead>
                          <tr class="success text-left">
                            <th>Tujuan</th>
                            <th>Unit Pemilik Resiko</th>
                            <th>Unit Eselon III/IV</th>
                            <th>Periode</th>
                            <th>Kegiatan</th>
                            <th></th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="tujuan in ListTujuan">
                            <td>{{ tujuan.name }}</td>
                            <td>{{ tujuan.unit_pemilik_resiko }}</td>
                            <td>{{ tujuan.unit_eselon }}</td>
                            <td>{{ tujuan.periode }}</td>
                            <td>{{ tujuan.kegiatan }}</td>
                            <td>
                              <a :href="'/#/admin/tujuan/'+tujuan._id.$oid">
                                <i class="far fa-eye fa-lg"></i>
                              </a>
                              &nbsp;&nbsp;
                              <a :href="'/#/admin/riskForm/'+tujuan._id.$oid">
                                <i class="fas fa-edit fa-lg"></i>
                              </a>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex';
  export default {
      props: [],
      components: {},
      name: 'ListTujuan',
      data() {
        return {
        };
      },
      created() {
          this.$store.dispatch('getListTujuan');
          console.log('list-tujuan');
      },
      methods: {

      },
      computed: {
        ...mapGetters({
          ListTujuan: 'listTujuan',
        })
    },
  };
</script>
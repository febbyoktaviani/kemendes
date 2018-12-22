<template>
  <div class="berita-list">
    <div class="container-table">
      <div class="container text-left">    
        <br>
        <div class="row">
          <div class="col-sm-12 linkapp-container">
            <div class="panel panel-success">
              <!-- Content Here -->
              <div class="panel-heading">
                <h3> List Berita </h3>
              </div>
              <div class="panel-body">
                <a href="/admin/berita/add">
                  Add <i class="fas fa-plus-circle fa-lg"></i>
                </a>
                <br/><br>
                <div class="table-responsive">
                  <table class="table">
                    <thead>
                      <tr class="success text-left">
                        <th>Judul</th>
                        <th>Created at</th>
                        <th></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="berita in listBerita">
                        <td>{{ berita.title }}</td>
                        <td>{{ toDate(berita.created_at.$date) }}</td>
                        <td>
                          <a :href="'/admin/tujuan/'">
                            <i class="far fa-eye fa-lg"></i>
                          </a>
                          &nbsp;&nbsp;
                          <a :href="'/admin/riskForm/'">
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
</template>
<script>
  import { mapGetters, mapActions } from 'vuex';
  export default {
      props: [],
      name: 'BeritaList',
      data() {
        return {
        };
      },
      created() {
        this.$store.dispatch('fetchListBerita');
        // console.log('list-berita');
      },
      methods: {
        toDate(ms) {
          const date = new Date(ms)
          const date_str = `${date.getDate()}-${date.getMonth()}-${date.getFullYear()}`
          const time_str = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
          // return date
          return `${date_str} ${time_str}`
        }

      },
      computed: {
        ...mapGetters({
          listBerita: 'listBerita',
        })
    },
  };
</script>
<style type="text/css">
  .container-table {
    min-width: 90%;
    margin-left: 5%;
    margin-right: 95%;
  }
</style>
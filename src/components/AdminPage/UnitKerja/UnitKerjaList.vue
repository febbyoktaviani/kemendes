<template>
  <div class="unit-kerja-list">
    <b-container fluid>
      <b-card bg-variant="sand"
              text-variant="black"
              title="List Unit Kerja"
              class="text-left">
        
        <a href="/admin/unit-kerja/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-table striped hover :fields="fields" :items="listUnitKerja">
          <template slot="created_at" slot-scope="data">
            {{ toDate(data.item.created_at.$date) }}
          </template>
          <template slot="action" slot-scope="data">
            <a :href="'/admin/unit-kerja/edit/'+data.item._id.$oid">
              <i class="fas fa-edit fa-lg"></i>
            </a>
          </template>
        </b-table>
      </b-card>
    </b-container>
  </div>
</template>
<script>
  import { mapGetters, mapActions } from 'vuex';
  export default {
      props: [],
      name: 'UnitKerjaList',
      data() {
        return {
          fields: [
            {
              key: 'name',
              label: 'Unit Kerja'
            },
            {
              key: 'created_at',
              label: 'Created At'
            },{
              key: 'action',
              label: 'Action'
            }
          ]
        };
      },
      created() {
        this.$store.dispatch('fetchUnitKerjaList');
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
          listUnitKerja: 'unitKerjaList',
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
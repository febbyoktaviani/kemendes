<template>
  <div class="rencana-kerja-list">
    <b-container fluid>
      <b-card bg-variant="sand"
              text-variant="brown"
              title="List Tujuan"
              class="text-left">
        <a href="/admin/rencana-kerja/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-table striped hover :fields="fields" :items="ListTujuan">
          <template slot="action" slot-scope="data">
            <a :href="'/admin/rencana-kerja/detail/'+data.item._id.$oid">
              <i class="far fa-eye fa-lg"></i>
            </a>
            &nbsp;&nbsp;
            <a :href="'/admin/rencana-kerja/edit/'+data.item._id.$oid">
              <i class="fas fa-edit fa-lg"></i>
            </a>
          </template>
        </b-table>
      </b-card>
    </b-container>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex';
  export default {
      props: [],
      name: 'RencanaKerjaList',
      data() {
        return {
          fields: [
            'name',
            'unit_pemilik_resiko',
            'unit_eselon',
            'periode',
            'kegiatan',
            {
              key: 'action',
              lable: 'Actions'
            }
          ]
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
<style type="text/css">
  .container-table {
    min-width: 90%;
    margin-left: 5%;
    margin-right: 95%;
  }
  .bg-sand {
    background-color: #f3faf2;
  }
  .text-greenbold {
    color: #003300;
  }
</style>
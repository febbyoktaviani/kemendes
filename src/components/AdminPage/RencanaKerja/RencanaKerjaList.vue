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
        <b-table striped
                 responsive
                 hover
                 :fields="fields"
                 :items="ListTujuan"
                 :current-page="currentPage"
                 :small="true"
                 :per-page="perPage">
          <template slot="action" slot-scope="data">
            <b-row>
              <b-col :cols="2" class="ocean">
                <a :href="'/admin/rencana-kerja/detail/'+data.item._id.$oid"
                   class="ocean"
                   v-b-tooltip.hover title="detail">
                  <i class="far fa-eye fa-lg"></i>
                </a>
              </b-col>
              <b-col :cols="2" class="green">
                <a :href="'/admin/rencana-kerja/edit/'+data.item._id.$oid"
                   class="green"
                   v-b-tooltip.hover title="edit">
                  <i class="fas fa-edit fa-lg"></i>
                </a>
              </b-col>
              <b-col :cols="2" class="danger">
                <a href="#"
                   class="danger"
                   v-b-tooltip.hover title="delete"
                   v-on:click="onModalDelete(data.item._id.$oid)">
                  <i class="fas fa-trash-alt fa-lg"></i>
                </a>
              </b-col>
            </b-row>
          </template>
        </b-table>
        <b-pagination :total-rows="ListTujuan.length" align="center" v-model="currentPage" :per-page="perPage"></b-pagination>
      </b-card>
      <b-modal ref="modalDelete" hide-footer title="Delete Image" warning>
        <div class="d-block text-center">
          <h3>Are you sure want to delete this image?</h3>
        </div>
        <b-btn class="mt-3" variant="outline-success" block @click="onDelete()">Confirm
        </b-btn>
      </b-modal>
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
      currentPage: 1,
      perPage: 20,
      deleteId: null,
      fields: [
        'name',
        'unit_pemilik_resiko',
        'unit_eselon',
        'periode',
        'kegiatan',
        {
          key: 'action',
          lable: 'Actions',
        },
      ],
    };
  },
  created() {
    this.$store.dispatch('getListTujuan');
    console.log('list-tujuan');
  },
  methods: {
    onModalDelete(deleteId) {
      this.deleteId = deleteId
      this.$refs.modalDelete.show()
    },
    onDelete() {
      this.$store.dispatch('removeRencanaKerja', this.deleteId)
      this.deleteId = null;
      this.$refs.modalDelete.hide()
    },
  },
  computed: {
    ...mapGetters({
      ListTujuan: 'listTujuan',
    }),
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

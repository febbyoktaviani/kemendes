<template>
  <div class="berita-list">
    <b-container fluid>
      <b-card bg-variant="sand"
              text-variant="black"
              title="List Berita"
              class="text-left">
        <a href="/admin/berita/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-table striped
                 hover
                 :fields="fields"
                 :items="listBerita"
                 :current-page="currentPage"
                 :per-page="perPage"
                 :small="true">
          <template slot="created_at" slot-scope="data">
            {{ toDate(data.item.created_at.$date) }}
          </template>
          <template slot="action" slot-scope="data">
            <b-row>
              <b-col :cols="1" class="green">
                <a :href="'/admin/berita/edit/'+data.item._id.$oid"
                   class="green"
                   v-b-tooltip.hover title="edit">
                  <i class="fas fa-edit fa-lg"></i>
                </a>
              </b-col>
              <b-col :cols="1" class="danger">
                <a href='#'
                   class="danger"
                   v-b-tooltip.hover title="delete"
                   v-on:click="onModalDelete(data.item._id.$oid)">
                  <i class="fas fa-trash-alt fa-lg"></i>
                </a>
              </b-col>
            </b-row>
          </template>
        </b-table>
        <b-pagination :total-rows="listBerita.length" align="center" v-model="currentPage" :per-page="perPage">
        </b-pagination>
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
import { mapGetters, mapActions } from 'vuex';

export default {
  props: [],
  name: 'BeritaList',
  data() {
    return {
      currentPage: 1,
      perPage: 20,
      deleteId: null,
      fields: [
        {
          key: 'title',
          label: 'Judul',
        },
        {
          key: 'created_at',
          label: 'Created At',
        }, {
          key: 'action',
          label: 'Action',
        },
      ],
    };
  },
  created() {
    this.$store.dispatch('fetchListBerita');
    // console.log('list-berita');
  },
  methods: {
    toDate(ms) {
      const date = new Date(ms);
      const date_str = `${date.getDate()}-${date.getMonth()}-${date.getFullYear()}`;
      const time_str = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
      // return date
      return `${date_str} ${time_str}`;
    },
    onModalDelete(deleteId) {
      this.deleteId = deleteId
      this.$refs.modalDelete.show()
    },
    onDelete() {
      this.$store.dispatch('removeBerita', this.deleteId)
      this.deleteId = null;
      this.$refs.modalDelete.hide()
    },
  },
  computed: {
    ...mapGetters({
      listBerita: 'listBerita',
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
  .aqua {
    background-color: #5da78f;
  }
</style>

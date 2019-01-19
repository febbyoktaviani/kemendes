<template>
  <div class="download-list">
    <b-container fluid>
      <b-card bg-variant="sand"
            text-variant="black"
            title="List Download"
            class="text-left">

        <a href="/admin/download/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-row>
          <b-table striped
                 responsive
                 hover
                 :fields="fields"
                 :items="listDownload"
                 :current-page="currentPage"
                 :small="true"
                 :per-page="perPage">
            <template slot="action" slot-scope="data">
              <b-dropdown right>
                <b-dropdown-item>
                  <a :href="'/admin/download/edit/'+data.item._id.$oid"
                    class="green">
                    <i class="fas fa-edit fa-lg"></i>
                    Edit
                  </a>
                </b-dropdown-item>
                <b-dropdown-item>
                  <a href="#"
                    class="danger"
                    v-on:click="onModalDelete(data.item._id.$oid)">
                    <i class="fas fa-trash-alt fa-lg"></i>
                    Hapus
                  </a>
              </b-dropdown-item>
            </b-dropdown>
            </template>
          </b-table>
        </b-row>
        <b-pagination :total-rows="listDownload.length"
                        align="center"
                        v-model="currentPage"
                        :per-page="perPage"></b-pagination>
      </b-card>
      <b-modal ref="modalDelete" hide-footer :title="'Hapus '+pageTitle" warning>
        <div class="d-block text-center">
          <h3>Apakah Anda yakin akan menghapus {{pageTitle}} ini?</h3>
        </div>
        <b-btn class="mt-3" variant="outline-success" block @click="onDelete()">Confirm
        </b-btn>
      </b-modal>
    </b-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import { getImageUrl } from '@/helpers/util';
export default {
  name: 'DownloadList',
  data() {
    return {
      pageTitle: "Dokumen",
      currentPage: 1,
      perPage: 20,
      deleteId: null,
      fields: [
        {
          key: 'name',
          label: 'Name',
        },
        {
          key: 'description',
          label: 'Description',
        }, {
          key: 'doc_url',
          label: 'Download Url',
        },
      ],
    };
  },
  created() {
    this.$store.dispatch('fetchListDownload')
  },
  computed: {
    ...mapGetters({
      listDownload: 'listDownload'
    })
    
  },
  methods: {
    onFileChanged(event) {
      const file = event.target.files[0]
      this.image = file
      console.log(file)
    },
    getImageUrl(image) {
      return getImageUrl(image)
    },
    onModalDelete(downloadId) {
      this.deleteId = downloadId
      this.$refs.modalDelete.show()
    },
    onDelete() {
      this.$store.dispatch('removeDownload', this.deleteId);
      this.deleteId = null;
      this.$refs.modalDelete.hide();
    },
  },
};
</script>
<style>
</style>
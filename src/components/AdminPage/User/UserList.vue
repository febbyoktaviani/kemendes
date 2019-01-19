<template>
  <div class="user-list">
    <b-container fluid>
      <b-card bg-variant="sand"
              text-variant="black"
              title="List User"
              class="text-left"
              :current-page="currentPage"
              :per-page="perPage"
              :small="true">

        <a href="/admin/user/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-table striped hover :fields="fields" :items="listUser">
          <template slot="role" slot-scope="data">
            {{ data.item.role ? data.item.role.name : '-' }}
          </template>
          <template slot="action" slot-scope="data">
            <b-dropdown right>
              <b-dropdown-item>
                <a :href="'/admin/user/edit/'+data.item._id.$oid"
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
        <b-pagination :total-rows="listUser.length"
                      align="center"
                      v-model="currentPage"
                      :per-page="perPage">
        </b-pagination>
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
import { mapGetters, mapActions } from 'vuex';

export default {
  props: [],
  name: 'UserList',
  data() {
    return {
      pageTitle: "User",
      currentPage: 1,
      perPage: 20,
      deleteId: null,
      fields: [
        {
          key: 'username',
          label: 'Username',
        },
        {
          key: 'email',
          label: 'Email',
        },
        {
          key: 'role',
          label: 'Role',
        },
        {
          key: 'action',
          label: 'Actions',
        },
      ],
    };
  },
  created() {
    this.$store.dispatch('fetchListUser');
    // console.log('list-berita');
  },
  methods: {
    onModalDelete(deleteId) {
      this.deleteId = deleteId
      this.$refs.modalDelete.show()
    },
    onDelete() {
      alert(this.deleteId)
      this.deleteId = null;
      this.$refs.modalDelete.hide()
    },
  },
  computed: {
    ...mapGetters({
      listUser: 'listUser',
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

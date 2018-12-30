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
            <a :href="'/admin/user/edit/'+data.item._id.$oid">
              <i class="fas fa-edit fa-lg"></i>
            </a>
          </template>
        </b-table>
        <b-pagination :total-rows="listUser.length"
                      align="center"
                      v-model="currentPage"
                      :per-page="perPage">
        </b-pagination>
      </b-card>
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
      currentPage: 1,
      perPage: 20,
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

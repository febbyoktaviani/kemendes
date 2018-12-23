<template>
  <div class="user-list">
    <div class="container-table">
      <div class="container text-left">    
        <br>
        <div class="row">
          <div class="col-sm-12 linkapp-container">
            <div class="panel panel-success">
              <!-- Content Here -->
              <div class="aqua panel-heading">
                <h3> List User </h3>
              </div>
              <div class="panel-body">
                <a href="/admin/user/add">
                  Add <i class="fas fa-plus-circle fa-lg"></i>
                </a>
                <br/><br>
                <div class="table-responsive">
                  <table class="table">
                    <thead>
                      <tr class="success text-left">
                        <th>Username</th>
                        <th>Email</th>
                        <th>Role</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="user in listUser">
                        <td>{{ user.username }}</td>
                        <td>{{ user.email }}</td>
                        <td>{{ user.role.name }}</td>
                        <td>
                          &nbsp;&nbsp;
                          <a :href="'/admin/user/edit/'+user._id.$oid">
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
      name: 'UserList',
      data() {
        return {
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
  .aqua {
    background-color: #5da78f;
  }
</style>
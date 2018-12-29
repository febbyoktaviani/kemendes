<template>
  <div class="user-edit">
    <b-container class="text-left">
      <h4>Add User</h4>
      <hr>
      <b-card bg-variant="sand">
        <b-form>
          <b-form-group label="Username"
                        :label-cols="2"
                        horizontal>
            <b-form-input type="text" v-model="userData.username"></b-form-input>
          </b-form-group>
          <b-form-group label="Password"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="password" v-model="userData.password"></b-form-input>
          </b-form-group>
          <b-form-group label="Email"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-input type="email" v-model="userData.email"></b-form-input>
          </b-form-group>
          <b-form-group label="Role"
                        :label-cols="2"
                        size="lg"
                        horizontal>
            <b-form-select v-model="userData.role" :options="listRole">
            </b-form-select>
          </b-form-group>
          <br>
          <b-form-group class="text-right">
            <b-button variant="info" v-on:click="onSave()">Save</b-button>
          </b-form-group>
        </b-form>
      </b-card>
    </b-container>
  </div>
</template>
<script>
import Editor from '@tinymce/tinymce-vue';
import { mapGetters } from 'vuex';

export default {
  props: ['userId'],
  name: 'UserEdit',
  data() {
    return {
    };
  },
  methods: {
    onSave() {
      if (!this.userData.role) {
        swal({
          title: 'Warning',
          text: 'please select user role!!',
          icon: 'warning',
          dangerMode: true,
          button: 'OK',
        });
      }
      const formData = new FormData();
      formData.append('id', this.userId);
      formData.append('username', this.userData.username);
      formData.append('password', this.userData.password);
      formData.append('email', this.userData.email);
      formData.append('role', this.userData.role);
      this.$store.dispatch('createUser', formData);
    },
  },
  created() {
    this.$store.dispatch('fetchUser', this.userId);
    this.$store.dispatch('fetchListRole');
  },
  computed: {
    ...mapGetters({
      userData: 'userData',
      listRole: 'listRole',
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
</style>

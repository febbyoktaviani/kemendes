<template>
  <div class="video-list">
    <b-container fluid>
      <b-card bg-variant="sand"
              text-variant="black"
              title="List Video"
              class="text-left"
              :current-page="currentPage"
              :per-page="perPage"
              :small="true">

        <a href="/admin/video/add">
          <button class="btn-success">
            Add <i class="fas fa-plus-circle fa-lg"></i>
          </button>
        </a>
        <br/><br>
        <b-table striped hover :fields="fields" :items="listVideo">
          <template slot="is_shown" slot-scope="data">
            <i class="fas fa-checklist">{{ data.item.is_shown }} </i>
          </template>
          <template slot="action" slot-scope="data">
            <a :href="'/admin/video/edit/'+data.item._id.$oid">
              <i class="fas fa-edit fa-lg"></i>
            </a>
          </template>
        </b-table>
        <b-pagination :total-rows="listVideo.length"
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
  name: 'VideoList',
  data() {
    return {
      currentPage: 1,
      perPage: 20,
      fields: [
        {
          key: 'title',
          label: 'Judul',
        },
        'description',
        'url',
        {
          key: 'is_shown',
          label: 'Active',
        },
        {
          key: 'action',
          label: 'Action',
        },
      ],
    };
  },
  created() {
    this.$store.dispatch('fetchListVideo');
    // console.log('list-berita');
  },
  methods: {

  },
  computed: {
    ...mapGetters({
      listVideo: 'listVideo',
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

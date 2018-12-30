<template>
  <div class="container">
    <div class="centered">
      <h4>BERITA</h4>
      <b-list-group class="list-group">
        <b-list-group-item
          v-for="news in newslist"
          :key="news._id.$oid"
          :to="`/berita/${news._id.$oid}`"
        >{{news.title}}</b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState({
      newslist: state => state.berita.listBerita
    })
  },
  methods: {
    ...mapActions({
      fetchListBerita: "fetchListBerita"
    })
  },
  async mounted() {
    await this.fetchListBerita();
  }
};
</script>

<style scoped>
.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>

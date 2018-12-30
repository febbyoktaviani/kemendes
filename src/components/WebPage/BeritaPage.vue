<template>
  <div class="container">
    <div class="row">
      <b-card
        :key="`news${idx}`"
        :img-src="news.image"
        img-alt="Image"
        img-top
        tag="article"
        class="mb-2"
      >
        <h3>{{news.title}}</h3>
        <br>
        <template v-for="(paragraph, idx) in splitPar(news.content)">
          <p align="left" :key="`par${idx}`">{{paragraph}}</p>
        </template>
      </b-card>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState({
      news: state => state.berita.berita
    })
  },
  methods: {
    ...mapActions({
      fetchBerita: "fetchBerita"
    }),
    splitPar(content) {
      return content.split("\n");
    }
  },
  async mounted() {
    await this.fetchBerita(this.$route.params.id);
  }
};
</script>

<style>
</style>

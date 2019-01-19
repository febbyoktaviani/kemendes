<template>
  <div class="container uker">
    <div class="row">
      <b-card :img-src="getImageUrl(unitKerja.bagan)" img-alt="Image" img-top tag="article" class="mb-2">
        <h3>{{unitKerja.name}}</h3>
        <span v-html="unitKerja.profil"></span>
        <!-- <br>
        <template v-for="(paragraph, idx) in splitPar(news.content)">
          <p align="left" :key="`par${idx}`">{{paragraph}}</p>
        </template>-->
      </b-card>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { getImageUrl } from '@/helpers/util';

export default {
  computed: {
    ...mapState({
      unitKerja: state => state.unitKerja.unitKerja
    })
  },
  methods: {
    ...mapActions({
      fetchUnitKerja: "fetchUnitKerja"
    }),
    splitPar(content) {
      return content.split("\n");
    },
    getImageUrl(image) {
      return getImageUrl(image)
    }
  },
  async mounted() {
    await this.fetchUnitKerja(this.$route.params.id);
  }
};
</script>

<style>
.uker {
  padding: 3rem 0;
}
</style>

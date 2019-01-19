<template>
  <div class="container uker">
    <div class="centered">
      <h4>UNIT KERJA</h4>
      <b-list-group class="list-group">
        <b-list-group-item
          v-for="uk in unitKerjaList"
          :key="uk._id.$oid"
          :to="`/unitkerja/${uk._id.$oid}`"
        >{{uk.name}}</b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState({
      unitKerjaList: state => state.unitKerja.unitKerjaList
    })
  },
  methods: {
    ...mapActions({
      fetchListUnitKerja: "fetchListUnitKerja"
    })
  },
  async mounted() {
    await this.fetchListUnitKerja();
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
.uker {
  padding: 3rem 0;
}
</style>

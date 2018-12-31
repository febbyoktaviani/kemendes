<template>
  <div id="app">
    <Menu v-if="!isAdminPage()"/>
    <router-view></router-view>
  </div>
</template>

<script>
import Menu from "@/components/WebPage/common/Menu";

export default {
  name: "App",
  components: {
    Menu
  },
  methods: {
    isAdminPage() {
      return this.$route.path.includes('admin');
    },
  },
};
</script>

<style>
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style>

<template>
  <div id="app">
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
  data() {
    return {
      berita: [
        {
          title: "Berita 1",
          image: "",
          content: "content berita 1"
        },
        {
          title: "Berita 2",
          image: "",
          content: "content berita 2"
        }
      ]
    };
  }
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

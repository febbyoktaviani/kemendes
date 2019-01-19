<template>
  <div class="home">
    <!-- <Menu/> -->
    <div class="berita">
      <div class="container">
        <div class="row">
          <h3 class="title">Berita Terkini</h3>
        </div>
        <div class="row">
          <b-card-group deck>
            <b-card
              v-for="(news,idx) in headline"
              :key="`news${idx}`"
              :img-src="`${news.image}`"
              img-alt="Image"
              img-top
              tag="article"
              class="mb-2 no-border thumbnail-image"
            >
              <h4 align="left">
                {{news.title}}
              </h4>
              <p align="left">{{truncateContent(news.content)}}</p>
              <router-link :to="`/berita/${news._id.$oid}`">
                <p class="red">Baca Selengkapnya</p>
              </router-link>
            </b-card>
          </b-card-group>
        </div>
      </div>
    </div>
    <div class="website">
      <div class="container">
        <!-- component link other apps -->
        <div class="row center">
          <h3 class="title">Aplikasi Lainnya</h3>
        </div>
        <div class="row">
          <div class="col-sm-3"></div>
          <div class="col-sm-2 center">
            <a href="http://simpeg.kemendesa.go.id/" target="_blank">
              <div class="linkapp">
                <font-awesome-icon icon="user" size="4x" class="icon"></font-awesome-icon>
                <p>Sistem Informasi Kepegawaian Kemendesa</p>
              </div>
            </a>
          </div>
          <div class="col-sm-2 center">
            <div class="linkapp">
              <font-awesome-icon icon="chalkboard-teacher" size="4x" class="icon"></font-awesome-icon>
              <p>SI & Pembelajaran Pendamping Perdesaan</p>
            </div>
          </div>
          <div class="col-sm-2 center">
            <div class="linkapp">
              <font-awesome-icon icon="desktop" size="4x" class="icon"></font-awesome-icon>
              <p>Sistem Informasi Kawasan Pedesaan</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="video">
      <div class="container">
        <!-- component lates videos -->
      <div class="row">
          <h3 class="title">Video Terakhir</h3>
        </div>
      <div class="row">
        <carousel-3d :controls-visible="true">
          <slide :index="0">
            <iframe
              src="https://www.youtube.com/embed/kzzMvetlB-Y"
              class="video-slide"
              frameborder="0"
              allowfullscreen
            ></iframe>
            <p>video-1</p>
          </slide>
          <slide :index="1">
            <iframe
              src="https://www.youtube.com/embed/9EP_IqZ6SoQ"
              class="video-slide"
              frameborder="0"
              allowfullscreen
            ></iframe>
            <p>video-1</p>
          </slide>
          <slide :index="2">
            <iframe
              src="https://www.youtube.com/embed/kzzMvetlB-Y"
              class="video-slide"
              frameborder="0"
              allowfullscreen
            ></iframe>
            <p>video-1</p>
          </slide>
          <slide :index="3">
            <iframe
              src="https://www.youtube.com/embed/Mi0AHT-01eU"
              class="video-slide"
              frameborder="0"
              allowfullscreen
            ></iframe>
            <p>video-1</p>
          </slide>
          <slide :index="4">
            <iframe
              src="https://www.youtube.com/embed/9EP_IqZ6SoQ"
              class="video-slide"
              frameborder="0"
              allowfullscreen
            ></iframe>
            <p>video-1</p>
          </slide>
        </carousel-3d>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import Menu from "@/components/WebPage/common/Menu";
import { mapActions, mapState } from "vuex";
import { Carousel3d, Slide } from 'vue-carousel-3d';


export default {
  name: "Home",
  components: { Menu, Carousel3d, Slide },
  data() {
    return {
      msg: ""
    };
  },
  computed: {
    ...mapState({
      berita: state => state.berita.listBerita
    }),
    headline() {
      return this.berita.slice(0, 3);
    }
  },
  methods: {
    ...mapActions({
      fetchBerita: "fetchListBerita"
    }),
    truncateContent(content) {
      return content.slice(0, content.indexOf(".")) + "...";
    }
  },
  async mounted() {
    await this.fetchBerita();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
.website {
  background-color: #ebf4f0;
  padding: 50px 0;
}
.icon {
  color:#0b5445;
  align-self: center;
}
.linkapp {
  background-color: #ffff;
  min-height: 230px;
  border-radius: 1em;
}
.linkapp > p {
  color: #9e2a3b
}
.center{
  display: flex;
  justify-content: center;
  text-align: center;
}
.center p {
  padding-top: 1rem;
  text-align: center;
}
.title {
  padding: 2rem 0;

}
.video-slide {
  width: 362px;
  height: 272px;
}
.no-border {
  border-style: none;
}
.card-img-top {
  height: 232px;
}
@media only screen and (max-width: 576px) {
  .linkapp {
    background-color: #ffff;
    min-height: 230px;
    min-width: 384px;
    border-radius: 1em;
    margin: 1rem 0;
  }
}
</style>

<template>
  <div class="home">
    <!-- <Menu/> -->
    <div class="container">
      <div class="row">
        <b-card-group deck>
          <b-card
            v-for="(news,idx) in headline"
            :key="`news${idx}`"
            :img-src="news.image"
            img-alt="Image"
            img-top
            tag="article"
            class="mb-2"
          >
            <h3 align="left">
              <router-link :to="`/berita/${news._id.$oid}`">{{news.title}}</router-link>
            </h3>
            <p align="left">{{truncateContent(news.content)}}</p>
          </b-card>
        </b-card-group>
        <!-- <div class="col-sm-4">
          <div class="well">
            <h3 align="left">
              <a href="#">RAPAT KOORDINASI ANTAR KEMENTERIAN/LEMBAGA TAHUN ANGGARAN 2019</a>
            </h3>
            <p
              align="left"
            >Direktorat Pembangunan Ekonomi Kawasan Perdesaan tanggal 13-15 Nopember 2018 di Hotel Puri Denpasar Jakarta, melaksanakan Kegiatan Sosialisasi dan Persiapan Daerah dalam Program dan Bantuan Kementerian Desa, PDT dan Transmigrasi. Plt Direktur Jenderal PKP Ibu Harlina Sulistiyorini berkesempatan membuka acara dan didampingi Direktur PEKP Lutfi Latief dan Kasubdit Analisa Kebijakan Ekonomi</p>
          </div>
        </div>-->
      </div>
      <hr>
    </div>
    <!-- component link other apps -->
    <div class="container text-center">
      <br>
      <div class="row">
        <div class="col-sm-4 linkapp-container">
          <a href="http://simpeg.kemendesa.go.id/" target="_blank">
            <div class="linkapp">
              <h3>Sistem Informasi Kepegawaian Kemendesa</h3>
              <br>
              <font-awesome-icon icon="desktop" size="6x"></font-awesome-icon>
            </div>
          </a>
        </div>
        <div class="col-sm-4 linkapp-container">
          <div class="linkapp light-color">
            <h3>SI & Pembelajaran Pendamping Perdesaan</h3>
            <br>
            <font-awesome-icon icon="clock" size="6x"></font-awesome-icon>
          </div>
        </div>
        <div class="col-sm-4 linkapp-container">
          <div class="linkapp">
            <h3>Sistem Informasi Kawasan Pedesaan</h3>
            <br>
            <font-awesome-icon icon="globe" size="6x"></font-awesome-icon>
          </div>
        </div>
      </div>
      <hr>
    </div>

    <!-- component lates videos -->
    <div class="container text-left">
      <h3>Latest Videos</h3>
      <br>
      <div class="row">
        <div class="col-sm-3">
          <iframe
            src="https://www.youtube.com/embed/kzzMvetlB-Y"
            width="268"
            height="181"
            frameborder="0"
            allowfullscreen
          ></iframe>
          <p>video-1</p>
        </div>
        <div class="col-sm-3">
          <iframe
            src="https://www.youtube.com/embed/xnuftoxO_G0"
            width="268"
            height="181"
            frameborder="0"
            allowfullscreen
          ></iframe>
          <p>Video 2</p>
        </div>
        <div class="col-sm-3">
          <iframe
            src="https://www.youtube.com/embed/9EP_IqZ6SoQ"
            width="268"
            height="181"
            frameborder="0"
            allowfullscreen
          ></iframe>
          <p>Video 3</p>
        </div>
        <div class="col-sm-3">
          <iframe
            src="https://www.youtube.com/embed/Mi0AHT-01eU"
            width="268"
            height="181"
            frameborder="0"
            allowfullscreen
          ></iframe>
          <p>Video 4</p>
        </div>
      </div>
    </div>
    <!-- component berita terkini -->
    <div class="container text-left">
      <h3>Berita Terkini</h3>
      <br>
      <div class="row">
        <div class="col-sm-3">
          <p>video-1</p>
        </div>
        <div class="col-sm-3">
          <p>Video 2</p>
        </div>
        <div class="col-sm-3">
          <p>Video 3</p>
        </div>
        <div class="col-sm-3">
          <p>Video 4</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/WebPage/common/Menu";
import { mapActions, mapState } from "vuex";

export default {
  name: "Home",
  components: { Menu },
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
a {
  color: #42b983;
}
</style>

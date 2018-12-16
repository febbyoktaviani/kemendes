<template>
  <div class="home">
    <div class="container">
      <div class="row">
        <div class="col-sm-8">
          <div id="myCarousel" class="carousel slide" data-ride="carousel">
            <!-- Indicators -->
            <ol class="carousel-indicators">
              <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
              <li data-target="#myCarousel" data-slide-to="1"></li>
            </ol>

            <!-- Wrapper for slides -->
            <div class="carousel-inner" role="listbox">
              <div class="item active">
                <img src="/static/pembukaan_pekp.jpeg"
                     alt="Image"
                     class="slide-caro">
                <div class="carousel-caption">
                </div>
              </div>

              <div class="item">
                <img src="/static/slide2.jpg"
                     alt="Image"
                     class="slide-caro">
                <div class="carousel-caption">
                  <h3>More Sell $</h3>
                  <p>Lorem ipsum...</p>
                </div>
              </div>
            </div>

            <!-- Left and right controls -->
            <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
              <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
              <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>
        <div class="col-sm-4">
          <div class="well">
            <h3 align="left">
              <a href="#">
                RAPAT KOORDINASI ANTAR KEMENTERIAN/LEMBAGA TAHUN ANGGARAN 2019
              </a>
            </h3>
            <p align="left">Direktorat  Pembangunan Ekonomi Kawasan Perdesaan tanggal 13-15 Nopember 2018 di Hotel Puri Denpasar Jakarta, melaksanakan Kegiatan Sosialisasi dan Persiapan Daerah dalam Program dan Bantuan Kementerian Desa, PDT dan Transmigrasi. Plt Direktur Jenderal PKP Ibu Harlina Sulistiyorini berkesempatan membuka acara dan didampingi Direktur PEKP Lutfi Latief dan Kasubdit Analisa Kebijakan Ekonomi </p>
          </div>
        </div>
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
              <h3> Sistem Informasi Kepegawaian Kemendesa </h3>
              <br>
              <font-awesome-icon icon="desktop" size="6x"></font-awesome-icon>
            </div>
          </a>
        </div>
        <div class="col-sm-4 linkapp-container">
          <div class="linkapp light-color">
            <h3> SI & Pembelajaran Pendamping Perdesaan </h3>
            <br>
            <font-awesome-icon icon="clock" size="6x"></font-awesome-icon>
          </div>
        </div>
        <div class="col-sm-4 linkapp-container">
          <div class="linkapp">
            <h3> Sistem Informasi Kawasan Pedesaan </h3>
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
          <iframe src="https://www.youtube.com/embed/kzzMvetlB-Y" width="268" height="181" frameborder="0" allowfullscreen=""></iframe>
          <p>video-1</p>
        </div>
        <div class="col-sm-3">
          <iframe src="https://www.youtube.com/embed/xnuftoxO_G0" width="268" height="181" frameborder="0" allowfullscreen=""></iframe>
          <p>Video 2</p>
        </div>
        <div class="col-sm-3">
          <iframe src="https://www.youtube.com/embed/9EP_IqZ6SoQ" width="268" height="181" frameborder="0" allowfullscreen=""></iframe>
          <p>Video 3</p>
        </div>
        <div class="col-sm-3">
          <iframe src="https://www.youtube.com/embed/Mi0AHT-01eU" width="268" height="181" frameborder="0" allowfullscreen=""></iframe>
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
export default {
  name: 'Home',
  data() {
    return {
      msg: '',
      berita: [
        {
            'title': 'Berita 1',
            'image': '',
            'content': 'content berita 1'
        },
        {
            'title': 'Berita 2',
            'image': '',
            'content': 'content berita 2'
        }
    ],

    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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

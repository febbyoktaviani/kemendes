<template>
  <div class="footer">
    <div :style="{backgroundColor:'#0b5445'}">
      <b-container class="text-light p-3 mt-5">
        <b-row>
          <b-col>
            <b-row class="center">
              <img src="/static/logo-kemendesa.png" :style="{maxWidth:'150px', maxHeight:'120px'}">
            </b-row>
            <b-row class="center">
              <p :style="{textAlign:'center'}">
                Kementerian Desa, Pembangunan Daerah Tertinggal <br/>
                Dan Transmigrasi Republik Indonesia
            </p>
            </b-row>
          </b-col>  
        </b-row>
        <b-row>
          <b-col cols=3 />
          <b-col cols=3>
            <b-row class="center">
              <p class="small">
                <a target="_blank" href="https://goo.gl/maps/DKuMp6jpD132">
                  <font-awesome-icon icon="map-marker" size="2x"></font-awesome-icon>
                </a>
                <br/>
                <br>Jl. Abdul Muis No.7, RT.2/RW.3, 
                <br>Gambir, Jakarta Pusat, 
                <br>DKI Jakarta, Indonesia
                <br/>
                <br>021 - 3500334
              </p>
            </b-row>
          </b-col>
          <b-col cols=3>
            <b-row class="center">
              <p class="small">
                <a target="_blank" href="https://goo.gl/maps/rKKhiDNUbFN2">
                  <font-awesome-icon icon="map-marker" size="2x"></font-awesome-icon>
                </a>
                <br/>
                <br>Jl. TMP Kalibata No.17, 
                <br>Jakarta Selatan 12750, 
                <br>DKI Jakarta, Indonesia
                <br/>
                <br>021 - 7994372
              </p>
            </b-row>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div :style="{backgroundColor:'black', marginTop:0}">
      <b-container>
        <div class="row center text-light">
          <p>@2019 Kemendesa</p>
        </div>
      </b-container>
    </div>     
  </div>
</template>
<script>
export default {
  name: "Footer",
  data() {
    return {};
  }
};
</script>
<style>
.bg-leaf {
  background-color: #87b880;
}
.center{
  display: flex;
  justify-content: center;
  align-items: center;
}
.center p {
  padding-top: 1rem;
  text-align: center;
}
.footer {
  flex-shrink: 0;
}
</style>
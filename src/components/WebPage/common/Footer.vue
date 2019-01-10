<template>
  <div class="footer">
    <b-container fluid class="bg-leaf text-light p-3 mt-5">
      <b-row align-v="start" class="ml-4">
        <b-col>
          <b-row align-v="start">
            <h5><strong>POPULAR ARTICLE</strong></h5>
          </b-row>
        </b-col>
        <b-col>
          <b-row>
            <h5><strong>HUBUNGI KAMI</strong></h5>
          </b-row>
          <b-row>
            <p class="small"><strong style="color: green;">Kantor 2</strong><br>
            Jl. Abdul Muis No.7, RT.2/RW.3, Gambir, Jakarta Pusat, DKI Jakarta, Indonesia<br>Telp : 021 - 3500334</p>
            <p class="small"><strong style="color: green;">Kantor 1</strong><br>
            Jl. TMP Kalibata No.17, Jakarta Selatan  12750, DKI Jakarta,  Indonesia<br>
            Telp : 021 - 7994372</p>
          </b-row>
        </b-col>
        <b-col>
          <h5><strong>STAY CONNECTED</strong></h5>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
export default {
  name: 'Footer',
  data() {
    return {
    };
  },
};
</script>
<style>
  .bg-leaf {
    background-color: #87b880;
  }
</style>
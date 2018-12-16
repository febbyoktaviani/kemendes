<template>
  <div class="tujuan-form">
    <div class="container text-left">    
      <br>
      <div class="row">
        <div class="col-sm-12 linkapp-container">
          <div class="panel panel-success">
            <div class="panel-heading">
              <h4>Tujuan {{ tujuanId }}</h4>
            </div>
            <div class="panel-body">
              <input class="form-control" type="text" v-model="tujuan" />
            </div>
            <div class="panel-footer">Panel Footer</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex';
  export default {
    props: ['tujuanId'],
    name: 'TujuanForm',
    data() {
      return {
        // tujuan: 'test',
      };
    },
    created() {
        this.$store.dispatch('getTujuan', this.tujuanId);
        console.log('tujuan')

    },
    computed: {
        ...mapGetters({
          tujuan: 'tujuan',
        })
    },
    methods: {
    //     createTujuan() {
    //         const opt = {
    //           method: 'POST',
    //           headers: new Headers({
    //             'Accept': 'application/json',
    //             'Access-Control-Allow-Origin': '*',
    //             'mode': 'no-cors'
    //           })
    //         }
    //         fetch('http://localhost:5000/tujuan', opt)
    //           .then((response) => {
    //             if(response.status == 200){
    //               return response.json();
    //             } 
    //           }).then((res) => {
    //             console.log('tujuan', res);
    //             this.tujuan = res;
    //           }).catch((err)=>{
    //             console.log('err', err);
    //           });
    //         }
      
    },
  };
</script>
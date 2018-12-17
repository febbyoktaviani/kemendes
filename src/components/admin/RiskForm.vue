<template>
  <div class="risk-form">
    <div class="container text-left">    
      <br>
      <div class="row">
        <div class="col-sm-12 linkapp-container">
          <div class="container text-left">    
            <br>
            <div class="row">
              <div class="col-sm-12 linkapp-container">
                <div class="panel panel-success">
                  <TujuanForm v-if="step == 0" :tujuanId="tujuanId" :tujuan="tujuan"/>
                  <IndikatorForm v-if="step == 1"
                                 :tujuanId="tujuanId"
                                 :indikators="tujuan.indikators"
                                 :tujuanName="tujuan.name"/>
                  <KegiatanForm v-if="step == 2"
                                 :tujuanId="tujuanId"
                                 :indikators="tujuan.indikators"
                                 :tujuanName="tujuan.name"/>
                  <ResikoForm v-if="step == 3"
                                 :tujuanId="tujuanId"
                                 :indikators="tujuan.indikators"
                                 :tujuanName="tujuan.name"/>
                  <div class="panel-footer">
                    <!-- <div class="btn-group" style="padding: 20px"> -->
                      <button v-if="step > 0"
                              type="button"
                              class="btn btn-info"
                              v-on:click="back()">Back
                      </button>
                      &nbsp;&nbsp;&nbsp;
                      <button v-if="step < 3"
                              type="button"
                              class="btn btn-info"
                              v-on:click="next()">Next</button>
                      &nbsp;
                      <button v-if="step == 3"
                              type="button"
                              class="btn btn-success"
                              v-on:click="save()">Save</button>
                    <!-- </div> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import TujuanForm from '@/components/admin/TujuanForm';
  import IndikatorForm from '@/components/admin/IndikatorForm';
  import KegiatanForm from '@/components/admin/KegiatanForm';
  import ResikoForm from '@/components/admin/ResikoForm';
  import { mapGetters } from 'vuex';
  export default {
    props: ['tujuanId'],
    components: {TujuanForm, IndikatorForm, KegiatanForm, ResikoForm},
    name: 'RiskForm',
    data() {
      return {
        step: 0,
      };
    },
    created() {
        if (this.tujuanId != '1') {
          this.$store.dispatch('getTujuan', this.tujuanId);
          console.log('tujuan')
        }
    },
    methods: {
      next() {
        this.step += 1
      },
      back() {
        this.step -= 1
      },
      save() {
        console.log(JSON.stringify(this.tujuan))
        let header = new Headers({
          'Accept': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'mode': 'no-cors'
        });
        const opt = {
          method: 'POST',
          headers: header,
          body: JSON.stringify(this.tujuan)
        }
        fetch('http://kemendesapi.detase.men/rencana-kerja', opt)
          .then((response) => {
            if(response.status == 200){
              console.log(response)
              return response.json();
            } 
            
          }).then((res) => {
            console.log(res);
            window.location.href = `/#/admin/tujuan/${res.tujuan_id}`
            
          }).catch((err)=>{
            console.log('err', err);
          });
      }
    },
    computed: {
        ...mapGetters({
          tujuan: 'tujuan',
          riskFormList: 'riskFormList',
        })
    },
  };
</script>
<style type="text/css">
  .sub-field {
    padding: 10px;
  }
</style>
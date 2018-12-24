<template>
  <div class="rencana-kerja-add">
    <div class="container text-left">    
      <br>
      <div class="row">
        <div class="col-sm-12 linkapp-container">
          <div class="container text-left">    
            <br>
            <div class="row">
              <div class="col-sm-12 linkapp-container">
                <div class="panel panel-success">
                  <TujuanForm v-if="step == 0" :tujuan="tujuan"/>
                  <IndikatorForm v-if="step == 1"
                                 :indikators="tujuan.indikators"
                                 :tujuanName="tujuan.name"/>
                  <KegiatanForm v-if="step == 2"
                                 :indikators="tujuan.indikators"
                                 :tujuanName="tujuan.name"/>
                  <ResikoForm v-if="step == 3"
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
  import TujuanForm from '@/components/AdminPage/RencanaKerja/Form/TujuanForm';
  import IndikatorForm from '@/components/AdminPage/RencanaKerja/Form/IndikatorForm';
  import KegiatanForm from '@/components/AdminPage/RencanaKerja/Form/KegiatanForm';
  import ResikoForm from '@/components/AdminPage/RencanaKerja/Form/ResikoForm';
  import { mapGetters } from 'vuex';
  import {base_url} from '@/store/config';
  import router from '@/router';
  export default {
    props: [],
    components: {TujuanForm, IndikatorForm, KegiatanForm, ResikoForm},
    name: 'RencanaKerjaAdd',
    data() {
      return {
        step: 0,
        tujuan: {'id': '', 'indikators':[{'kegiatans':[]}]},
      };
    },
    created() {
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
        fetch(`${base_url}/rencana-kerja`, opt)
          .then((response) => {
            if(response.status == 200){
              console.log(response)
              return response.json();
            } 
            
          }).then((res) => {
            console.log(res);
            router.push(`/admin/tujuan/${res.tujuan_id}`)
            
          }).catch((err)=>{
            console.log('err', err);
          });
      }
    },
    computed: {
        ...mapGetters({
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
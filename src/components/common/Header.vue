<template>
  <div class='header'>
    <header class="container-fluid text-left">
      <div class="container-fluid col-sm-8 text-left">
        <p><i class="fas fa-map-marker-alt"></i>&nbsp;&nbsp;<b>Jl. TMP Kalibata No.17, DKI Jakarta</b></p>
        <p>
            <i class="fas fa-phone-volume"></i>&nbsp;&nbsp;<b>+6251 878767</b>
            &nbsp;&nbsp;&nbsp;
            <i class="fas fa-envelope"></i>&nbsp;&nbsp;<b>contact@kemendesa.go.id</b>
        </p>
      </div>
      <div class="container-fluid col-sm-4 text-right">
        <button class="btn btn-danger">Login</button>
      </div>
    </header>
  </div>
</template>
<script>
export default {
    name: '',
    data() {
        return {
            isLoggedin: false,

        };
    }
};
</script>
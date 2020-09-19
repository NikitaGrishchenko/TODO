<template>
  <div>
    <navbar />
    <div class="d-flex wrapper" ref="wrapper">
      <div class="container">
        <child />
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MainLayout'
  }
</script>

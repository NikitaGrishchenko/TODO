<template>
  <div class="sidebar">
    <div class="sidebar-username">
      {{ this.userName }}
    </div>
    <a href="/auth/logout/">Выйти</a>
  </div>
</template>

<script>
  export default {
    name: 'sidebar',
    props: {
      userName: {
        type: String
      }
    }
  }
</script>

<style lang="sass">
  .sidebar
    height: 100%
    width: 85px
    background-color: #333
    position: fixed
    z-index: 5
    top: 0
    left: 0
    overflow-x: hidden
    color: #ffffff
</style>

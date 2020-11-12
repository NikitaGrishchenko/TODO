<template>
  <div
    class="sidebar d-flex flex-column justify-content-between align-items-center"
  >
    <div class="sidebar-user text-center">
      <img
        width="50"
        src="static/img/sidebar-plug-user.png"
        alt=""
        class="sidebar-user__img mt-3 mb-1"
      />
      <div class="sidebar-user__username">
        {{ this.userName }}
      </div>
    </div>
    <a class="mb-3" href="/auth/logout/">
      <img src="static/img/sidebar-exit.png" alt="" class="sidebar-exit" />
    </a>
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
    background-color: #0F121B
    position: fixed
    z-index: 5
    top: 0
    left: 0
    overflow-x: hidden
    color: #ffffff
</style>

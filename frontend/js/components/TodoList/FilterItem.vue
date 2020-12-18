<template>
  <button
    type="button"
    class="todo-box-btn__item"
    :class="{ active: isActive }"
    @click="active"
  >
    {{ text }}
  </button>
</template>

<script>
  export default {
    props: {
      text: String,
      id: String,
      isActive: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      active() {
        this.$emit('active', {
          id: this.id
        })
      }
    }
  }
</script>

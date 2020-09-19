<template>
  <div class="row">
    {{ todos }}

    <ul>
      <li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    metaInfo() {
      const { appName } = window.config

      return {
        title: appName,
        titleTemplate: null
      }
    },
    data() {
      return {
        todos: null
      }
    },
    created() {
      axios.get('todo/').then(response => {
        this.todos = response.data
      })
    }
  }
</script>

<style lang="sass" scoped>
  *
    color: #fff
</style>

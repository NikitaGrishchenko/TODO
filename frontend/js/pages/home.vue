<template>
  <todo-list></todo-list>
</template>

<script>
  import TodoList from '../components/todo/TodoList'
  export default {
    components: {
      'todo-list': TodoList
    },

    layout: 'default',
    metaInfo() {
      const { appName } = window.config

      return {
        title: appName,
        titleTemplate: null
      }
    }
  }
</script>

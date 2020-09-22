<template>
  <list-task />
</template>

<script>
  import ListTask from '../components/ui/ListTask'
  export default {
    components: {
      'list-task': ListTask
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

import Vue from 'vue'
import App from './App'
import TodoList from './TodoList'
;[App, TodoList].forEach(Component => {
  if (!Component.name) {
    throw new Error(`Not component name: ${Component}`)
  }

  Vue.component(Component.name, Component)
})

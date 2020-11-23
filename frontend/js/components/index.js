import Vue from 'vue'
import App from './App'
import TodoList from './TodoList'
import Sidebar from './Sidebar'
import Preloader from './Preloader'
;[App, TodoList, Sidebar, Preloader].forEach(Component => {
  if (!Component.name) {
    throw new Error(`Not component name: ${Component}`)
  }

  Vue.component(Component.name, Component)
})

<template>
  <div class="container">
    <div class="row">
      <div class="col-6 offset-3 d-flex align-items-center">
        <input
          type="text"
          class="todo-input"
          placeholder="Что надо сделать?"
          v-model="newTodo"
          @keyup.enter="addTodo"
        />
        <button @click="addTodo">
          Ок
        </button>
      </div>
    </div>
    <div v-if="!todos" class="row">
      <div class="col-6 offset-3 text-center mt-3">
        <div class="preloader">
          <div class="loader07"></div>
        </div>
      </div>
    </div>
    <div v-if="todos && todos.length > 0" class="row">
      <div class="col-6 offset-3 mb-2">
        <div class="d-flex align-items-center justify-content-between">
          <div class="d-flex">
            <button
              class="btn btn-primary"
              :class="{ active: filter == 'all' }"
              @click="filter = 'all'"
            >
              Все
            </button>
            <button
              class="btn btn-primary mx-2"
              :class="{ active: filter == 'active' }"
              @click="filter = 'active'"
            >
              Активные
            </button>
            <button
              class="btn btn-primary"
              :class="{ active: filter == 'completed' }"
              @click="filter = 'completed'"
            >
              Завершённые
            </button>
          </div>
          <div>{{ remaining }} {{ remainingTitle }}</div>
        </div>
      </div>
      <transition-group
        enter-active-class="animated fadeInLeft"
        leave-active-class="animated fadeOutRight"
        class="col-6 offset-3"
      >
        <div
          class="todo-item d-flex justify-content-between align-items-center"
          v-for="(todo, index) in todosFiltered"
          :key="todo.id"
        >
          <div class="d-flex justify-content-between align-items-center">
            <input
              type="checkbox"
              v-model="todo.completed"
              class="todo-item__checkbox"
              @change="checkTodo(index)"
            />
            <div
              v-if="!todo.editing"
              @dblclick="editTodo(todo)"
              class="todo-item__title"
              :class="{ completed: todo.completed }"
            >
              {{ todo.title }}
            </div>
            <div class="d-flex" v-else>
              <input
                class="todo-item__edit"
                type="text"
                v-model="todo.title"
                @keyup.esc="cancelEdit(todo)"
              />
              <button @click="doneEdit(index)">
                Ок
              </button>
            </div>
          </div>
          <div :class="{ clickRemove: clickRemove === todo.id }">
            <div
              class="todo-item__remove"
              @click="removeTodo(index)"
              @click.prevent="clickRemove = todo.id"
            >
              &times;
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    <div v-if="todos && todos.length === 0" class="row">
      <div class="col-6 offset-3 text-center mt-3">
        <h1>Задач нету</h1>
      </div>
    </div>
  </div>
</template>

<script>
  import Swal from 'sweetalert2'
  import axios from 'axios'
  // axios.defaults.baseURL = ''

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
        clickRemove: undefined,
        newTodo: '',
        beforeEditCache: '',
        filter: 'all',
        todos: null
      }
    },
    computed: {
      remaining() {
        return this.todos.filter(todo => !todo.completed).length
      },
      // правописание словосочетания 'задач осталось'
      remainingTitle() {
        var title = ''
        if (this.remaining === 1) {
          title = 'задача осталась'
        } else if (this.remaining >= 2 && this.remaining <= 4) {
          title = 'задачи осталось'
        } else {
          title = 'задач осталось'
        }
        return title
      },
      todosFiltered() {
        if (this.filter === 'all') {
          const initialArray = this.todos
          // выполнененные задачи опусаются вниз списка
          const sortedTodos = initialArray.sort(function(a, b) {
            return a.completed - b.completed
          })
          return sortedTodos
        } else if (this.filter === 'active') {
          return this.todos.filter(todo => !todo.completed)
        } else if (this.filter === 'completed') {
          return this.todos.filter(todo => todo.completed)
        }
        return this.todos
      }
    },
    directives: {
      focus: {
        inserted: function(el) {
          el.focus()
        }
      }
    },
    methods: {
      addTodo() {
        if (this.newTodo.trim().length === 0) {
          return Swal.fire({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            icon: 'warning',
            title: 'Ты походу что-то забыл',
            timer: 1800,
            timerProgressBar: true,
            background: '#333333'
          })
        } else {
          // eslint-disable-next-line no-unused-vars
          const result = {
            title: this.newTodo,
            completed: false,
            editing: false
          }
          this.newTodo = ''
          axios
            .post('todo/', result)
            .then(response => {
              var newArray = response.data
              this.todos.unshift({
                id: newArray.id,
                title: newArray.title,
                completed: false,
                editing: false
              })
              Swal.fire({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                icon: 'success',
                title: 'Задача добавлена',
                timer: 3000,
                timerProgressBar: true,
                background: '#333333'
              })
            })
            .catch(() => {
              Swal.fire({
                icon: 'error',
                title: 'Ошибка'
              })
            })
        }
      },
      editTodo(todo) {
        this.beforeEditCache = todo.title
        todo.editing = true
      },
      doneEdit(index) {
        // if (todo.title.trim() === '') {
        //   todo.title = this.beforeEditCache
        // }
        this.todos[index].editing = false
        const updateData = this.todos[index]
        if (updateData.title !== this.beforeEditCache) {
          axios
            .patch('todo/' + updateData.id + '/', updateData)
            .then(() => {
              Swal.fire({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                icon: 'success',
                title: 'Задача изменена',
                timer: 3000,
                timerProgressBar: true,
                background: '#333333'
              })
            })
            .catch(error => {
              console.log(error)
            })
        } else {
          Swal.fire({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            icon: 'question',
            title: 'И ШО? Буквы платные?',
            timer: 3000,
            timerProgressBar: true,
            background: '#333333'
          })
        }
      },
      cancelEdit(todo) {
        todo.title = this.beforeEditCache
        todo.editing = false
      },
      removeTodo(index) {
        const deleteData = this.todos[index]
        this.todos.splice(index, 1)
        axios.delete('todo/' + deleteData.id + '/', deleteData).then(() => {
          Swal.fire({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            icon: 'warning',
            title: 'Задача удалена',
            timer: 3000,
            timerProgressBar: true,
            background: '#333333'
          })
        })
      },
      checkTodo(index) {
        const indexData = this.todos[index]
        const checkTodoData = {
          completed: indexData.completed
        }
        axios
          .patch('todo/' + indexData.id + '/', checkTodoData)
          .then(() => {})
          .catch(error => {
            console.log(error)
          })
      }
    },
    created() {
      axios
        .get('todo/')
        .then(response => {
          setTimeout(() => {
            this.todos = response.data.reverse()
            console.log(this.todos)
          }, 750)
        })
        .catch(error => console.log(error))
    }
  }
</script>

<style lang="sass" scoped>
  @import url("https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.0.0/animate.compat.css")

  div
    color: #333
  .todo
    &-input
      width: 100%
      padding: 10px 18px
      margin: 20px 0px
      font-size: 18px
      &:focus
        outline: 0
    &-item
      padding: 17px 23px
      margin: 14px 0px
      border-radius: 3px
      font-size: 18px
      animation-duration: 0.3s
      &__remove
        cursor: pointer
        user-select: none
        &:hover
          color: #000
      &__edit
        font-size: 18px
        margin-left: -5px
        width: 100%
        padding: 5px
        border: 1px solid #ccc
        &:focus
          outline: none
      &__checkbox
        margin-right: 7px
  .completed
    text-decoration: line-through
    color: grey
  .clickRemove
    visibility: hidden
</style>

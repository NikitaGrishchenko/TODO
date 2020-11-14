{% load static%}
<template>
  <div class="container todo-container">
    <div class="row">
      <div class="col-6 offset-3 text-center my-2 mt-3">
        <div class="todo-logo">
          <img class="todo-logo__img" src="/static/img/logo.png" alt="" />
        </div>
      </div>
    </div>
    <div v-if="!todos" class="row">
      <div class="col-6 offset-3 text-center mt-3">
        <div class="preloader">
          <div class="loader07"></div>
        </div>
      </div>
    </div>
    <div v-if="todos" class="row">
      <div class="col-6 offset-3">
        <input
          type="text"
          class="todo-input"
          placeholder="Что надо сделать?"
          v-model="newTodo"
          @keyup.enter="addTodo"
        />
        <button class="d-none" @click="addTodo">
          Ок
        </button>
      </div>
    </div>
    <div v-if="todos && todos.length === 0" class="row">
      <div class="col-6 offset-3 text-center mt-3 none-active">
        <h3>Активных задач нет</h3>
      </div>
    </div>
    <div v-if="todos && todos.length > 0" class="row">
      <div class="col-6 offset-3 mb-2">
        <div class="todo-box-btn">
          <button
            type="button"
            class="todo-box-btn__item"
            :class="{ active: filter == 'all' }"
            @click="filter = 'all'"
          >
            Все
          </button>
          <button
            type="button"
            class="todo-box-btn__item"
            :class="{ active: filter == 'active' }"
            @click="filter = 'active'"
          >
            Активные
          </button>
          <button
            type="button"
            class="todo-box-btn__item"
            :class="{ active: filter == 'completed' }"
            @click="filter = 'completed'"
          >
            Завершённые
          </button>
        </div>
      </div>
    </div>
    <div v-if="todos" class="row">
      <!-- <div class="col-6 offset-3 text-right mb-3">
        <div>{{ remaining }} {{ remainingTitle }}</div>
      </div> -->
      <transition-group
        enter-active-class="animated fadeInLeft"
        leave-active-class="animated fadeOutRight"
        class="todo-wrapper col-6 offset-3"
        tag="div"
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
          <div class="d-flex justify-content-between align-items-center">
            <div class="todo-item__change" @click="editTodo(todo)">
              <img
                src="static/img/pencil.png"
                alt="pencil"
                class="todo-item__pencil"
              />
            </div>
            <div :class="{ clickRemove: clickRemove === todo.id }">
              <div
                class="todo-item__remove"
                @click="removeTodo(index)"
                @click.prevent="clickRemove = todo.id"
              >
                <img
                  src="static/img/times.png"
                  alt="times"
                  class="todo-item__times"
                />
              </div>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
  </div>
</template>

<script>
  import Swal from 'sweetalert2'
  import axios from 'axios'
  export default {
    name: 'todo-list',
    props: { userId: Number },
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
    methods: {
      addTodo() {
        if (this.newTodo.trim().length === 0) {
          return Swal.fire({
            position: 'center',
            showConfirmButton: false,
            icon: 'warning',
            title: 'Введите текст',
            timer: 1000,
            timerProgressBar: true
          })
        } else {
          // eslint-disable-next-line no-unused-vars
          const result = {
            title: this.newTodo,
            completed: false,
            editing: false,
            user: this.userId
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
              // Swal.fire({
              //   toast: true,
              //   position: 'top-end',
              //   showConfirmButton: false,
              //   icon: 'success',
              //   title: 'Задача добавлена',
              //   timer: 3000,
              //   timerProgressBar: true,
              //   background: '#333333'
              // })
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
            .then(() => {})
            .catch(error => {
              console.log(error)
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
        axios.delete('todo/' + deleteData.id + '/', deleteData).then(() => {})
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
            console.log(response.data)
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
    &-container
    &-wrapper
    &-input
      background: url(../../static/img/plus-input.png) no-repeat 3px 11px
    &-item
      font-size: 18px
      animation-duration: 0.3s
      padding: 20px 20px
      margin: 10px 0px
      border-radius: 15px
      background: #0F121B
      border: none
      outline: none
      &__title
        padding-left: 10px
        padding-right: 7px
        color: #ffffff
      &__remove
        cursor: pointer
        user-select: none
        margin-left: 9px
        color: #FF2D2D
      &__change
        cursor: pointer
        user-select: none
        color: #fff
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
    &-box-btn
      display: flex
      justify-content: flex-end
      margin-top: 10px
      &__item
        display: inline-block
        margin-left: 10px
        padding: 8px 15px
        border-radius: 15px
        background: transparent
        border: none
        border: 1px solid #7B7D8A
        outline: none
        color: #7B7D8A
    &-logo
      margin-top: 30px
      margin-bottom: 10px
      &__img
        user-select: none
  .completed
    text-decoration: line-through
    color: #7b7d8a
  .clickRemove
    visibility: hidden
  .btn
    border-radius: 0px !important
  .active
    background: transparent
    color: #fff
    border: 1px solid #fff
  .none-active
    color: #ffffff
</style>

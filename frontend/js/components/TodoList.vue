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
    <preloader v-if="!todos"></preloader>
    <div v-if="todos" class="row">
      <div class="col-6 offset-3">
        <div class="todo-input__wrapper">
          <textarea
            type="text"
            class="todo-input"
            placeholder="Что надо сделать?"
            v-model="newTodo"
            @keyup.enter="addTodo"
          ></textarea>
          <div class="todo-input__footer d-flex align-content-center">
            <datepicker
              input-class="todo-datepicker"
              v-model="inputDatePicker"
              :language="ru"
              :monday-first="true"
              :format="format"
            ></datepicker>
            <select class="todo-select" v-model="selectedUserPriority">
              <option class="todo-option__4" value="4">Обычный</option>
              <option value="1">1 приоритет</option>
              <option value="2">2 приоритет</option>
              <option value="3">3 приоритет</option>
            </select>
          </div>
        </div>
      </div>
    </div>
    <div v-if="todos && todos.length === 0" class="row">
      <div class="col-6 offset-3 text-center mt-3 none-active">
        <h3>Активных задач нет</h3>
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
          <div class="todo-right">
            <div class="d-flex align-items-center">
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
                :style="{
                  'border-bottom': '1px solid' + ' ' + todo.priority_color
                }"
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
            <div class="todo-item__date">
              {{ todo.date }}
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
  </div>
</template>

<script>
  import Swal from 'sweetalert2'
  import axios from 'axios'
  import Preloader from './Preloader'
  import Datepicker from 'vuejs-datepicker'
  import { ru } from 'vuejs-datepicker/dist/locale'
  import moment from 'moment'

  export default {
    components: { Preloader, Datepicker },
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
        ru: ru,
        clickRemove: undefined,
        newTodo: '',
        beforeEditCache: '',
        todos: null,
        filter: 'all',
        inputDatePicker: moment().format(),
        format: 'd MMM',
        selectedUserPriority: '4'
      }
    },
    computed: {
      // счетчик количества выполненных задач
      // remaining() {
      //   return this.todos.filter(todo => !todo.completed).length
      // },
      // правописание словосочетания 'задач осталось'
      // remainingTitle() {
      //   var title = ''
      //   if (this.remaining === 1) {
      //     title = 'задача осталась'
      //   } else if (this.remaining >= 2 && this.remaining <= 4) {
      //     title = 'задачи осталось'
      //   } else {
      //     title = 'задач осталось'
      //   }
      //   return title
      // },
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
      //форматирование даты для API
      // customFormatter(date) {
      //   moment.lang('ru')
      //   return moment(date).format('d MMMM, dddd')
      // },
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
            user: this.userId,
            priority: this.selectedUserPriority,
            date: moment(this.inputDatePicker).format('YYYY-MM-DD')
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
                editing: false,
                priority: newArray.priority,
                date: newArray.date,
                priority_color: newArray.priority_color
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
    &-container
    &-wrapper
    &-input
      background: url(../../static/img/plus-input.png) no-repeat 3px 0px
      &__wrapper
        border-bottom: 0.5px solid #fff
        padding: 10px 0
        margin-bottom: 10px
    &-item
      font-size: 18px
      animation-duration: 0.3s
      padding: 20px 20px
      margin: 10px 0px
      border-radius: 15px
      background: #0F121B
      border: none
      outline: none
      &:hover .todo-item__remove
        opacity: 1
      &:hover .todo-item__change
        opacity: 1
      &__title
        margin-left: 10px
        padding-right: 2px
        margin-right: 10px
        padding-bottom: 2px
        margin-bottom: 5px
        color: #ffffff
      &__remove
        cursor: pointer
        user-select: none
        margin-left: 9px
        color: #FF2D2D
        opacity: 0
        transition: .2s
      &__change
        cursor: pointer
        user-select: none
        color: #fff
        opacity: 0
        transition: .2s
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
        margin-top: -8.5px
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

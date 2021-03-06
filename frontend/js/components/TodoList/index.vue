{% load static%}
<template>
  <div class="container todo-container">
    <div class="row">
      <div class="col-6 offset-3 text-center my-4 mt-4">
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
            @keyup.enter="addItem"
          ></textarea>
          <div
            class="todo-input__footer d-flex align-content-center justify-content-between"
          >
            <div class="d-flex align-content-center">
              <datepicker
                input-class="todo-datepicker"
                v-model="inputDatePicker"
                :language="ru"
                :monday-first="true"
                :format="format"
              ></datepicker>
              <select class="todo-select" v-model="selectedUserPriority">
                <option class="todo-option__4" value="1">Обычный</option>
                <!-- <option value="1">1 приоритет</option>
                <option value="2">2 приоритет</option>
                <option value="3">3 приоритет</option> -->
              </select>
            </div>
            <div class="todo-input__btn" @click="addItem">Добавить</div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <transition-group
        enter-active-class="animated fadeInLeft"
        leave-active-class="animated fadeOutRight"
        class="todo-wrapper col-6 offset-3"
        tag="div"
        v-if="todosFiltered && todosFiltered.length > 0"
        appear
      >
        <item
          v-for="item in todosFiltered"
          :key="item.id"
          :item="item"
          :ru="ru"
          :format="format"
          @beginEdit="beginEditItem"
          @finishEdit="finishEditItem"
          @remove="removeItem"
          @check="checkItem"
        />
      </transition-group>
      <div
        v-if="todos && todosFiltered.length == 0"
        class="col-6 offset-3 text-center mt-5 none-active"
      >
        <h3>Задач нет</h3>
      </div>
    </div>
    <div v-if="todos && todos.length === 0" class="row">
      <div class="col-6 offset-3 text-center none-active">
        <p>Напишите выше, что нужно сделать и нажмите Enter</p>
      </div>
    </div>
    <div v-if="todos && todos.length > 0">
      <div class="todo-box-btn">
        <filter-item
          v-for="filterItem in filters"
          :key="filterItem.id"
          :id="filterItem.id"
          :text="filterItem.text"
          :is-active="filterItem.id === filter"
          @active="filtering"
        />
      </div>
    </div>
  </div>
</template>

<script>
  import Swal from 'sweetalert2'
  import axios from 'axios'
  import Preloader from './Preloader'
  import Item from './Item'
  import FilterItem from './FilterItem'
  import Datepicker from 'vuejs-datepicker'
  import { ru } from 'vuejs-datepicker/dist/locale'
  import moment from 'moment'

  export default {
    components: { Preloader, Datepicker, Item, FilterItem },
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
        filters: [
          {
            text: 'Активные',
            id: 'active'
          },
          {
            text: 'Завершённые',
            id: 'completed'
          },
          {
            text: 'Все',
            id: 'all'
          }
        ],
        filter: 'active',
        inputDatePicker: moment().format(),
        format: 'd MMM',
        selectedUserPriority: '1'
      }
    },
    computed: {
      todosFiltered() {
        if (!this.todos) {
          return []
        }

        if (this.filter === 'all') {
          return this.todos
        } else if (this.filter === 'completed') {
          return this.todos.filter(todo => todo.completed)
        }
        return this.todos.filter(todo => !todo.completed)
      }
    },
    methods: {
      filtering({ id }) {
        this.filter = id
      },
      updateTodoItem(item) {
        const saveDate = {
          ...item,
          date: moment(item.date, 'MM-DD-YYYY').format('YYYY-MM-DD')
        }
        axios
          .patch(`todo/${item.id}/`, saveDate)
          .then(() => {})
          .catch(error => {
            console.log(error)
          })
      },

      checkItem({ item, completed }) {
        item.completed = completed
        this.updateTodoItem(item)
      },
      removeItem(item) {
        const index = this.todos.findIndex(t => t.id === item.id)
        this.todos.splice(index, 1)
        axios.delete(`todo/${item.id}/`).then(() => {})
      },
      finishEditItem({ item, complite }) {
        if (!complite) {
          //
          return
        }
        this.updateTodoItem(item)
      },
      addItem() {
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
            user: this.userId,
            priority: this.selectedUserPriority,
            date: moment(this.inputDatePicker).format('YYYY-MM-DD')
          }
          this.newTodo = ''
          axios
            .post('todo/', result)
            .then(response => {
              this.todos.unshift(response.data)
            })
            .catch(() => {
              Swal.fire({
                icon: 'error',
                title: 'Ошибка'
              })
            })
        }
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
</style>

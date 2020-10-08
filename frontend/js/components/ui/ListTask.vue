<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <input
          type="text"
          class="todo-input"
          placeholder="Что надо сделать?"
          v-model="newTodo"
          @keyup.enter="addTodo"
        />
      </div>
    </div>
    <div v-if="this.todos && this.todos.length > 0" class="row">
      <div class="col-12 mb-2">
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
          <div>{{ remaining }} задачи осталось</div>
        </div>
      </div>
      <div class="col-12">
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
          <div class="todo-item__remove" @click="removeTodo(index)">
            &times;
          </div>
        </div>
      </div>
    </div>
    <div v-else class="row">
      <div class="col-12 text-center mt-3">
        <h1>Задач нет</h1>
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
        newTodo: '',
        beforeEditCache: '',
        filter: 'all',
        todos: []
      }
    },
    computed: {
      remaining() {
        return this.todos.filter(todo => !todo.completed).length
      },
      anyRemaining() {
        return this.remaining === 0
      },
      todosFiltered() {
        if (this.filter === 'all') {
          return this.todos
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
          return alert('Введите что-нибудь')
        } else {
          // eslint-disable-next-line no-unused-vars
          const result = {
            title: this.newTodo,
            completed: false,
            editing: false
          }
          axios
            .post('todo/', result)
            .then(response => {
              var newArray = response.data
              this.todos.push({
                id: newArray.id,
                title: newArray.title,
                completed: false,
                editing: false
              })
              console.log(newArray)
              Swal.fire({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                icon: 'success',
                title: 'Задача добавлена',
                timer: 3000,
                timerProgressBar: true
              })
              this.newTodo = ''
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
              timerProgressBar: true
            })
          })
          .catch(error => {
            console.log(error)
          })
      },
      cancelEdit(todo) {
        todo.title = this.beforeEditCache
        todo.editing = false
      },
      removeTodo(index) {
        const deleteData = this.todos[index]
        axios.delete('todo/' + deleteData.id + '/', deleteData).then(() => {
          Swal.fire({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            icon: 'success',
            title: 'Задача удалена',
            timer: 3000,
            timerProgressBar: true
          })
          this.todos.splice(index, 1)
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
          this.todos = response.data
        })
        .catch(error => console.log(error))
    }
  }
</script>

<style lang="sass" scoped>
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
      border: 1px solid #333
      padding: 17px 23px
      margin: 14px 0px
      border-radius: 3px
      font-size: 18px
      &__remove
        cursor: pointer
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
</style>

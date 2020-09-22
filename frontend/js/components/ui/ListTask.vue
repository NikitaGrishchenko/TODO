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
            />
            <div
              v-if="!todo.editing"
              @dblclick="editTodo(todo)"
              class="todo-item__title"
              :class="{ completed: todo.completed }"
            >
              {{ todo.title }}
            </div>
            <input
              v-else
              class="todo-item__edit"
              type="text"
              v-model="todo.title"
              @blur="doneEdit(todo)"
              @keyup.esc="cancelEdit(todo)"
              v-focus
            />
          </div>
          <div class="todo-item__remove" @click="removeTodo(index)">
            &times;
          </div>
        </div>
      </div>
      <div class="col-12">
        <div class="d-flex align-items-center justify-content-between">
          <div>
            <label>
              <input
                type="checkbox"
                :checked="anyRemaining"
                @change="checkAllTodos"
              />
              Выбрать всё
            </label>
          </div>
          <div>{{ remaining }} задачи осталось</div>
        </div>
      </div>
      <div class="col-12">
        <hr />
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
      </div>
    </div>
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
        newTodo: '',
        idForTodo: 10,
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
        // eslint-disable-next-line eqeqeq
        return this.remaining == 0
      },
      todosFiltered() {
        // eslint-disable-next-line eqeqeq
        if (this.filter == 'all') {
          return this.todos
          // eslint-disable-next-line eqeqeq
        } else if (this.filter == 'active') {
          return this.todos.filter(todo => !todo.completed)
          // eslint-disable-next-line eqeqeq
        } else if (this.filter == 'completed') {
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
          this.todos.push({
            id: this.idForTodo,
            title: this.newTodo,
            completed: false,
            editing: false
          })
          this.newTodo = ''
          this.idForTodo++
        }
      },
      editTodo(todo) {
        this.beforeEditCache = todo.title
        todo.editing = true
      },
      doneEdit(todo) {
        // eslint-disable-next-line eqeqeq
        if (todo.title.trim() == '') {
          todo.title = this.beforeEditCache
        }
        todo.editing = false
      },
      cancelEdit(todo) {
        todo.title = this.beforeEditCache
        todo.editing = false
      },
      removeTodo(index) {
        this.todos.splice(index, 1)
      },
      checkAllTodos() {
        this.todos.forEach(todo => (todo.completed = event.target.checked))
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

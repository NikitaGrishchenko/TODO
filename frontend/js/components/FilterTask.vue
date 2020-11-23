<template>
  <div class="row">
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
</template>

<script>
  export default {
    name: 'filter-task',
    data() {
      return {
        filter: 'all'
      }
    },
    computed: {
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
    }
  }
</script>

<style lang="sass">
  .todo
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
  .active
    background: transparent
    color: #fff
    border: 1px solid #fff
</style>

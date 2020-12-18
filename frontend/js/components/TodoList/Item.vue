<template>
  <div class="todo-item d-flex justify-content-between align-items-center">
    <div class="todo-right">
      <div class="d-flex align-items-center">
        <input
          type="checkbox"
          v-model="value"
          class="todo-item__checkbox"
          @change="check"
        />
        <div
          v-if="!item.editing"
          :class="{ 'todo-item__title': true, completed: item.completed }"
          :style="{
            'border-bottom': '1px solid' + ' ' + item.priority_color
          }"
        >
          {{ item.title }}
        </div>
        <div class="d-flex" v-else>
          <input
            class="todo-item__edit"
            type="text"
            v-model="item.title"
            @keyup.esc="cancelEdit"
          />
          <button @click="doneEdit">
            Ок
          </button>
        </div>
      </div>
      <div class="todo-item__date">
        {{ format_date }}
      </div>
    </div>
    <div class="d-flex justify-content-between align-items-center">
      <div class="todo-item__change" @click="beginEdit">
        <img
          src="static/img/pencil.png"
          alt="pencil"
          class="todo-item__pencil"
        />
      </div>
      <div>
        <div class="todo-item__remove" @click="remove">
          <img
            src="static/img/times.png"
            alt="times"
            class="todo-item__times"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import moment from 'moment'

  export default {
    props: {
      item: Object
    },
    data() {
      return {
        value: Boolean
      }
    },
    mounted() {
      this.value = this.item.completed
    },
    computed: {
      format_date() {
        moment.locale('ru')
        return moment(this.item.date, 'D-M-YYYY').format('D MMMM')
      }
    },
    methods: {
      check() {
        this.$emit('check', {
          item: this.item,
          completed: this.value
        })
      },
      beginEdit() {
        this.$emit('beginEdit', this.item)
      },
      remove() {
        if (this.item.editing) {
          this.cancelEdit()
          return
        }
        this.$emit('remove', this.item)
      },
      doneEdit() {
        this.$emit('finishEdit', {
          item: this.item,
          complite: true
        })
      },
      cancelEdit() {
        this.$emit('finishEdit', {
          item: this.item,
          complite: false
        })
      }
    }
  }
</script>

<template>
  <div>
    <edit-popup
      :item="item"
      v-if="isPopupChangeVisible"
      @closePopup="closePopup"
      @doneEdit="doneEdit"
      :ru="ru"
      :format="format"
    />
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
            :class="{ 'todo-item__title': true, completed: item.completed }"
            :style="{
              'border-bottom': '1px solid' + ' ' + item.priority_color
            }"
          >
            {{ item.title }}
          </div>
        </div>
        <div class="todo-item__date">
          {{ format_date }}
        </div>
      </div>
      <div class="d-flex justify-content-between align-items-center">
        <div class="todo-item__change" @click="showPopupChange">
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
  </div>
</template>

<script>
  import moment from 'moment'
  import editPopup from '../Popup/index'

  export default {
    props: {
      item: Object,
      ru: Object,
      format: String
    },
    data() {
      return {
        value: Boolean,
        isPopupChangeVisible: false
      }
    },
    components: {
      editPopup
    },
    mounted() {
      this.value = this.item.completed
    },
    computed: {
      format_date() {
        moment.locale('ru')
        return moment(this.item.date, 'M-D-YYYY').format('D MMMM')
      }
    },
    methods: {
      showPopupChange() {
        this.isPopupChangeVisible = true
      },
      closePopup() {
        this.isPopupChangeVisible = false
      },
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

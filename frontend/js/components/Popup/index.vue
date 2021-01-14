<template>
  <transition name="modal-fade" appear>
    <div @click.self="closePopup" class="popup-wrapper">
      <div class="popup">
        <div class="popup-header d-flex justify-content-end">
          <div class="popup-header__close" @click="closePopup">
            закрыть
          </div>
        </div>
        <div class="popup-main">
          <input
            v-model="item.title"
            type="text"
            @focus="focusInputTitle(item)"
            @blur="doneEdit(item)"
          />
          <datepicker
            input-class="todo-datepicker"
            v-model="item.date"
            :language="ru"
            :monday-first="true"
            :format="format"
            @closed="doneEditDate(item)"
            @focus="focusInputDate(item)"
          ></datepicker>
          <div @click="deleteItem" class="popup-main__del">
            удалить
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import Datepicker from 'vuejs-datepicker'
  import moment from 'moment'
  import Swal from 'sweetalert2'
  export default {
    components: { Datepicker },
    name: 'edit-popup',
    props: {
      item: Object,
      ru: Object,
      format: String
    },
    computed: {
      dateItemFormat() {
        return moment(this.item.date).format()
      }
    },
    date() {
      return {
        initialItemTitle: '',
        initialItemDate: ''
      }
    },
    methods: {
      closePopup() {
        this.$emit('closePopup')
      },
      deleteItem() {
        this.$emit('deleteItem')
      },
      doneEditDate(item) {
        if (item.date != this.initialItemDate) {
          this.$emit('doneEdit')
        }
      },
      doneEdit(item) {
        if (item.title === '') {
          this.item.title = this.initialItemTitle
          return Swal.fire({
            position: 'center',
            showConfirmButton: false,
            icon: 'warning',
            title: 'Введите текст',
            timer: 1000,
            timerProgressBar: true
          })
        }
        if (this.initialItemTitle == item.title) {
          return
        } else {
          this.$emit('doneEdit')
        }
      },
      focusInputTitle(item) {
        this.initialItemTitle = item.title
      },
      focusInputDate(item) {
        this.initialItemDate = item.date
      }
    }
  }
</script>

<style lang="sass">
  .popup
    padding: 20px
    width: 500px
    min-height: 300px
    background: #fff
    z-index: 100
    border-radius: 15px
    &-wrapper
      position: fixed
      height: 100%
      width: 100%
      left: 0
      top: 0
      background: rgba(0,0,0,.6)
      z-index: 100
      display: flex
      justify-content: center
      align-items: center
      transition: all 0.2s
    & .todo-datepicker
      color: #000000 !important
    &-header
      &__close
        z-index: 200000
        cursor: pointer

  .modal-fade-enter, .modal-fade-leave-to
    opacity: 0
    transition: .1s
  .modal-fade-active, .modal-fade-leave-active
    transition: opacity .1s
</style>

<template>
  <transition name="modal-fade" appear>
    <div @dblclick.self="closePopup" class="popup-wrapper">
      <div ref="popup" class="popup">
        <div class="popup-header d-flex justify-content-between">
          <div class="popup-header__title">
            Редактировать здачу
          </div>
          <div class="popup-header__close" @click.self="closePopup">
            &times;
          </div>
        </div>
        <div class="popup-main">
          <input
            v-model="item.title"
            type="text"
            @focus="focusInputTitle(item)"
            @blur="doneEdit(item)"
            class="popup-input"
          />
          <div class="d-flex align-items-center justify-content-between mt-3">
            <datepicker
              input-class="todo-datepicker"
              v-model="item.date"
              :language="ru"
              :monday-first="true"
              :format="format"
              @input="doneEditDate(item)"
              @focus="focusInputDate(item)"
            ></datepicker>
            <div @click="deleteItem" class="popup-main__del">
              Удалить
            </div>
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
        initialItemDate: '',
        beginDelItem: true
      }
    },
    methods: {
      closePopup() {
        this.$emit('closePopup')
      },
      deleteItem() {
        this.$refs.popup.style.display = 'none'
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
    padding: 10px 13px 30px 13px
    width: 450px
    min-height: auto
    background: #fff
    border-radius: 10px
    &-input
      width: 100%
      padding: 5px
      font-size: 18px
      border-radius: 0px
      border-radius: 5px
      border: 1px solid #333
      color: #333
      outline: none
      resize: none
      overflow-y: hidden
      &:focus
        outline: 0
      &::placeholder
        color: #7B7D8A
    &-main
      display: flex
      flex-direction: column
      justify-content: space-between
      &__del
        display: block
        border: 1px solid tomato
        padding: 5px 10px
        color: #fff
        background: tomato
        border-radius: 5px
        cursor: pointer
    &-wrapper
      position: fixed
      height: 100%
      width: 100%
      left: 0
      top: 0
      background: rgba(0,0,0,.6)
      display: flex
      justify-content: center
      align-items: center
      transition: all 0.2s
      z-index: 100
    & .todo-datepicker
      color: #000000 !important
    &-header
      &__close
        cursor: pointer
        margin-bottom: 10px
      &__title
        margin: 15px 0

  .modal-fade-enter, .modal-fade-leave-to
    opacity: 0
    transition: .1s

  .modal-fade-active, .modal-fade-leave-active
    transition: opacity .1s

  .begin-item-delete
    opacity: 0
</style>

<template>
  <transition name="modal-fade">
    <div @click.self="closePopup" class="popup-wrapper">
      <div class="popup">
        <div class="popup-header d-flex justify-content-end">
          <div class="popup-header__close" @click="closePopup">
            закрыть
          </div>
        </div>
        <div class="popup-main">
          <input v-model="item.title" type="text" @blur="doneEdit" />
          <datepicker
            input-class="todo-datepicker"
            v-model="item.date"
            :language="ru"
            :monday-first="true"
            :format="format"
            @closed="doneEdit"
          ></datepicker>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import Datepicker from 'vuejs-datepicker'
  import moment from 'moment'
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
      return {}
    },
    methods: {
      closePopup() {
        this.$emit('closePopup')
      },
      doneEdit() {
        this.$emit('doneEdit')
      }
    }
    // directives: {
    //   focus: {
    //     inserted: function(el) {
    //       el.focus()
    //     }
    //   }
    // }
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
      transition: all 1s
    & .todo-datepicker
      color: #000000 !important
    &-header

  .modal-fade-enter, .modal-fade-leave-to
    opacity: 0
  .modal-fade-active, .modal-fade-leave-active
    transition: opacity .3s
</style>

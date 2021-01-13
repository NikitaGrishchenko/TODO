<template>
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
    position: fixed
    top: 50%
    left: 50%
    transform: translate(-50%,-50%)
    width: 500px
    height: 500px
    background: #f3f3f3
    z-index: 100
    & .todo-datepicker
      color: #000000 !important
    &-header
</style>

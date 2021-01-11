import $ from 'jquery'

$(function() {
  $('#password1').tooltip({
    trigger: 'focus',
    title:
      'В пароле должна присутствовать хотя бы одна цифра и одна заглавная буква. (Вы так же можете использовать спецсимволы: $,%,#,^) (минимум 8 символов)',
    placement: 'right'
  }),
    $('.sidebar-user').tooltip({
      trigger: 'hover',
      title: 'Личный кабинет в разработке',
      placement: 'right',
      delay: { show: 500, hide: 3000 }
    })
})

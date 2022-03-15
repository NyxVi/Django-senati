class ValidateForm {
  constructor(form, options) {
    this.form = form
    this.options = options
    this.elements = { text: [], number: [] }
    this.app()
  }
  validateNumber(value = '') {
    if (value === '') return false
    const is_valid = /^[0-9]*$/.test(value)
    return is_valid
  }
  app() {
    if (this.options.number) {
      this.elements.number = this.form.querySelectorAll('.input-number')
    }
    if (this.options.text) {
      this.elements.text = this.form.querySelectorAll('.input-text')
    }
    this.form.addEventListener('submit', e => {
      e.preventDefault()
      const is_valid = this.validate()
      if (is_valid) {
        this.form.submit()
      }
    })
    if (this.options.validateOnWriting) {
      this.elements.number.forEach(input => {
        input.addEventListener('keyup', e => {
          const lastValue = input.value.slice(-1)
          let val = this.validateNumber(lastValue)
          if (!val) input.value = input.value.slice(0, -1)
        })
      })
    }
  }
  validate() {
    let errors = true
    this.elements.number.forEach(input => {
      errors = errors === true ? this.validateNumber(input.value) : false
    })
    return errors
  }
}
export { ValidateForm }

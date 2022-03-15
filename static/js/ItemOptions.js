class ItemOptions {
  constructor({ element }) {
    this.element = element
    this.options = this.element.querySelector('.itemOptions-options')
    this.state = 'disabled' //activate
    this.run()
  }
  run() {
    this.element.addEventListener('click', e => {
      if (this.state === 'disabled') {
        this.state = 'activate'
        this.options.style.display = 'block'
        const prov = e => {
          const contain = this.element.contains(e.target)
          if (
            !contain ||
            e.target.classList.contains('itemOptions-item_link')
          ) {
            this.state = 'disabled'
            this.options.style.display = 'none'
            window.removeEventListener('click', prov)
          }
        }
        window.addEventListener('click', prov)
      }
    })
  }
}
export { ItemOptions }

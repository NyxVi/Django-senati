class Carousel {
  constructor({ element }) {
    this.element = element
    this.container = this.element.querySelector('.carousel-container')
    this.shadowLeft = this.element.querySelector('.carousel-shadow-left')
    this.shadowRight = this.element.querySelector('.carousel-shadow-right')

    this.state = {
      countTransform: 0,
      widthContainer: this.container.offsetWidth,
      witdhElement: this.element.offsetWidth
    }
    this.run()
  }
  _shadowLeftDisplay(value) {
    this.shadowLeft.style.display = value
  }
  _shadowRighttDisplay(value) {
    this.shadowRight.style.display = value
  }
  actions() {
    const back = this.element.querySelector('.carousel-action-back')
    const next = this.element.querySelector('.carousel-action-next')
    back.addEventListener('click', () => {
      if (this.state.countTransform < 0) {
        this.state.countTransform += this.state.witdhElement
        this._shadowRighttDisplay('initial')
        this.container.style.transform = `translateX(${this.state.countTransform}px)`
      }
      if (this.state.countTransform + this.state.witdhElement > 0)
        this._shadowLeftDisplay('none')
    })
    next.addEventListener('click', () => {
      let yea = this.state.countTransform - this.state.witdhElement
      if (yea > this.state.widthContainer * -1) {
        this.state.countTransform = yea
        this._shadowLeftDisplay('initial')
        this.container.style.transform = `translateX(${this.state.countTransform}px)`
      }
      if (
        this.state.countTransform * -1 + this.state.witdhElement >
        this.state.widthContainer
      )
        this._shadowRighttDisplay('none')
    })
  }
  run() {
    this._shadowLeftDisplay('none')
    this.actions()
  }
}

export { Carousel }

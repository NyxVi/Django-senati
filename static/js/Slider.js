class Slider {
  constructor({ element, settings = {} }) {
    this.element = element
    this.images = element.querySelectorAll('.slider-img')
    this.settings = settings
    this.state = {
      previusImg: 0,
      currentImg: settings?.start ?? 0,
      currentImgObservers: [this._managerNavigation],
      totalImg: this.images.length,
      containerState: 'still', // back, next, still
      intervalAnimation: null
    }
    this.setCurrentImg = number => {
      this.state.currentImg = number
      this.state.currentImgObservers.forEach(elm => {
        elm.bind(this)()
      })
    }
    this.run()
  }
  run() {
    this.images[this.state.currentImg].classList.add('is-active')
    this.actions()
    this.configure_settings()
  }
  actions() {
    const next = this.element.querySelector('.slider-action-next')
    const back = this.element.querySelector('.slider-action-back')
    if (next)
      next.addEventListener('click', () => {
        this.next()
      })
    if (back)
      back.addEventListener('click', () => {
        this.back()
      })
    const container = this.element.querySelector('.slider-container')

    container.addEventListener('animationend', () => {
      let direction = this.state.containerState
      let pImg = this.state.previusImg
      this.images[pImg].classList.remove('is-active')
      container.classList.remove(`is-moving-${direction}`)
      this.images[this.state.currentImg].classList.remove(
        `is-active-${direction}`
      )
      this.state.containerState = 'still'
      this._setAutomaticAnimation()
    })
  }
  _setAutomaticAnimation() {
    if (this.settings.automatic) {
      this.state.intervalAnimation = setInterval(() => {
        this.next()
      }, this.settings.time || 3000)
    }
  }
  _managerNavigation() {
    if (!this.settings.navigation) return
    let list = this.navigation.querySelectorAll('span')
    list[this.state.currentImg].classList.add('is-active')
    list[this.state.previusImg].classList.remove('is-active')
  }
  configure_settings() {
    this._setAutomaticAnimation()
    if (this.settings.navigation) {
      this.navigation = this.element.querySelector('.slider-navigation')
      for (let i = 0; i < this.state.totalImg; i++) {
        let span = document.createElement('span')
        span.className = `slider-navigation-item ${
          this.state.currentImg === i ? 'is-active' : ''
        }`
        span.addEventListener('click', () => {
          if (i < this.state.currentImg) this.back(i)
          else if (i > this.state.currentImg) this.next(i)
          else {
            if (this.state.intervalAnimation) {
              clearInterval(this.state.intervalAnimation)
              this._setAutomaticAnimation()
            }
          }
        })
        this.navigation.appendChild(span)
      }
    }
  }

  next(specific) {
    if (this.state.intervalAnimation) {
      clearInterval(this.state.intervalAnimation)
    }
    if (this.state.containerState != 'still') return ''
    this.state.previusImg = this.state.currentImg
    let maybe_next = 0
    if (this.state.previusImg + 1 >= this.state.totalImg) maybe_next = 0
    else if (specific != undefined) maybe_next = specific
    else maybe_next = this.state.previusImg + 1
    this.state.containerState = 'next'
    this.setCurrentImg(maybe_next)
    this.images[this.state.currentImg].className =
      'slider-img is-active is-active-next'
    this.element
      .querySelector('.slider-container')
      .classList.add('is-moving-next')
  }
  back(specific) {
    if (this.state.intervalAnimation) {
      clearInterval(this.state.intervalAnimation)
    }
    if (this.state.containerState != 'still') return ''
    this.state.previusImg = this.state.currentImg
    let maybe_back = 0
    if (this.state.previusImg - 1 < 0) maybe_back = this.state.totalImg - 1
    else if (specific != undefined) maybe_back = specific
    else maybe_back = this.state.currentImg - 1

    this.setCurrentImg(maybe_back)
    this.state.containerState = 'back'
    this.images[this.state.currentImg].className =
      'slider-img is-active is-active-back'
    this.element
      .querySelector('.slider-container')
      .classList.add('is-moving-back')
  }
  getNodes() {
    return { element: this.element, images: this.image }
  }
}

export { Slider }

import { Slider } from './Slider.js'
import { Carousel } from './Carousel.js'
import { ItemOptions } from './ItemOptions.js'

const elementHero = document.getElementById('slider-home')
const novedades = document.getElementById('carousel-novedades')
const menuUser = document.getElementById('menu-user')
const menuCart = document.getElementById('menu-cart')

const sliderHero = new Slider({
  element: elementHero,
  settings: {
    automatic: true,
    // time: 500,
    navigation: true
  }
})
const novedadesCarousel = new Carousel({ element: novedades })

new ItemOptions({ element: menuUser })
new ItemOptions({ element: menuCart })

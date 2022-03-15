import { ItemOptions } from './ItemOptions.js'

const menuUser = document.getElementById('menu-user')
const menuCart = document.getElementById('menu-cart')

new ItemOptions({ element: menuUser })
new ItemOptions({ element: menuCart })

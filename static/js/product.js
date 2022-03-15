import { ItemOptions } from './ItemOptions.js'
import { ValidateForm } from './ValidateForm.js'

const menuUser = document.getElementById('menu-user')
const menuCart = document.getElementById('menu-cart')
const formCart = document.getElementById('formCart')

new ItemOptions({ element: menuUser })
new ItemOptions({ element: menuCart })
new ValidateForm(formCart, { number: true, validateOnWriting: true })

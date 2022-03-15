const elements = document.querySelectorAll('.js-img')
const showImg = document.getElementById('show-img')
const showImgClose = document.getElementById('show-img-close')
const imgElement = document.getElementById('img-element')
showImgClose.addEventListener('click', () => {
  showImg.style.display = 'none'
  imgElement.src = ''
})
elements.forEach(element =>
  element.addEventListener('click', () => {
    imgElement.src = element.getAttribute('data-url')
    showImg.style.display = 'flex'
  })
)

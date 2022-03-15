const inputFile = document.getElementById('input-file')
const inputFileImg = document.getElementById('input-file-img')

function verifyFile() {
  if (inputFile.files.length > 0) {
    let url = URL.createObjectURL(inputFile.files[0])
    inputFileImg.src = url
  }
}
verifyFile()
inputFile.addEventListener('change', e => {
  verifyFile()
})

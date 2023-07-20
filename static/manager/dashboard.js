const sideBar = document.querySelector('.sideBar')
const main = document.querySelector('.main')

const toggleSideBar = () => {
  sideBar.classList.toggle('change')
  main.classList.toggle('change')
}

document.querySelectorAll('.stat').forEach((el,i)=>{
  anime({
    targets : el,
    translateY : [40,0],
    duration : 1000,
    opacity : [0,1],
    delay : 100 * i
  })
})

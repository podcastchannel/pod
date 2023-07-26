let topAnimeEl = []
topAnimeEl.push(document.getElementById('logo'))
topAnimeEl.push(document.querySelector('.logo_box'))
topAnimeEl.push(document.querySelectorAll('.player_box')[0])
topAnimeEl.push(document.querySelector('.next_box'))
topAnimeEl.push(document.querySelectorAll('.player_box')[1])

topAnimeEl.forEach((el, i) => {
  anime({
    targets: el,
    opacity: [0, 1],
    duration: 1500,
    delay: i * 200,
    translateX: [-50, 0]

  })
})


anime({
  loop: true,
  duration: 3000,
  targets: '#clock',
  rotate: [0, 360],
  opacity: [0, 1]
})

document.querySelectorAll('.item_box i').forEach((el, i) => {
  anime({
    targets: el,
    delay: i * 50,
    translateY: [-30, 0],
    opacity: [0, 1]
  })
})

document.querySelectorAll('.news_box .stack-card').forEach((el, i) => {
  anime({
    targets: el,
    delay: i * 50,
    translateY: [100, 0],
    opacity: [0, 1]
  })
})


let Lineup_tags = ['Up Next', 'Later', 'Still to come']
const radio_tags = document.querySelectorAll('.radio_tag')
radio_tags.forEach((radio, i) => {
  radio.innerHTML = Lineup_tags[i]
})

const info_holder = document.querySelector('.head_box .right')
const page = document.querySelector('.page')




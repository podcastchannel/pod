const addImage = (el, el_p) => {
  const [file] = el.files
  var src = URL.createObjectURL(file)
  el_p.style.backgroundImage = `url(${src})`
}

const main_cover = document.querySelector('.main_cover')
const add_program_box = document.querySelector('.add_program_box')

const day_box = document.querySelector('.day_box')

let program_list = JSON.parse(day_box.dataset.program_list)



program_list.forEach((el, i) => {
  const pro_box = document.querySelector('.program_box')

  pro_box.innerHTML += `
      <div class="program" data-name="${el.name}">
        <div class="img_box" style="background-image: url(${el.image_url});"></div>
        <p>
          <strong>${el.name}</strong>
          <span>${el.description.substring(0, 100)}</span>
          <small><i class="material-symbols-outlined">event</i> ${createRealDate(new Date(el.start_date))} </small>
        </p>
        <p style="flex-direction: row;">
          <i class="material-symbols-outlined" onclick="toggleProgramForm(event.target, ${el.id})" style="font-size: 1.6rem;">edit</i>
          <i class="material-symbols-outlined" onclick="delete_program(event.target, ${el.id}, '${el.name}')" style="font-size: 1.6rem;">delete</i>
        </p>
      </div>
    `
})


const program_form = document.getElementById('program_form')

const toggleProgramForm = (el, el_id) => {
  if (el) {
    document.getElementById('program_type').innerHTML = 'New Announcement'
  }

  if (el_id) {
    program_list.forEach(prog => {
      if (prog.id === el_id) {
        document.querySelector('input[name="id"]').value = prog.id
        document.getElementById('program_type').innerHTML = 'Edit Announcement'
        document.querySelector('input[name="name"]').value = prog.name
        document.querySelector('textarea[name="description"]').value = prog.description
        document.querySelector('.img_box').style.backgroundImage = `url(${prog.image_url})`
        document.querySelector('textarea[name="share_link"]').value = prog.share_link
        document.querySelector('textarea[name="social_accounts"]').value = prog.social_accounts
      }
    })
  }

  if (add_program_box.classList.contains('change')) {
    document.querySelector('.img_box').style.backgroundImage = '';
    [...program_form.elements].forEach(el => {
      el.value = ''
    })
  }

  add_program_box.classList.toggle('change')
  main_cover.classList.toggle('change')
}

const prompt_box = document.querySelector('.prompt_box')

const days = document.querySelectorAll('.day')

const filterDay = (val) => {
  if (val === 'all') {
    days.forEach(day => {
      day.style.display = 'flex'
    })
  } else {
    days.forEach(day => {
      if (day.dataset.name === val) {
        day.style.display = 'flex'
      } else {
        day.style.display = 'none'
      }
    })
  }
}

const programs = document.querySelectorAll('.program')

const searchProgram = (val) => {
  var results = 0
  programs.forEach(program => {
    if (program.dataset.name) {
      if (program.dataset.name.toLowerCase().includes(val)) {
        runSearchAnime(program)
        program.style.display = 'flex'
        results += 1
      } else {
        program.style.display = 'none'
      }
    }
  })
  document.querySelector('.search_box h4').innerHTML = `${results} Results`
}



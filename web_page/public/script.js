const url = new URL(window.location.href)
const ip = url.host.split(':')[0]

let ws = new WebSocket(`ws://${ip}:8765`);

let isTrust = false

setInterval(keep_alive, 10000)

function movement(ele, event, data) {
  try {
    ws.send(JSON.stringify({
      type: 'movement',
      data
    }))
  } catch(err) {
    console.error(err)
  }
  ele?.classList?.add("button-touched")

  if(!isTrust) return

  const audio = document.createElement("audio")
  audio.src = `${data}.mp3`
  audio.play()
  plusOne(event)
  window.navigator.vibrate(20)
}

function topMachine(ele, event, data) {
  try {
    ws.send(JSON.stringify({
      type: 'top_machine',
      data
    }))
  } catch(err) {
    console.error(err)
  }
  ele?.classList?.add("button-touched")

  if(!isTrust) return

  const audio = document.createElement("audio")
  audio.src = `${data}.mp3`
  audio.play()
  plusOne(event)
  window.navigator.vibrate(20)
}

function topMachineTouchEnd(ele) {
  try {
    ws.send(JSON.stringify({
      type: 'top_machine',
      data: 'stop'
    }))
  } catch(err) {
    console.error(err)
  }
  ele.classList.remove("button-touched")
  isTrust = true
}

function arduinoTestHigh(ele, event, _data) {
  try {
    ws.send(JSON.stringify({
      type: 'arduino',
      "data": '{"pin": 13, "state": 1}'
    }))
  } catch(err) {
    console.error(err)
  }
  ele?.classList?.add("button-touched")

  if(!isTrust) return

  plusOne(event)
  window.navigator.vibrate(20)
}

function arduinoTestLow(ele, event, _data) {
  try {
    ws.send(JSON.stringify({
      type: 'arduino',
      "data": '{"pin": 13, "state": 0}'
    }))
  } catch(err) {
    console.error(err)
  }
  ele?.classList?.add("button-touched")

  if(!isTrust) return

  plusOne(event)
  window.navigator.vibrate(20)
}


function movementTouchEnd(ele) {
  try {
    ws.send(JSON.stringify({
      type: 'movement',
      data: 'stop'
    }))
  } catch(err) {
    console.error(err)
  }
  ele.classList.remove("button-touched")
  isTrust = true
}

function basicTouchEnd(ele) {
  ele.classList.remove("button-touched")
  isTrust = true
}

function plusOne(event) {
  console.log(event)
  let x = event.targetTouches[0].clientX + 10;
  let y = event.targetTouches[0].clientY - 30;

  let element = document.createElement('span')
  element.innerHTML = '功德 +1'
  element.setAttribute("style", `position: fixed;top: ${y}px;left: ${x}px;`)
  document.body.appendChild(element)
  element.setAttribute("class", "plus-one")

  setTimeout(() => {
    element.remove()
  }, 900)
}

function keep_alive() {
  try{
    ws.send(JSON.stringify({
      type: 'ping'
    }))
  } catch(err) {
    ws = new WebSocket(`ws://${ip}:8765`);
  }
}
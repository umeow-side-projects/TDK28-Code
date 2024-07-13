const express = require("express")
const fs = require("fs")

const app = express()

app.use(express.static('public'));

app.get('/', async (req, res) => {
  const controlHtml = fs.readFileSync(__dirname + '/control.html', encoding='utf8')
  res.send(controlHtml)
})

app.listen(3000, '0.0.0.0', () => {
  console.log("webserver start!")
})
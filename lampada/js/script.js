//dom

const lampada = document.querySelector('#lampada')
const btligar = document.querySelector('#btligar')
const btdesligar = document.querySelector('#btdesligar')

//evento

btligar.addEventListener('click',acender)
btdesligar.addEventListener('click',apagar)
lampada.addEventListener('dblclick',quebrar)

//função

function acender(){
    lampada.src = 'images/acesa.gif'

}
function apagar(){
    lampada.src = 'images/apagada.gif'

}
function quebrar(){
    lampada.src = 'images/quebrada.jpg'
 }
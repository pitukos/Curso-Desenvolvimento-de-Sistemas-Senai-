//dom

const alvo = document.querySelector('#alvo')
const btalegria = document.querySelector('#btalegria')
const bttristeza = document.querySelector('#bttristeza')
const btnojinho = document.querySelector('#btnojinho')
const btraiva = document.querySelector('#btraiva')

//eventos

btalegria.addEventListener('click',alegria)
bttristeza.addEventListener('click',tristeza)
btnojinho.addEventListener('click',nojinho)
btraiva.addEventListener('click',raiva)
//funções

function alegria(){
    alvo.src = 'images/02.png'
}
function tristeza(){
    alvo.src = 'images/04.png'
}
function nojinho(){
    alvo.src = 'images/03.png'
}
function raiva(){
    alvo.src = 'images/01.png'
}
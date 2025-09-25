//dom

const alvo = document.querySelector('#alvo')
const btshinra = document.querySelector('#btshinra')
const btsho = document.querySelector('#btsho')
const btbenimaru = document.querySelector('#btbenimaru')
const btburns = document.querySelector('#btburns')
const btogun = document.querySelector('#btogun')
const btcharon = document.querySelector('#btcharon')
const btarthur = document.querySelector('#btarthur')
const btevangelist = document.querySelector('#btevangelist')
const bthaumea = document.querySelector('#bthaumea')
const btjoker = document.querySelector('#btjoker')

//eventos

btshinra.addEventListener('click',Shinra)
btsho.addEventListener('click',Sho)
btbenimaru.addEventListener('click',Benimaru)
btburns.addEventListener('click',Burns)
btogun.addEventListener('click',Maki)
btcharon.addEventListener('click',Hibana)
btarthur.addEventListener('click',Arthur)
btevangelist.addEventListener('click',Iris)
bthaumea.addEventListener('click',Haumea)
btjoker.addEventListener('click',Joker)
//funções

function Shinra(){
    alvo.src = 'images/Shinra.png'
}
function Sho(){
    alvo.src = 'images/SHO.png'
}
function Benimaru(){
    alvo.src = 'images/Benimaru.png'
}
function Burns(){
    alvo.src = 'images/Burns.png'
}
function Maki(){
    alvo.src = 'images/Maki.png'
}
function Hibana(){
    alvo.src = 'images/Hibana.png'
}
function Arthur(){
    alvo.src = 'images/Arthur.png'
}
function Iris(){
    alvo.src = 'images/Iris.png'
}
function Haumea(){
    alvo.src = 'images/Haumea.png'
}
function Joker(){
    alvo.src = 'images/Joker.png'
}
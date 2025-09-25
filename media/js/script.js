//dom

const nome= document.querySelector('#nome')
const uni1= document.querySelector('#uni1')
const uni2= document.querySelector('#uni2')
const uni3= document.querySelector('#uni3')
const uni4= document.querySelector('#uni4')
const botao= document.querySelector('#botao')
const resultado= document.querySelector('#resultado')

//evento

botao.addEventListener('click',calculo)

//função
function calculo(){
    x1 = Number(uni1.value);
    x2 = Number(uni2.value);
    x3 = Number(uni3.value);
    x4 = Number(uni4.value);
    nume = nome.value
    y = String
    media = (x1+x2+x3+x4)/4;
if (media<=6){
    y = 'reprovado'
}
else{
    y = 'aprovado' 
}
resultado.textContent = `Aluno(a) ${nume}, a sua média é ${media.toFixed(2)}, você foi ${y}!`

}
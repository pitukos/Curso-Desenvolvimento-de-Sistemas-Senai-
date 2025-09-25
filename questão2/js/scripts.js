//dom
const peso= document.querySelector('#peso')
const altura= document.querySelector('#altura')
const calculate= document.querySelector('#calculate')
const botao= document.querySelector('#resultado')
//event
calculate.addEventListener('click',imc)
//função
function imc(){
    p = Number(peso.value)
    a = Number(altura.value)

    calculo = (p/(a*a))

    if (calculo <18,5)
        botao.textContent=`O seu IMC é de ${calculo.toFixed(2)} você é magro`
    if (25<calculo >18,5)
        botao.textContent=`O seu IMC é de ${calculo.toFixed(2)} você esta no peso ideal`
    if (30<calculo>25)
        botao.textContent=`O seu IMC é de ${calculo.toFixed(2)} você esta acima do peso`
    if (calculo>30)
        botao.textContent=`O seu IMC é de ${calculo.toFixed(2)} você é obeso`
}
const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const seletor = document.querySelector("#operacao");
const botao = document.querySelector("#igual");
let resposta = document.querySelector("#resposta");

botao.addEventListener("click", e => {
    const valor1 = parseInt(campo1.value);
    const valor2 = parseInt(campo2.value);

    const operacao = seletor.value;

    if (operacao == "soma") {
        resposta.innerHTML = valor1 + valor2;
    } else if(operacao == "subtracao") {
        resposta.innerHTML = valor1 - valor2;
    } else if (operacao == "multiplicacao") {
        resposta.innerHTML = valor1 * valor2;
    } else if (operacao == "divisao") {
        resposta.innerHTML = valor1 / valor2;
    }


})


let idade;
let primeiroNome;
let nome = "Lucas";

console.log(typeof nome)

idade = 30;
let maioridade = idade >= 18;

//nome = "Luigi";

//let mensagem = "Olá, " + nome + ".";

let mensagem = `Olá, ${nome}. Sua idade é ${idade} anos. 
Seja muito bem-vindo!`;

if(maioridade) {
    console.log(mensagem);
} else {
    console.log("Você não pode entrar no site.");
}

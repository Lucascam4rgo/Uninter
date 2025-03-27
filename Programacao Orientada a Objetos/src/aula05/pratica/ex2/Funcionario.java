package aula05.pratica.ex2;

import java.math.BigInteger;

public class Funcionario implements Imprimivel{
    String cpf;
    String nome;
    String telefone;

    public Funcionario(String cpf, String nome, String telefone) {
        this.cpf = cpf;
        this.nome = nome;
        this.telefone = telefone;
    }

    @Override
    public void imprimir() {
        System.out.println("CPF: " + cpf);
        System.out.println("Nome: " + nome);
        System.out.println("Telefone: " + telefone);
        System.out.println();
    }
}

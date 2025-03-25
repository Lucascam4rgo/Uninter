package aula02classesobjetos.pratica.ex2;

import java.util.Scanner;

public class Conta {

    int numero;
    String titular;
    float saldo;
    float limite;

    public Conta(int numero, String titular, float saldo, float limite) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
        this.limite = limite;
    }

    public boolean sacar (float saque) {
        if (saque > saldo || saque > limite) {
            System.out.println("Saldo/limite indisponível");
            return false;
        }

        saldo -= saque;
        return true;
    }

    public boolean deposita (float deposito) {
        if (deposito < 0) {
            return false;
        }

        saldo += deposito;
        return true;
    }

    boolean transferencia (float valorTransferencia, Conta conta) {
        if (valorTransferencia > saldo || valorTransferencia < 0) {
            System.out.println("Falha na transferência, tente novamente!");
            return false;
        }

        this.saldo -= valorTransferencia;

        conta.saldo += valorTransferencia;
        return true;
    }

    void info() {
        System.out.println("Número da conta: " + numero);
        System.out.println("Titular da conta: " + titular);
        System.out.println("Saldo da conta: " + saldo);
        System.out.println("Limite da conta: " + limite);
        System.out.println();
    }
}

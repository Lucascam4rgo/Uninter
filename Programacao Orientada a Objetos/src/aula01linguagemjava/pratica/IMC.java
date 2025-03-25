package aula01linguagemjava.pratica;

import java.util.Scanner;

public class IMC {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite seu peso: ");
        int peso = teclado.nextInt();

        System.out.println("Digite sua altura: ");
        double altura = teclado.nextDouble();

        double imc = peso / Math.pow(altura, 2);

        System.out.println("Agora, digite seu nome: ");
        String nome = teclado.next();

        System.out.printf("%s, seu IMC é : %.2f", nome, imc);

    }

}

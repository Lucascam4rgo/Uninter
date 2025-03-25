package aula01linguagemjava.teorica;

import java.util.Arrays;
import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {

        int idade = 10;

        idade += 2;
        String nome = "Mario";
        double peso = 72.5;
        float peso2 = 80.6f;

        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite nome, idade e peso: ");

        nome = teclado.nextLine();
        idade = teclado.nextInt();
        peso = teclado.nextFloat();

        System.out.println();

        System.out.println("Nome: " + nome);
        System.out.printf("Idade: %d\n", idade);
        System.out.printf("Peso: %.2f\n", peso);

        if (idade < 18) {
            System.out.println("Acesso Bloqueado");
        }
        else if (idade < 65) {
            System.out.println("Adulto");
        }
        else {
            System.out.println("Adulto idoso");
        }

        //while () {

        //}

        for (int i=0;i<10; i++) {
            System.out.println("Valor: " + i);
        }

        //array
        //lista

        int[] megaSena = {11, 14, 21, 30, 37, 56};
        int[] numeros = new int[200];

        numeros[60] = 50;

        megaSena[0] = 10;

        System.out.println(Arrays.toString(megaSena));
        System.out.println(Arrays.toString(numeros));
    }

}

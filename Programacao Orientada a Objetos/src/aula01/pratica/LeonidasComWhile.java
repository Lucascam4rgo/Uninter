package aula01.pratica;

import java.util.Scanner;

public class LeonidasComWhile {

    public static void main(String[] args) {

        System.out.println("------" + "JOGO DE ADIVINHAÇÃO - LEÔNIDAS " + "------");

        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite quantos soldados você acha que os 300 irão enfrentar: ");
        int numSoldados = teclado.nextInt();
        String msg;

        while(numSoldados != 10000) {

            msg = numSoldados>10000?"Um pouco menos":"Um pouco mais";

            /*if (numSoldados > 10000) {
                System.out.println("Um pouco menos...");
            }
            else {
                System.out.println("Um pouco mais...");
            }*/

            System.out.println(msg);
            System.out.println("Tente novamente: ");
            numSoldados = teclado.nextInt();
        }
        System.out.println("Parabéns, você acertou!!");
    }

}

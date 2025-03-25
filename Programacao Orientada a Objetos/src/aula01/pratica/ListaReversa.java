package aula01.pratica;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class ListaReversa {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 9, 29, 78};

        System.out.println(numeros[4]);
        System.out.println(numeros[3]);
        System.out.println(numeros[2]);
        System.out.println(numeros[1]);
        System.out.println(numeros[0]);

        //modo convencional

        Scanner teclado = new Scanner(System.in);

        ArrayList<String> listadenomes = new ArrayList<String>();

        System.out.println("Digite a quantidade de nomes: ");
        int qtd = teclado.nextInt();

        for (int i = 0; i < qtd; i++) {
            listadenomes.add(teclado.next());
        }

        for (int i=listadenomes.size()-1; i>=0;i--) {
            System.out.println(listadenomes.get(i));
        } // forma sem collections

        // Com collections
        Collections.reverse(listadenomes);


        //Modo diferenciado com arraylist




    }

}

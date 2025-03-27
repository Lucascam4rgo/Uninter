package aula05.pratica.ex1;

import java.util.ArrayList;

public class Principal {

    public static void main(String[] args) {

        Desktop desk = new Desktop(16, 4, 2);

        Notebook note = new Notebook(8, 2, 11);

        Computador computador;

        ArrayList<Computador> listaComputadores = new ArrayList<>();

        listaComputadores.add(desk);
        listaComputadores.add(note);
        listaComputadores.add(new Desktop(16, 8, 12));
        listaComputadores.add(new Notebook(16, 8, 18));

        double total = 0;

        for (Computador c: listaComputadores) {
            total += c.calculaValor();
        }
        System.out.printf("R$ %.2f \n", total);

        System.out.println("---------------------------");

        computador = desk;

        System.out.printf("R$ %.2f \n", computador.calculaValor());

        System.out.println("---------------------------");

        computador = note;

        System.out.printf("R$ %.2f \n", computador.calculaValor());

    }

}

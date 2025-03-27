package aula05.pratica.ex2;

import java.util.ArrayList;

public class Principal {

    public static void main(String[] args) {
        Imprimivel func = new Funcionario("444.111.111-99", "Kun", "11944449999");

        Imprimivel c = new Carro("Hyundai", "Cinza", 4);

        Imprimivel protagonista = new Protagonistas("Monkey D. Luffy", "One Piece", "Virar Borracha");

        func.imprimir();

        c.imprimir();

        protagonista.imprimir();

        ArrayList<Imprimivel> lista = new ArrayList<>();

        lista.add(func);
        lista.add(c);
        lista.add(protagonista);

        for (Imprimivel i : lista) {
            i.imprimir();
        }

    }

}

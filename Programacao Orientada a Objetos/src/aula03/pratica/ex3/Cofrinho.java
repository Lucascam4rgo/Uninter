package aula03.pratica.ex3;

import java.util.ArrayList;

public class Cofrinho {

    ArrayList<Moeda> listaMoeda = new ArrayList<>();

    public Cofrinho() {

    }

    public void adicionar(Moeda moeda) {
        listaMoeda.add(moeda);
    }

    public double calcularTotal() {
        double total = 0;
        for (Moeda m : listaMoeda) {
            total += m.getValor();
        }
        return total;
    }
}

package aula03.pratica.ex3;

public class Principal {

    public static void main(String[] args) {
        Cofrinho c = new Cofrinho();

        c.adicionar(new Moeda(1.5,"Euro"));
        c.adicionar(new Moeda(1.0,"Dólar"));
        c.adicionar(new Moeda(0.5,"Real"));
        c.adicionar(new Moeda(0.2,"Peso"));

        System.out.println(c.calcularTotal());
    }

}

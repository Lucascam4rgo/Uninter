package aula04.pratica.ex2;

public class Principal {
    public static void main(String[] args) {
        Ingresso ingresso = new Ingresso("Comic Con", 300);

        IngressoVip ingressoVip = new IngressoVip("Comic Con", 300, 50);

        ingresso.imprimir();
        System.out.println();
        ingressoVip.imprimir();
    }
}

package aula02.pratica.ex2;

public class Principal {

    public static void main(String[] args) {

        Conta c1 = new Conta(1001, "Lucas Camargo", 2000, 700);
        Conta c2 = new Conta(1005, "Andreia Camargo", 1200, 400);

        c1.transferencia(2300, c2);

        c1.info();
        c2.info();

        /*c1.sacar(800);


        if(!c1.deposita(-150)) {
            System.out.println("Problema ao depositar, depósito negativo");
        }
        c1.info();*/



    }
}

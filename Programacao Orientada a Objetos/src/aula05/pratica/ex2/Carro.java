package aula05.pratica.ex2;

public class Carro implements Imprimivel{
    String marca;
    String cor;
    int portas;

    public Carro(String marca, String cor, int portas) {
        this.marca = marca;
        this.cor = cor;
        this.portas = portas;
    }

    @Override
    public void imprimir() {
        System.out.println("Marca: " + marca);
        System.out.println("Cor: " + cor);
        System.out.println("Portas: " + portas);
        System.out.println();
    }
}

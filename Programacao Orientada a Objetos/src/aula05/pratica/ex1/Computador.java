package aula05.pratica.ex1;

public abstract class Computador implements Imprimivel {

    int gbMemoria;
    int numProcessadores;

    public Computador(int gbMemoria, int numProcessadores) {
        this.gbMemoria = gbMemoria;
        this.numProcessadores = numProcessadores;
    }

    public abstract double calculaValor();

    @Override
    public void imprimir() {
        System.out.println("Memória RAM (GB): " + gbMemoria);
        System.out.println("Número de Processadores: " + numProcessadores);
    }

}

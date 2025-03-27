package aula05.pratica.ex1;

public class Desktop extends Computador implements Imprimivel {

    double acessorios;

    public Desktop(int gbMemoria, int numProcessadores, double acessorios) {
        super(gbMemoria, numProcessadores);
        this.acessorios = acessorios;
    }

    @Override
    public double calculaValor() {
        //System.out.println("O valor do Desktop é: ");
        return gbMemoria * 200 + numProcessadores * 400 + acessorios;
    }

    @Override
    public void imprimir() {
        super.imprimir();
        System.out.println("Acessórios: " + acessorios);
    }
}

package aula05.pratica.ex1;

public class Notebook extends Computador implements Imprimivel{

    int polegadasTela;

    public Notebook(int gbMemoria, int numProcessadores, int polegadasTela) {
        super(gbMemoria, numProcessadores);
        this.polegadasTela = polegadasTela;
    }

    @Override
    public double calculaValor() {
        //System.out.println("O valor do Notebook é: ");
        return gbMemoria * 250 + numProcessadores * 500 + polegadasTela * 100;
    }

    @Override
    public void imprimir() {
        super.imprimir();
        System.out.println("Polegadas: " + polegadasTela);
    }

}

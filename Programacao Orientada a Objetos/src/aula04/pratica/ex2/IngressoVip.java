package aula04.pratica.ex2;

public class IngressoVip extends Ingresso{

    public double adicional;

    public IngressoVip(String nomeEvento, double valor, double adicional) {
        super(nomeEvento, valor);
        this.adicional = adicional;
    }

    @Override
    public void imprimir() {
        super.imprimir();
        System.out.println("Adicional no preço do ingresso: " + adicional);
        System.out.println("Total do Ingresso: " + String.format("%.2f", (valor + adicional)));
    }
}

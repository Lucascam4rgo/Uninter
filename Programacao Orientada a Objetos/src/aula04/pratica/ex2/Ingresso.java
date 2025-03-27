package aula04.pratica.ex2;

public class Ingresso {

    public String nomeEvento;
    public double valor;

    public Ingresso(String nomeEvento, double valor) {
        this.nomeEvento = nomeEvento;
        this.valor = valor;
    }

    public void imprimir() {
        System.out.println("Nome do evento: " + nomeEvento);
        System.out.println("Valor do evento: " + String.format("%.2f", valor));
        //DecimalFormat df = new DecimalFormat("#.##");
        //System.out.println("Valor do evento: " + df.format(valor));
    }

}

package aula03.teorica.encapsulamento;

public class Horario {
    private int hora;
    private int minuto;
    private int segundo;

    public void setHora(int hora) {
        if (hora>=0 && hora <=23) {
            this.hora = hora;
        }
        else {
            System.out.println("Hora inválida");
        }
    }

    public int getHora() {
        return hora;
    }

    public int getMinuto() {
        return minuto;
    }

    public void setMinuto(int minuto) {
        if(minuto >= 0 && minuto <= 59) {
            this.minuto = minuto;
        }
        else {
            System.out.println("Minutos inválidos");
        }
    }

    public int getSegundo() {
        return segundo;
    }

    public void setSegundo(int segundo) {
        if(segundo >= 0 && segundo <= 59) {
            this.segundo = segundo;
        }
        else {
            System.out.println("Segundos inválidos");
        }
    }
}

package aula02.pratica.ex1;

import java.text.DecimalFormat;

public class Avaliacao {

    float nota1;
    float nota2;
    float nota3;

    public Avaliacao() {
    }

    public Avaliacao(float nota1, float nota2, float nota3) {
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }

    public String mediaAritmetica () {
        DecimalFormat df = new DecimalFormat("#.##");
        return df.format((nota1+nota2+nota3)/ 3);
    }

    public String mediaPonderada () {
        DecimalFormat df = new DecimalFormat("#.##");
        return df.format((nota1*2+nota2*3+nota3*4)/ 9);
    }




}

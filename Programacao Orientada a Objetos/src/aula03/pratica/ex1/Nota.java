package aula03.pratica.ex1;

public class Nota {
    private double nota1;
    private double nota2;
    private int faltas;

    public Nota() {

    }

    public Nota(double nota1, double nota2, int faltas) {
        //this.nota1 = nota1;
        //this.nota2 = nota2;
        //this.faltas = faltas;
        setNota1(nota1);
        setNota2(nota2);
        setFaltas(faltas);

    }

    public int getFaltas() {
        return faltas;
    }

    public void setFaltas(int faltas) {
        if (faltas < 0 || faltas > 40) {
            throw new IllegalArgumentException("Número de faltas inválido");
        }
        this.faltas = faltas;
    }

    double getNota1() {
        return nota1;
    }

    void setNota1(double nota1) {
        if (nota1 < 0 || nota1 > 10) {
            throw new IllegalArgumentException("Notas inválidas");
        }
        this.nota1 = nota1;
    }

    double getNota2() {
        return nota2;
    }

    void setNota2(double nota2) {
        if (nota2 < 0 || nota2 > 10) {
            throw new IllegalArgumentException("Notas inválidas");
        }
        this.nota2 = nota2;
    }

    void resultado() {
        /*if (nota1 < 0 || nota2 < 0 ) {
            throw new IllegalArgumentException("Notas inválidas");
        }*/

        double media = (nota1 + nota2)/2;

        System.out.println("A média do aluno é: " + media);

        if (faltas > 7) {
            System.out.println("Reprovado por faltas");
        }
        else if (media >= 6) {
            System.out.println("O aluno está aprovado");
        }
        else if (media >= 4 && media <= 5.9) {
            System.out.println("O aluno está de recuperação");
        }
        else {
            System.out.println("O aluno está reprovado");
        }
    }
}

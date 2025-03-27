package aula03.pratica.ex2;

public class Aluno {
    String nome;
    int matricula;
    double desconto;
    Curso curso;

    public Aluno(String nome, int matricula, double desconto, Curso curso) {
        this.nome = nome;
        this.matricula = matricula;
        this.desconto = desconto;
        this.curso = curso;
    }

    void descrever() {
        System.out.println("Nome do aluno: " + nome);
        System.out.println("Matrícula: " + matricula);
        System.out.println("Desconto: " + desconto);
        curso.info();
    }

    double pagamento() {
        return curso.mensalidade*(1-desconto);
    }

}

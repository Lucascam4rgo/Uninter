package aula03.teorica.visibilidade;

public class Aluno {
    private int matricula;
    public String nome;
    public String cpf;
    protected int notas[];

    public Aluno(int matricula, String nome, String cpf) {
        this.matricula = matricula;
        this.nome = nome;
        this.cpf = cpf;
    }

    void info() {
        System.out.println("Matrícula: " + matricula);
        System.out.println("Nome: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println("Notas: " + notas);
    }
}

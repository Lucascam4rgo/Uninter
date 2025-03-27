package aula02.pratica.ex1;

public class Aluno {
    String nome;
    String curso;
    Avaliacao avaliacao;

    public Aluno(String nome, String curso, Avaliacao avaliacao) {
        this.nome = nome;
        this.curso = curso;
        this.avaliacao = avaliacao;
    }

    void info() {
        System.out.println("Nome do Aluno: " + nome);
        System.out.println("Nome do Curso: " + curso);
        System.out.println("Média Aritmética do aluno: " + avaliacao.mediaAritmetica());
        System.out.println("Média Ponderada do aluno: " + avaliacao.mediaPonderada());

    }
}

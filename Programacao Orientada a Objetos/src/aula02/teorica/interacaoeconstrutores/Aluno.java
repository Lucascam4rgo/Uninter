package aula02.teorica.interacaoeconstrutores;

public class Aluno {

    int matricula;
    String nome;
    String cpf;

    public Aluno(int matricula) {
        this.matricula = matricula;
        this.nome = "Vazio";
        this.cpf = "000.000.000-00";
    }

    //Construtor com campos preenchidos previamente

    public Aluno() {
        System.out.println("Aluno criado sem parâmetros!");
    }

    public Aluno(int matricula, String nome, String cpf) {
        this.matricula = matricula;
        this.nome = nome;
        this.cpf = cpf;
    }

    void info() {
        System.out.println("Matricula: " + matricula);
        System.out.println("Nome: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println();
    }

}

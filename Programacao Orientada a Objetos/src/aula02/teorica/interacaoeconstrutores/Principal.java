package aula02.teorica.interacaoeconstrutores;

import java.util.ArrayList;

public class Principal {

    public static void main(String[] args) {
        Turma nova = new Turma();

        nova.prof = new Professor();
        nova.prof.nome="Leonardo";
        nova.listaAluno = new ArrayList<>();
        nova.listaAluno.add(new Aluno()); // Aqui foi feito com construtor vazio da classe Aluno
        nova.listaAluno.getFirst().nome="Lucas Camargo";

        //System.out.println(nova.listaAluno.getFirst().nome="Lucas Camargo");

        // Aula Construtores

        Aluno a = new Aluno(1001, "Lucas Camargo", "111.222.333-40");

        a.info();

        Aluno b = new Aluno(1002, "Beatriz Bolota", "112.223.334-50");

        b.info();

        Aluno c = new Aluno(1003);

        ArrayList<Aluno> alunos = new ArrayList<>();

        alunos.add(c);
        alunos.add(new Aluno(1004, "Pênis", "123.456.789-10"));
    }
}

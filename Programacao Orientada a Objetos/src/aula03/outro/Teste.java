package aula03.outro;

import aula03.teorica.visibilidade.Aluno;

public class Teste {
    public static void teste() {
        Aluno a = new Aluno(1001, "Super Mario", "111.222.333-40");

        //a.info(); Erro pois o método info é default
    }
}

package aula03.pratica.ex2;

public class Principal {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Lucas Camargo", 1001, 0.5, new Curso("ADS", 800));

        aluno.descrever();
        System.out.println("O aluno " + aluno.nome + " paga a mensalidade de: R$ " + String.format("%.2f", aluno.pagamento()));
    }
}

package aula03.pratica.ex1;

public class Principal {
    public static void main(String[] args) {
        Nota aluno = new Nota();

        //Nota aluno2 = new Nota(90, 80, 5); // Com o construtor normal, sem validação
        Nota aluno3 = new Nota(9, 8, 6);// Porém, depois de montar o construtor com os Sets, a validação é feita

        //aluno2.resultado(); // qualquer número na nota pode ser usado, o que traz erros nos códigos
        aluno3.resultado();// Depois da validação com os Sets do construtor, números acima de 10 e menores que 0 são
        //proibidos

        aluno.setNota1(9);
        aluno.setNota2(5);
        aluno.setFaltas(8);

        aluno.resultado();

    }
}

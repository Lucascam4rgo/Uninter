package aula02classesobjetos.pratica.ex1;

public class Principal {

    public static void main(String[] args) {

        /*Avaliacao bola = new Avaliacao();
        bola.nota1 = 10;
        bola.nota2 = 6.5F;
        bola.nota3 = 7;

        Avaliacao lucas = new Avaliacao(7, 4, 10);

        System.out.println("Média aritmética de Lucas: " + lucas.mediaAritmetica());
        System.out.println("Média aritmética de Bola: " + bola.mediaAritmetica());
        System.out.println("Média ponderada de Lucas: " + lucas.mediaPonderada());
        System.out.println("Média ponderada de Bola: " + bola.mediaPonderada());
*/

        Aluno joao =
                new Aluno("João", "Farmácia",
                        new Avaliacao(9, 10, 7));

        joao.info();


    }

}

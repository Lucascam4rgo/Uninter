package aula04.teorica;

public class Principal {

    public static void main(String[] args) {
        Livro l1 = new Livro("Sir Arthur Conan Doyle", "Sherlock Holmes");
        
        LivroDigital l2 = new LivroDigital("Sir Arthur Conan Doyle","Sherlock Holmes",
                "https://site.sherlock.com.br");

        System.out.println(l1 instanceof Livro);
        System.out.println(l2 instanceof Livro);
        System.out.println(l1 instanceof LivroDigital);
        System.out.println(l2 instanceof LivroDigital);

    }

}

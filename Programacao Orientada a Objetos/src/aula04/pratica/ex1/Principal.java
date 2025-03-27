package aula04.pratica.ex1;

public class Principal {

    public static void main(String[] args) {
        Autor autor = new Autor("Machado de Assis", "machad0ass1s@email.com", "Brasileiro");

        LivroFisico livro = new LivroFisico("Percy Jackson e os Olimpianos", new Autor("Rick Riordan",
                "rickriordan@email.com", "Americano"), "Aventura", 13, 80, 80);

        LivroDigital livrodigital = new LivroDigital("Percy Jackson e os Olimpianos", new Autor("Rick Riordan",
                "rickriordan@email.com", "Americano"), "Aventura", 13, 600, 600);

        LivroFisico livrofisico = new LivroFisico("Percy Jackson e os Olimpianos", new Autor("Rick Riordan",
                "rickriordan@email.com", "Americano"), "Aventura", 13, 24, 70);

        autor.info();
        System.out.println();

        Livro l;

        l = livrodigital;

        l.info();

        l = livrofisico;

        l.info();

    }
}

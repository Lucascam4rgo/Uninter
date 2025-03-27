package aula04.teorica;

public class Livro {
    public String autor;
    public float custoProducao;
    public float precoVenda;
    public String titulo;
    public int paginas;

    public Livro() {

    }

    public Livro(String autor, String titulo) {
        this.autor = autor;
        this.titulo = titulo;
    }

    public float lucro() {
        return precoVenda - custoProducao;
    }

    public void imprimirTitulo() {
        System.out.println("O título: " + titulo);
    }

    public float imposto() {
        return 0.2f * lucro();
    }

}


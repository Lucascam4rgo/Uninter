package aula04.pratica.ex1;

public abstract class Livro {

    protected String titulo;
    protected Autor autor;
    protected String genero;
    protected int edicao;

    public Livro(String titulo, Autor autor, String genero, int edicao) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.edicao = edicao;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public Autor getAutor() {
        return autor;
    }

    public void setAutor(Autor autor) {
        this.autor = autor;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getEdicao() {
        return edicao;
    }

    public void setEdicao(int edicao) {
        this.edicao = edicao;
    }

    void info() {
        System.out.println("Título do Livro: " + titulo);
        System.out.println("Gênero do livro: " + genero);
        System.out.println("Edição do Livro: " + edicao);
        autor.info();
    }
}

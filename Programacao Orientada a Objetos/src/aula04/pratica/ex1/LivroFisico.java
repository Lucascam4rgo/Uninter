package aula04.pratica.ex1;

public class LivroFisico extends Livro {

    private int tiragem;
    private int peso;


    public LivroFisico(String titulo, Autor autor, String genero, int edicao, int tiragem, int peso) {
        super(titulo, autor, genero, edicao);
        this.tiragem = tiragem;
        this.peso = peso;
    }

    public int getTiragem() {
        return tiragem;
    }

    public void setTiragem(int tiragem) {
        this.tiragem = tiragem;
    }

    public int getPeso() {
        return peso;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }

    @Override
    public void info() {
        super.info();
        System.out.println("Tiragem do Livro: " + tiragem);
        System.out.println("Peso do Livro: " + peso);
        System.out.println();
    }
}

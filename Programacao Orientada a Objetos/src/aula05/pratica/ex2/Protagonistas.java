package aula05.pratica.ex2;

public class Protagonistas implements Imprimivel {
    String nome;
    String anime;
    String poder;

    public Protagonistas(String nome, String anime, String poder) {
        this.nome = nome;
        this.anime = anime;
        this.poder = poder;
    }

    @Override
    public void imprimir() {
        System.out.println("Nome: " + nome);
        System.out.println("Anime: " + anime);
        System.out.println("Poder: " + poder);
        System.out.println();
    }
}

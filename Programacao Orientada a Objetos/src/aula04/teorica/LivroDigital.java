package aula04.teorica;

public class LivroDigital extends Livro{
    public String linkDownload;
    public int tamanhoMB;

    public LivroDigital(String autor, String titulo, String linkDownload) {
        super(autor, titulo);
        this.linkDownload = linkDownload;
    }

    public float imposto() {
        return super.imposto() + 2;
    }

    public float tamanhoPorPagina() {
        return tamanhoMB/(float)paginas;
    }

    public void imprimirImposto() {
        System.out.println("Imposto livro Físico: " + super.imposto());
        System.out.println("Imposto livro Digital: " + this.imposto());
    }
}

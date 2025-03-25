package aula02classesobjetos.teorica.classesatributosemetodos;

public class Carro {
    String nome;
    String modelo;
    float velocidade;
    static final double PI = 3.15;

    static float milhasParaMetros(float milhas) {
        return milhas * 1600;
    }
}

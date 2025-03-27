package aula05.teorica.classeabstrata;

public class Principal {

    public static void main(String[] args) {
        FormaGeometrica forma;

        //Forma é um Quadrado
        forma = new Quadrado();
        forma.calculaArea();
        System.out.println(forma.area);
    }
}

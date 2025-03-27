package aula05.teorica.classeabstrata;

import java.util.Scanner;

public class Quadrado extends FormaGeometrica{

    public void calculaArea() {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Digite a medida do lado: ");
        double lado = teclado.nextDouble();
        area = lado*lado;
    }

}

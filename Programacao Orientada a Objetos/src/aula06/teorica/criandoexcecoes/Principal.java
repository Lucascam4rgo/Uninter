package aula06.teorica.criandoexcecoes;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) throws ValorInvalidoException{

        System.out.println("Digite um valor entre 0 e 10");

        Scanner teclado = new Scanner(System.in);

        int valor = teclado.nextInt();

        if (valor > 10 || valor < 0) {
            throw new ValorInvalidoException("Valor Inválido");
        }

        // Com try and catch
        /*try {
            System.out.println("Digite um valor entre 0 e 10");

            Scanner teclado = new Scanner(System.in);

            int valor = teclado.nextInt();

            if (valor > 10 || valor < 0) {
                throw new ValorInvalidoException("Valor Inválido");
            }
        } catch (ValorInvalidoException e) {
            System.out.println("Erro: " + e.getMessage());
        }*/

    }
}



            /* Uma das formas de resolver
            try {
                if (valor > 10 || valor < 0) {
                    throw new Exception("Valor inválido");
                }
            } catch (Exception e) {
                System.out.println("Aconteceu um problema: " + e.getMessage());
            }*/

            /* Outra forma
            if (valor > 10 || valor < 0) {
                throw new RuntimeException("Valor inválido");
            } */

            /* Forma com a criação da Exception
            if (valor > 10 || valor < 0) {
                throw new ValorInvalidoException("Valor inválido");
            }*/

package aula03.teorica.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

public class Principal {
    public static void main(String[] args) {
        //ArrayList<String> pessoas = new ArrayList<>();
        LinkedList<String> pessoas = new LinkedList<>();

        pessoas.add("Mario");
        pessoas.add("Luigi");
        pessoas.add("Peach");
        pessoas.add("Yoshi");

        //pessoas.remove(1);
        System.out.println(pessoas);
        System.out.println(pessoas.get(0));

        System.out.println("Ordem original");
        System.out.println(pessoas);

        Collections.sort(pessoas);
        System.out.println("Ordem original");
        System.out.println(pessoas);

        Collections.shuffle(pessoas);
        System.out.println("Após shuffle");
        System.out.println(pessoas);

        Collections.reverse(pessoas);
        System.out.println("Ordem inversa");
        System.out.println(pessoas);

        System.out.println(Collections.min(pessoas));
        System.out.println(Collections.max(pessoas));

    }
}

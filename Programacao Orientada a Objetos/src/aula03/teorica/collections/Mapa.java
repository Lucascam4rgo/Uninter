package aula03.teorica.collections;

import java.util.HashMap;

public class Mapa {
    public static void main(String[] args) {
        HashMap<String, String> capitais = new HashMap<>();
        capitais.put("Brasil", "Brasília");
        capitais.put("Argentina", "Buenos Aires");
        capitais.put("Paraguai", "Assunção");
        capitais.put("Uruguai", "Montevidéu");

        System.out.println(capitais);
        System.out.println(capitais.get("Uruguai"));


    }


}

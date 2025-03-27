package aula06.teorica.igualdadeetostring;

public class Principal {
    public static void main(String[] args) {
        String s1 = new String("MSG");
        String s2 = new String("MSG");
        String s3 = s1;


        System.out.println(s1 == s2); // IGUAIS EM ENDEREÇAMENTO
        System.out.println(s1.equals(s2)); // IGUAIS EM MENSAGENS

        System.out.println(s1 == s3);

        System.out.println("-----------------------------------------------------");

        Usuario u1 = new Usuario(111, "Mario", "111222333");
        Usuario u2 = new Usuario(111, "Mario", "111222333");
        Usuario u3 = u1;

        System.out.println(u1 == u2);
        System.out.println(u1 == u3);
        System.out.println(u1.equals(u2));
        System.out.println(u1.equals(u3));


        System.out.println("------------------------------------");

        System.out.println("toString");

        System.out.println("------------------------------------");

        Usuario u4 = new Usuario(111, "Lucas", "111222333");

        System.out.println(u4);


    }

}

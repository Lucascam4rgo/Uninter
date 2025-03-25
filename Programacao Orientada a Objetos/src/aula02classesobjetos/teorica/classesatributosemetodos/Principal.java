package aula02classesobjetos.teorica.classesatributosemetodos;

public class Principal {

    public static void main(String[] args) {
        System.out.println("Alô, mamãe!");

        Aluno a = new Aluno();
        a.matricula = 1001;
        a.nome = "Galvão";
        a.cpf = "111222333";

        Aluno b = new Aluno();
        b.matricula = 1002;
        b.nome = "Monarch";
        b.cpf = "112224334";

        a.info();

        a.nome = "Bueno";

        a.info();

        b.info();
    }

}

package aula05.teorica.polimorfismoeclasseabstrata;

public class Principal {

    public static void main(String[] args) {
        /*Funcionario f1 = new Funcionario("Lucas Camargo");

        Funcionario f2 = f1;

        System.out.println("Nome f1: " + f1.nome);
        System.out.println("Nome f2: " + f2.nome);

        System.out.println();

        f2.nome = "Buceta";

        System.out.println("Nome f1: " + f1.nome);
        System.out.println("Nome f2: " + f2.nome);

        Exemplo para o endereçamento de memória, se n houve um new no Funcionario f2, eles estão no mesmo endereço

        */

        Funcionario f1 = new Assalariado("Mario", 3500);

        f1 = new Horista("Luigi", 40, 40.5f);

        Funcionario funcionarios[] = { new Assalariado("Mario", 3500),
        new Horista("Luigi", 100, 40.5f),
        new Comissionado("Yoshi", 50000, 0.05f)};

        Funcionario f;
        float total = 0;
        for (int i=0; i< funcionarios.length;i++) {
            f = funcionarios[i];
            System.out.println(f.nome+" Salário: " + f.pagamento());
            total += f.pagamento();
        }
        System.out.println("Total: " + total);

        System.out.println("------------------------------------------");

        // Classe Abstrata
        //Funcionario f3 = new Funcionario("Mario"); não é possível instanciar uma classe abstrata

        //System.out.println(f3.pagamento());

    }
}

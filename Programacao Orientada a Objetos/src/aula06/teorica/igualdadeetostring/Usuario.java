package aula06.teorica.igualdadeetostring;

import java.util.Objects;

public class Usuario {
    int id;
    String nome;
    String cpf;

    public Usuario(int id, String nome, String cpf) {
        this.id = id;
        this.nome = nome;
        this.cpf = cpf;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Usuario usuario = (Usuario) o;
        return id == usuario.id && Objects.equals(nome, usuario.nome) && Objects.equals(cpf, usuario.cpf);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, nome, cpf);
    }

    @Override
    public String toString() {
        return "Usuario: " +
                "id = " + id +
                ", nome = '" + nome + '\'' +
                ", cpf = '" + cpf + '\'';
    }
}

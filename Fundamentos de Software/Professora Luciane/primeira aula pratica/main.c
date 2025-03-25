
/*
obter notas
calcular media
verifica se o aluno foi reprovado ou não
se a média for >= 7 aprovado
se não reprovado
*/

#include <stdio.h>

int main(void)
{
    // declarando variáveis
    float nota1, nota2, media;

    // obter as notas
    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);

    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

    if (media >= 7)
    {
        printf("O aluno esta aprovado!!");
    }
    else
    {
        printf("O aluno esta reprovado!!");
    }
}
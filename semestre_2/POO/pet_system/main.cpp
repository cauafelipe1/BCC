#include<stdio.h>
#include<iostream>
#include "includes/Pessoa.h"
#include "includes/Voluntario.h"
#include "includes/Tutor.h"
#include "includes/Animal.h"
#include "includes/Cachorro.h"
#include "includes/Gato.h"
#include "includes/Abrigo.h"
#include "includes/Adocao.h"
#include "includes/AdocaoCachorro.h"
#include "includes/AdocaoGato.h"


using namespace std;

//versao basica de teste

int main() {
    Voluntario volunteer("name", 20, "12345678910", "rua dos bobos numero zero", 1, "username", "senha");
    volunteer.listarDados();

    Abrigo petlovers("petlovers", "12345", "5547912345678", "Rua XV de novembro, 4");
    petlovers.listarAdocoes();

    //precisa da UI no console
}
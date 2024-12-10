#include<stdio.h>
#include<iostream>
#include "includes/Pessoa.h"
#include "includes/Voluntario.h"
using namespace std;

//versao basica de teste

int main() {
    Voluntario volunteer("name", 20, "12345678910", "rua dos bobos numero zero", 1, "username", "senha");
    volunteer.listarDados();
}
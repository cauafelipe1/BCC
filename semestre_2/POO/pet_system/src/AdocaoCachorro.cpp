#include<iostream>
#include "../includes/AdocaoCachorro.h"
using namespace std;

AdocaoCachorro::AdocaoCachorro(string dA, int iD, Tutor t, Cachorro c) : Adocao(dA, iD, t), cachorroAdotado(c)  {}

void AdocaoCachorro::listarDados() {
    Adocao::listarDados();
    cout << "Cachorro: " << cachorroAdotado.nome << endl;
}
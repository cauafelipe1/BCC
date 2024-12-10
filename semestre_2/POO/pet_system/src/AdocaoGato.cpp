#include<iostream>
#include "../includes/AdocaoGato.h"
using namespace std;

AdocaoGato::AdocaoGato(string dA, int iD, Tutor t, Gato gA) : Adocao(dA, iD, t), gatoAdotado(gA)  {}

void AdocaoGato::listarDados() {
    Adocao::listarDados();
    cout << "Gato: " << gatoAdotado.nome << endl;
}

#include<iostream>
#include "../includes/Adocao.h"
using namespace std;

Adocao::Adocao(string dA, int iD, Tutor t) : dataAdocao(dA), id(iD), tutor(t)  {}

void Adocao::listarDados() {

    cout << "[DADOS DA ADOÇÃO]\n";
    cout << "Data: " << dataAdocao << endl;
    cout << "Tutor: " << tutor.nome << endl;
}

Adocao::~Adocao() = default;
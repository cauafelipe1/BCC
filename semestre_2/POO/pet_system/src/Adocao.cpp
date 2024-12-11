#include<iostream>
#include "../includes/Adocao.h"
using namespace std;

Adocao::Adocao(string dA, int iD, Tutor t) : dataAdocao(dA), id(iD), tutor(t)  {}

void Adocao::listarDados() {
    cout << "--- Data: " << dataAdocao << "\t";
    cout << "Tutor: " << tutor.nome << "\t";
}

Adocao::~Adocao() = default;
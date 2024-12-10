#include<iostream>
#include "../includes/Pessoa.h"

using namespace std;

Pessoa::Pessoa(string n, int i, string t, string e, const int id) : nome(n), idade(i), telefone(t), endereco(e), id(id) {

}

void Pessoa::listarDados() {
    cout << "[DADOS PESSOAIS]\n";
    cout << "Nome: " << nome << endl;
    cout << "Idade: " << idade << endl;
    cout << "Telefone: " << telefone << endl;
    cout << "Endereco: " << endereco << endl;
}

Pessoa::~Pessoa() = default;
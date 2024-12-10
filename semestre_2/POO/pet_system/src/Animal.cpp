#include<iostream>
#include "../includes/Animal.h"
using namespace std;

Animal::Animal(string n, int i, int iD, string o, bool s, string e) : nome(n), idade(i), id(iD), origem(o), sociavel(s), especificacoes(e) {}

void Animal::listarDados() {

    cout << "[DADOS]\n";
    cout << "Nome: " << nome << endl;
    cout << "Idade: " << idade << endl;
    cout << "Origem: " << origem << endl;
    string s = sociavel ? "sim" : "nao";
    cout << "Sociavel: " << s << endl;
    cout << "Especificacoes: " << especificacoes << endl;
}

Animal::~Animal() = default;
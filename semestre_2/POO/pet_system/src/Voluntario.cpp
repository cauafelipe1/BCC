#include<iostream>
#include "../includes/Voluntario.h"

using namespace std;

Voluntario::Voluntario(string n, int i, string t, string e, int iD, string l, string s) : Pessoa(n, i, t, e, iD), login(l), senha(s) {}

void Voluntario::listarDados() {
    Pessoa::listarDados();
    cout << "Login: " << login << endl;
    cout << "Senha: " << senha << endl;
}
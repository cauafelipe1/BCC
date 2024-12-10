#include<iostream>
#include "../includes/Gato.h"
using namespace std;

Gato::Gato(string n, int i, int iD, string o, bool s, string e, string p, string c, string pA) : Animal(n, i, iD, o, s, e), padraoPelagem(p), comprimentoPelagem(c), preferenciaAmbiente(pA) {}

void Gato::listarDados() {
    Animal::listarDados();
    cout << "Padrao de pelagem: " << padraoPelagem << endl;
    cout << "Comprimento de pelagem: " << comprimentoPelagem << endl;
    cout << "Preferencia de ambiente: " << preferenciaAmbiente << endl;

}
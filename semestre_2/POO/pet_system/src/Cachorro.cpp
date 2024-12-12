#include<iostream>
#include "../includes/Cachorro.h"
using namespace std;

Cachorro::Cachorro(string n, int i, int iD, string o, bool s, string e, string r, string p, string nA) : Animal(n, i, iD, o, s, e), raca(r), porte(p), nivelAdestramento(nA) {}

void Cachorro::listarDados() {
    Animal::listarDados();
    cout << "Raca: " << raca << endl;
    cout << "Porte: " << porte << endl;
    cout << "Nivel de adestramento: " << nivelAdestramento << endl;

}
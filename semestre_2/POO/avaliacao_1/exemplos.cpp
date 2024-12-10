#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
#include <cstdlib>
using namespace std;


class Pessoa {
    public:
        string nome;
        Pessoa(string n) : nome(n) {} //construtor simples
};

class EntradaHall {
    private: 
        Pessoa pessoa;
    public:
        //construtor usando um objeto do tipo pessoa como parametro
        EntradaHall(Pessoa p) : pessoa(p) {
            cout << "A pessoa chamada " << pessoa.nome << " entrou no hall" << endl;
        }
};

int main() {
    //objeto pessoa sendo criado
    Pessoa newPessoa("joao");

    //objeto entrada sendo criado com o objeto newPessoa como parametro
    EntradaHall entrada(newPessoa);
    return 0;
}
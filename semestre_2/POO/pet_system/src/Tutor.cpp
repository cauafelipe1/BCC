#include<iostream>
#include "../includes/Tutor.h"
#include<vector>

Tutor::Tutor(std::string n, int i, std::string t, std::string e, const int iD, std::vector<Gato> g, std::vector<Cachorro> c) : Pessoa(n, i, t, e, iD), gatos(g), caes(c) {}

void Tutor::listarDados() {
    Pessoa::listarDados();
    
    std::cout << "Gatos:\n";
    for (const auto& cat : gatos) {
        std::cout << cat.nome << std::endl;
    }
    std::cout << "Cachorros:\n";
    for (const auto& dog : caes) {
        std::cout << dog.nome << std::endl;
    }
}
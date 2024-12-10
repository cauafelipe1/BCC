#pragma once
#include "Pessoa.h"
#include "Gato.h"
#include "Cachorro.h"
#include <vector>
class Tutor : public Pessoa {
    public:
        std::vector<Gato> gatos;
        std::vector<Cachorro> caes;
        Tutor(std::string n, int i, std::string t, std::string e, const int iD, std::vector<Gato> g, std::vector<Cachorro> c);
        void listarDados() override;
};
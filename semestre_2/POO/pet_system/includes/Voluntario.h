#pragma once
#include "Pessoa.h"

class Voluntario : public Pessoa {
    public:
        std::string login;
        std::string senha;
        Voluntario(std::string n, int i, std::string t, std::string e, int iD, std::string l, std::string s);
        void listarDados() override;
};
#pragma once

class Pessoa {
    public:
        std::string nome;
        int idade;
        std::string telefone;
        std::string endereco;
        const int id;
        Pessoa(std::string n, int i, std::string t, std::string e, const int iD);
        virtual ~Pessoa();
        virtual void listarDados();
};
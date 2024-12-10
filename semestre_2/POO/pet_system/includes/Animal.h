#pragma once
class Animal {
    public:
        std::string nome;
        int idade;
        int id;
        std::string origem;
        bool sociavel;
        std::string especificacoes;
        Animal(std::string n, int i, int iD, std::string o, bool s, std::string e);
        virtual ~Animal();
        virtual void listarDados();
};
#pragma once 
#include "Animal.h" 

class Cachorro : public Animal {
    public:
        std::string raca;
        std::string porte;
        std::string nivelAdestramento;
        Cachorro(std::string n, int i, int iD, std::string o, bool s, std::string e, std::string r, std::string p, std::string nA);
        void listarDados() override;
};
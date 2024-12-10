#pragma once 
#include "Animal.h" 

class Gato : public Animal {
    public:
        std::string padraoPelagem;
        std::string comprimentoPelagem;
        std::string preferenciaAmbiente;
        Gato(std::string n, int i, int iD, std::string o, bool s, std::string e, std::string p, std::string c, std::string pA);
        void listarDados() override;
};
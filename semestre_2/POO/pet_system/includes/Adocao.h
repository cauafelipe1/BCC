#pragma once
#include "Tutor.h"

class Adocao {
    public:
        std::string dataAdocao;
        int id;
        Tutor tutor;

        Adocao(std::string dA, int id, Tutor t);
        virtual ~Adocao();
        virtual void listarDados();
};
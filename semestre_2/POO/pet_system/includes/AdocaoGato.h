#pragma once
#include "Adocao.h"
#include "Gato.h"

class AdocaoGato : public Adocao {
    public:
        Gato gatoAdotado;
        AdocaoGato(std::string dA, int id, Tutor t, Gato gA);
        void listarDados() override;
};
#pragma once
#include "Adocao.h"
#include "Cachorro.h"

class AdocaoCachorro : public Adocao {
    public:
        Cachorro cachorroAdotado;
        AdocaoCachorro(std::string dA, int id, Tutor t, Cachorro c);
        void listarDados() override;
};
#pragma once
#include "Voluntario.h"
#include <vector>
#include "Tutor.h"
#include "Cachorro.h"
#include "Gato.h"
#include "AdocaoGato.h"
#include "AdocaoCachorro.h"

class Abrigo {
    public:
        
       static Voluntario admin;
        std::string nome;
        std::string CNPJ;
        std::string telefone;
        std::string endereco;
        std::vector<Voluntario> funcionarios;
        std::vector<Tutor> tutores;
        std::vector<Cachorro> caes;
        std::vector<Gato> gatos;
        std::vector<AdocaoGato> adocoesGatos;
        std::vector<AdocaoCachorro> adocoesCachorros;

        //metodos
        Abrigo(std::string n, std::string cnpj, std::string t, std::string e);
        Tutor* getTutorById(int iD);
        Gato* getGatoById(int iD);
        //Voluntario* getVoluntarioById(int iD);
        Cachorro* getCachorroById(int iD);
        bool voluntarioLogin(std::string l, std::string s);
        void cadastrarVoluntario();
        void cadastrarAnimal();
        void cadastrarTutor();
        void listarAnimais();
        void removerVoluntario();
        void removerAnimal();
        void realizarAdocao();
        void listarAdocoes();

};
#include<iostream>
#include "../includes/Abrigo.h"
#include <algorithm>
using namespace std;
    


Abrigo::Abrigo(string n, string cnpj, string t, string e) : nome(n), CNPJ(cnpj), telefone(t), funcionarios(), tutores(), caes(), gatos(), adocoesGatos(), adocoesCachorros() {
    Voluntario admin("admin", 20, "nao consta", endereco, 1, "admin123", "admin123");
    funcionarios.push_back(admin);
}

void Abrigo::cadastrarVoluntario() {
    cout << "[CADASTRO DE VOLUNTARIO]\n";
    cout << "Insira alguns dados para seguir com o cadastro...\n";
    //implementar verificacoes + hash de senha em um arquivo com funcoes uteis
}

Tutor* Abrigo::getTutorById(int iD) {
    for (auto& tutor : tutores) {
        if (tutor.id == iD) {
            return &tutor;
        }
    }
    return nullptr;
}


Gato* Abrigo::getGatoById(int iD) {
    for (auto& cat : gatos) {
        if (cat.id == iD) {
            return &cat;
        }
    }
    return nullptr;
}


Cachorro* Abrigo::getCachorroById(int iD) {
    for (auto& dog : caes) {
        if (dog.id == iD) {
            return &dog;
        }
    }
    return nullptr;
}

bool Abrigo::voluntarioLogin(string l, string s) {
    for (auto& voluntario : funcionarios) {
        if ((voluntario.login == l) && (voluntario.senha == s)) {
            return true;
        }
    }
    return false;
}

void Abrigo::cadastrarAnimal() {

    cout << "[CADASTRO DE ANIMAIS]\n";
    int escolha;

    //Formulario de preenchimento de cadastro de animais
    while (1) {
        cout << "Qual tipo de animal deseja cadastrar?\n";
        cout << "1 - cachorro\n";
        cout << "2 - gato\n";
        cout << "Insira sua escolha (1 ou 2): ";
        cin >> escolha;
        cin.ignore();


        switch (escolha) {
        case 1: {
            cout << "Insira os dados do cachorro que sera cadastrado no abrigo...\n";
            /* trata os inputs do cachorro*/
            break;
        }
        case 2: {
            cout << "Insira os dados do gato que sera cadastrado no abrigo...\n";
            /* trata os inputs do gato */
            break;
        }
        default:
            cout << "escolha invalida!\n";
        }
    }
    
}

void Abrigo::cadastrarTutor() {
    cout << "[CADASTRO DE TUTOR]\n";

}

void Abrigo::listarAnimais() {
    cout << "[ANIMAIS DISPONIVEIS PARA ADOCAO]\n";
    
    cout << "Cachorros:\n";
    int i = 1;
    for (auto& dog : caes) { 
        cout << i << " - ";
        dog.listarDados();
        i++;
    }
    cout << "Gatos:\n";
    for (auto & cat : gatos) {
        cout << i << " - ";
        cat.listarDados();
        i++; 
    }
}
/*
Voluntario* Abrigo::getVoluntarioById (int iD) {
    for (auto& voluntario : funcionarios) {
        if (voluntario.id == iD) {
            return &voluntario;
        }
    }
    return nullptr;
}
*/

void Abrigo::removerVoluntario() {
    cout << "[REMOVER VOLUNTARIO]\n";
    int iD;
    cout << "Insira o ID do voluntario que sera removido: ";
    cin >> iD;
    cin.ignore();
    
    if (iD == 1) {
        cout << "admin nao pode ser removido\n";
    }

    auto condicao = [iD](const Voluntario& voluntario) {
        return voluntario.id == iD;
    };
    auto newEnd = remove_if(funcionarios.begin(), funcionarios.end(), condicao);

        if (newEnd!= funcionarios.end()) {
            funcionarios.erase(newEnd, funcionarios.end());
            cout << "Voluntario removido com sucesso!\n" << endl;
        } else {
            cout << "ID de voluntario nao encontrado...\n" << endl;
        }
}

void Abrigo::removerAnimal() {
    cout << "[REMOVER ANIMAL]\n";
    int iD;
    int escolha;
    while (1) {
        cout << "Que tipo de animal deseja remover?\n";
        cout << "1 - Cachorro\n";
        cout << "2 - Gato\n";
        cout << "Insira sua escolha (1 ou 2): ";
        cin >> escolha;
        cin.ignore();
        switch (escolha) {
        case 1: {
            cout << "Insira o ID do cachorro que deseja remover do abrigo: ";
            cin >> iD;
            cin.ignore();

            auto condicao = [iD](const Cachorro& dog) {
                return dog.id == iD;
            };
            auto newEnd = remove_if(caes.begin(), caes.end(), condicao);

            if (newEnd!= caes.end()) {
                caes.erase(newEnd, caes.end());
                cout << "Cachorro removido com sucesso!\n";
            } 
            else {
                cout << "Cachorro nao encontrado no abrigo...\n";
            }

            break;
        }

        case 2: {

            cout << "Insira o ID do gato que deseja remover do abrigo: ";
            cin >> iD;
            cin.ignore();

            auto condicao = [iD](const Gato& cat) {
                return cat.id == iD;
            };
            auto newEnd = remove_if(gatos.begin(), gatos.end(), condicao);

            if (newEnd!= gatos.end()) {
                gatos.erase(newEnd, gatos.end());
                cout << "Gato removido com sucesso!\n";
            } 
            else {
                cout << "Gato nao encontrado no abrigo...\n";
            }
            break;
        }
        
        default:
            cout << "insira uma opcao valida\n";
        }
    }
    
}

void Abrigo::realizarAdocao() {
    //realizar adocao
}

void Abrigo::listarAdocoes() {
    cout << "[LISTA DE ADOCOES EFETUADAS NO ABRIGO]\n";
    cout << "[CAES]\n";

    for (auto& caoAdotado : adocoesCachorros) {
        caoAdotado.listarDados(); 
    }
    cout << "[GATOS]\n";
    for (auto&  gatoAdotado: adocoesGatos) {
        gatoAdotado.listarDados(); 
    }

}
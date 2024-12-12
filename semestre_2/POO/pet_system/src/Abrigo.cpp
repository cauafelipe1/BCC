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
    try
    {
        string nome;
        int idade;
        string telefone;
        string endereco;
        int id = funcionarios.back().id + 1;
        string login;
        string senha;
        cout << "Nome: ";
        getline(cin >> ws, nome);
        cout << "Idade: ";
        if (!(cin >> idade)) {
            throw runtime_error("Insira uma idade valida!\n");
        }
        if ((idade < 14) || (idade > 80)) {
            throw runtime_error("Somente podem ser cadastrados voluntarios de 14 a 80 anos..\n");
        }
        cin.clear();
        cin.ignore();

        cout << "Telefone: ";
        getline(cin >> ws, telefone);
        cout << "Endereco: ";
        getline(cin >> ws, endereco);
        cout << "Login: ";
        getline(cin >> ws, login);
        cout << "Senha: ";
        //implementar hash
        getline(cin >> ws, senha);
        


        Voluntario newVoluntario(nome, idade, telefone, endereco,  id, login, senha);
        funcionarios.push_back(newVoluntario);
        cout << "Novo voluntario cadastrado com sucesso!\n";
    }
    catch(const exception& e)
    {
        cout << "Erro: " << e.what() << '\n';
    }
    catch (...) {
        cout << "erro inesperado..\n";
    }
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
            try
            {
                string nome;
                int idade;
                int id;
                string origem; 
                string especificacoes;
                bool sociavel;
                string raca;
                string porte;
                string nivelAdestramento;
                cout << "Nome: ";
                getline(cin >> ws, nome);
                cout << "Idade: ";
                if (!(cin >> idade)) {
                    throw runtime_error("Insira um valor de idade valido!\n");
                    break;
                }
                if ((idade < 1) || (idade > 30)) {
                    throw runtime_error("Insira uma idade real (1 a 30 anos)..\n");
                    break;
                }
                cin.clear();
                cin.ignore();

                cout << "Origem: ";
                getline(cin >> ws, origem);
                cout << "Especificacoes: ";
                getline(cin >> ws, especificacoes);

                char x;
                cout << "O cachorro é sociavel? (S/N): ";
                cin >> x;
                if (x == 'S' || x == 's') {
                    sociavel = true;
                }
                else if (x == 'N' || x == 'n') {
                    sociavel = false;
                }
                else {
                    throw invalid_argument("Entrada invalida..");
                    break;
                }
                cin.clear();
                cin.ignore();

                cout << "Raca: ";
                getline(cin >> ws, raca);
                cout << "Porte: ";
                getline(cin >> ws, porte);
                cout << "Nivel de adestramento: ";
                getline(cin >> ws, nivelAdestramento);

                if (caes.empty()) {
                    id = 1;
                }
                else {
                    id = caes.back().id + 1;
                }

                Cachorro newDog(nome, idade, id, origem, sociavel,  especificacoes,  raca,  porte,  nivelAdestramento);
                caes.push_back(newDog);
                cout << "CACHORRO CADASTRADO COM SUCESSO!!\n";
            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << "\n";
            }
            catch(...) {
                cout << "erro inesperado...";
            }
            
            break;
        }
        case 2: {
            cout << "Insira os dados do gato que sera cadastrado no abrigo...\n";
            try
            {
                string nome;
                int idade;
                int id;
                string origem; 
                string especificacoes;
                bool sociavel;
                string padraoPelagem;
                string comprimentoPelagem;
                string preferenciaAmbiente;
                cout << "Nome: ";
                getline(cin >> ws, nome);
                cout << "Idade: ";
                if (!(cin >> idade)) {
                    throw runtime_error("Insira um valor de idade valido!\n");
                    break;
                }
                if ((idade < 1) || (idade > 30)) {
                    throw runtime_error("Insira uma idade real (1 a 30 anos)..\n");
                    break;
                }
                cin.clear();
                cin.ignore();

                cout << "Origem: ";
                getline(cin >> ws, origem);
                cout << "Especificacoes: ";
                getline(cin >> ws, especificacoes);

                char x;
                cout << "O gato é sociavel? (S/N): ";
                cin >> x;
                if (x == 'S' || x == 's') {
                    sociavel = true;
                }
                else if (x == 'N' || x == 'n') {
                    sociavel = false;
                }
                else {
                    throw invalid_argument("Entrada invalida..");
                    break;
                }
                cin.clear();
                cin.ignore();
                cout << "Padrao de pelagem: ";
                getline(cin >> ws, padraoPelagem);

                cout << "Comprimento da pelagem: ";
                getline(cin >> ws, comprimentoPelagem);

                cout << "Preferencia de ambiente: ";
                getline(cin >> ws, preferenciaAmbiente);

                if (caes.empty()) {
                    id = 1;
                }
                else {
                    id = caes.back().id + 1;
                }

                Gato newCat(nome, idade, id, origem, sociavel,  especificacoes,  padraoPelagem, comprimentoPelagem, preferenciaAmbiente);
                gatos.push_back(newCat);
                cout << "GATO CADASTRADO COM SUCESSO!!\n";
            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << "\n";
            }
            catch(...) {
                cout << "erro inesperado...";
            }
            
            break;
        }
        default:
            cout << "escolha invalida!\n";
        }
    }
    
}

void Abrigo::cadastrarTutor() {
    cout << "[CADASTRO DE TUTOR]\n";

     try
    {
        string nome;
        int idade;
        string telefone;
        string endereco;
        int id;
        vector<Gato> gatos;
        vector<Cachorro> caes;

        cout << "Nome: ";
        getline(cin >> ws, nome);
        cout << "Idade: ";
        if (!(cin >> idade)) {
            throw runtime_error("Insira uma idade valida!\n");
        }
        if ((idade < 10) || (idade > 100)) {
            throw runtime_error("Somente podem ser cadastrados tutores de 10 a 100 anos..\n");
        }
        cin.clear();
        cin.ignore();

        cout << "Telefone: ";
        getline(cin >> ws, telefone);
        cout << "Endereco: ";
        getline(cin >> ws, endereco);
        if (tutores.empty()) {
             id = 1;
        }
        else {
            id = tutores.back().id + 1;
        }


        Tutor newTutor(nome, idade, telefone, endereco,  id, gatos, caes);
        tutores.push_back(newTutor);
        cout << "Novo tutor cadastrado com sucesso!\n";
    }
    catch(const exception& e)
    {
        cout << "Erro: " << e.what() << '\n';
    }
    catch (...) {
        cout << "erro inesperado..\n";
    }

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
    cout << "[ADOCAO]\n";
    cadastrarTutor();
    int escolha;
    int idEscolhido;
    while (1) {
        cout << "Que tipo de animal deseja adotar?\n";
        cout << "1 - Cachorro\n";
        cout << "2 - Gato\n";
        cout << "Insira sua escolha (1 ou 2): ";
        cin >> escolha;
        cin.ignore();
        switch (escolha) {
        case 1: {
            try {
                cout << "Confira a lista abaixo com os animais disponiveis no abrigo:\n";
                listarAnimais();
            cout << "Insira o ID do cachorro que deseja realizar a adocao: ";
            if (cin >> idEscolhido) {
                throw runtime_error("Insira um numero valido\n");
                break;
            }
            
            cin.clear();
            cin.ignore();

            Cachorro* caoEscolhido = getCachorroById(idEscolhido);
            Tutor* currentTutor = getTutorById(tutores.back().id);
            currentTutor->caes.emplace_back(caoEscolhido->nome, caoEscolhido->idade, caoEscolhido->id, caoEscolhido->origem, caoEscolhido->sociavel, caoEscolhido->especificacoes, caoEscolhido->raca, caoEscolhido->porte, caoEscolhido->nivelAdestramento);
            
            //remocao do cachorro de dentro do abrigo
            auto condicao = [idEscolhido](const Cachorro& dog) {
                return dog.id == idEscolhido;
            };
            auto newEnd = remove_if(caes.begin(), caes.end(), condicao);

            if (newEnd!= caes.end()) {
                caes.erase(newEnd, caes.end());
                cout << "Cachorro removido do abrigo com sucesso! Agora ele tera um novo lar :)\n";
            } 
            else {
                cout << "Cachorro nao encontrado no abrigo...\n";
            }   

            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << '\n';
            }
            catch (...) {
                cout << "erro inesperado..\n";
            }
            
            break;
        }

        case 2: {
            try {
                cout << "Confira a lista abaixo com os animais disponiveis no abrigo:\n";
                listarAnimais();
            cout << "Insira o ID do gato que deseja realizar a adocao: ";
            if (cin >> idEscolhido) {
                throw runtime_error("Insira um numero valido\n");
                break;
            }
            
            cin.clear();
            cin.ignore();

            Gato* gatoEscolhido = getGatoById(idEscolhido);
            Tutor* currentTutor = getTutorById(tutores.back().id);
            currentTutor->gatos.emplace_back(gatoEscolhido->nome, gatoEscolhido->idade, gatoEscolhido->id, gatoEscolhido->origem, gatoEscolhido->sociavel, gatoEscolhido->especificacoes, gatoEscolhido->padraoPelagem, gatoEscolhido->comprimentoPelagem, gatoEscolhido->preferenciaAmbiente);
            
            //remocao do gato de dentro do abrigo
            auto condicao = [idEscolhido](const Gato& cat) {
                return cat.id == idEscolhido;
            };
            auto newEnd = remove_if(gatos.begin(), gatos.end(), condicao);

            if (newEnd!= gatos.end()) {
                gatos.erase(newEnd, gatos.end());
                //AdocaoGato("bla", 1, currentTutor, gatoEscolhido);
                cout << "Gato removido do abrigo com sucesso! Agora ele tera um novo lar :)\n";
            } 
            else {
                cout << "Gato nao encontrado no abrigo...\n";
            }   

            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << '\n';
            }
            catch (...) {
                cout << "erro inesperado..\n";
            }
            
            break;
        }
        
        default:
            cout << "insira uma opcao valida\n";
        }
    }
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
#include<iostream>
#include "../includes/Abrigo.h"
#include <algorithm>
#include "../includes/uteis.h"
using namespace std;
    


Abrigo::Abrigo(string n, string cnpj, string t, string e) : nome(n), CNPJ(cnpj), telefone(t), funcionarios(), tutores(), caes(), gatos(), adocoesGatos(), adocoesCachorros() {
    Voluntario admin("admin", 20, "nao consta", endereco, 1, "admin123", "admin123");
    funcionarios.push_back(admin);
}

//classe de cadastro de voluntario
void Abrigo::cadastrarVoluntario() {
    cout << "\n[ CADASTRO DE VOLUNTARIO ]\n";
    cout << "Insira alguns dados para seguir com o cadastro...\n";
    try {
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
            clearInputBuffer();
            throw runtime_error("Insira uma idade válida!");
        }
        if (idade < 14 || idade > 80) {
            throw runtime_error("Somente podem ser cadastrados voluntários de 14 a 80 anos.");
        }
        cin.ignore();
         

        cout << "Telefone: ";
        getline(cin >> ws, telefone);

        cout << "Endereco: ";
        getline(cin >> ws, endereco);

        cout << "Login: ";
        getline(cin >> ws, login);

        cout << "Senha: ";
        getline(cin >> ws, senha);

        Voluntario newVoluntario(nome, idade, telefone, endereco, id, login, criptografar(senha, 'K'));
        funcionarios.push_back(newVoluntario);

        
        cout << "Novo voluntário cadastrado com sucesso!\n";
        return;
    } catch (const exception& e) {
        cout << "Erro: " << e.what() << '\n';
        return;
    } catch (...) {
        cout << "Erro inesperado.\n";
        return;
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
    string senhaEncriptada = criptografar(s, 'K');
    for (auto& voluntario : funcionarios) {
        if ((voluntario.login == l) && (voluntario.senha == senhaEncriptada)) {
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
                    clearInputBuffer();
                    throw runtime_error("Insira um valor de idade valido!\n");
                }
                if ((idade < 1) || (idade > 30)) {
                    throw runtime_error("Insira uma idade real (1 a 30 anos)..\n");
                 
                }
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
                    clearInputBuffer();
                    throw invalid_argument("Entrada invalida..");
                }
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
                return;
            }
            catch(...) {
                cout << "erro inesperado...";
                return;
            }
            
            return;
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
                    clearInputBuffer();
                    throw runtime_error("Insira um valor de idade valido!\n");
              
                }
                if ((idade < 1) || (idade > 30)) {
                    throw runtime_error("Insira uma idade real (1 a 30 anos)..\n");
             
                }
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
                    clearInputBuffer();
                    throw invalid_argument("Entrada invalida..");
                  
                }
                cin.ignore();
                cout << "Padrao de pelagem: ";
                getline(cin >> ws, padraoPelagem);

                cout << "Comprimento da pelagem: ";
                getline(cin >> ws, comprimentoPelagem);

                cout << "Preferencia de ambiente: ";
                getline(cin >> ws, preferenciaAmbiente);

                if (gatos.empty()) {
                    id = 1;
                }
                else {
                    id = gatos.back().id + 1;
                }

                Gato newCat(nome, idade, id, origem, sociavel,  especificacoes,  padraoPelagem, comprimentoPelagem, preferenciaAmbiente);
                gatos.push_back(newCat);
                cout << "GATO CADASTRADO COM SUCESSO!!\n";
            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << "\n";
                return;
            }
            catch(...) {
                cout << "erro inesperado...";
                return;
            }
            
            return;
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
            clearInputBuffer();
            throw runtime_error("Insira uma idade valida!\n");
        }
        cin.ignore();
        if ((idade < 10) || (idade > 100)) {
            throw runtime_error("Somente podem ser cadastrados tutores de 10 a 100 anos..\n");
        } 
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
        return;
    }
    catch(const exception& e)
    {
        cout << "Erro: " << e.what() << '\n';
        return;
    }
    catch (...) {
        cout << "erro inesperado..\n";
        return;
    }

}

void Abrigo::listarAnimais() {
    cout << "[ANIMAIS DISPONIVEIS PARA ADOCAO]\n";
    
    cout << "Cachorros:\n";
    for (auto& dog : caes) { 
        dog.listarDados();
    }
    cout << "Gatos:\n";
    for (auto & cat : gatos) {
        cat.listarDados();
    }
}


void Abrigo::removerVoluntario() {
    try {
    cout << "[REMOVER VOLUNTARIO]\n";
    int iD;
    cout << "Insira o ID do voluntario que sera removido: ";
    if (!(cin >> iD))
    {
        clearInputBuffer();
        throw runtime_error("Insira um id valido..");
    }
    
    if (iD == 1) {
        cout << "admin nao pode ser removido\n";
        return void();
    }

    auto condicao = [iD](const Voluntario& voluntario) {
        return voluntario.id == iD;
    };
    auto newEnd = remove_if(funcionarios.begin(), funcionarios.end(), condicao);

        if (newEnd!= funcionarios.end()) {
            funcionarios.erase(newEnd, funcionarios.end());
            cout << "Voluntario removido com sucesso!\n" << endl;
            return;
        } else {
            cout << "ID de voluntario nao encontrado...\n" << endl;
            return;
        }
    }
    catch(const std::exception& e)
    {
        cout << "Erro: " << e.what() << '\n';
        return void();
    }
    catch(...) {
        cout << "erro inesperado...\n";
        return void();
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
            try
            {
            if (caes.size() == 0) {
                cout << "O abrigo não possui cachorros para serem removidos..\n";
                return;
            }
            cout << "Lista de cachorros - ID e nome:\n";
            for (auto&dog : caes) {
                cout << dog.id << " - " << dog.nome << endl;
            }
            cout << "Insira o ID do cachorro que deseja remover do abrigo: ";
            if (!(cin >> iD))
            {
                clearInputBuffer();
                throw runtime_error("insira um id valido..");
            }
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
            return;
            }
            catch(const std::exception& e)
            {
                cout << "Erro: " << e.what() << endl;
                return;
            }
            catch (...) {
                cout << "Erro inesperado..\n";
                return;
            }

            return;
        }

        case 2: {

            try
            {
            if (gatos.size() == 0) {
                cout << "O abrigo não possui gatos para serem removidos..\n";
                return;
            }

            cout << "Lista de gatos - ID e nome:\n";
            for (auto&cat : gatos) {
                cout << cat.id << " - " << cat.nome << endl;
            }
            cout << "Insira o ID do gato que deseja remover do abrigo: ";

            if (!(cin >> iD)) {
                clearInputBuffer();
                throw runtime_error("Insira um id valido..");
            }
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
            }
            catch(const std::exception& e)
            {
                cout << "Erro: " << e.what() << endl;
                return;
            }
            
            catch(...) {
                cout << "erro inesperado...\n";
                return;
            }
        return;
        }
        
        default:
            cout << "insira uma opcao valida\n";
        }
    }
    return;
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
            if (!(cin >> idEscolhido)) {
                clearInputBuffer();
                throw runtime_error("Insira um numero valido\n");
            }
            cin.ignore();
 

            Cachorro* caoEscolhido = getCachorroById(idEscolhido);
            Tutor* currentTutor = getTutorById(tutores.back().id);
            currentTutor->caes.push_back(*caoEscolhido);
            
            //remocao do cachorro de dentro do abrigo
            auto condicao = [idEscolhido](const Cachorro& dog) {
                return dog.id == idEscolhido;
            };
            auto newEnd = remove_if(caes.begin(), caes.end(), condicao);

            if (newEnd!= caes.end()) {
                string dataAtual = obterDataAtual();

                caes.erase(newEnd, caes.end());
                if (adocoesCachorros.size() == 0) {
                    AdocaoCachorro newAdocao(dataAtual, 1, *currentTutor, *caoEscolhido);
                    adocoesCachorros.push_back(newAdocao);
                }
                else {
                int newID = adocoesCachorros.back().id + 1;
                AdocaoCachorro newAdocao(dataAtual, newID, *currentTutor, *caoEscolhido);
                adocoesCachorros.push_back(newAdocao);
               
                }

                cout << "Cachorro removido do abrigo com sucesso! Agora ele tera um novo lar :)\n";
            } 
            else {
                cout << "Cachorro nao encontrado no abrigo...\n";
            }   

            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << '\n';
                return;
            }
            catch (...) {
                cout << "erro inesperado..\n";
                return;
            }
            
            return;
        }

        case 2: {
            try {
                cout << "Confira a lista abaixo com os animais disponiveis no abrigo:\n";
                listarAnimais();
            cout << "Insira o ID do gato que deseja realizar a adocao: ";
            if (!(cin >> idEscolhido)) {
                clearInputBuffer();
                throw runtime_error("Insira um numero valido\n");
                return;
            }
            cin.ignore();

            Gato* gatoEscolhido = getGatoById(idEscolhido);
            Tutor* currentTutor = getTutorById(tutores.back().id);
            currentTutor->gatos.push_back(*gatoEscolhido);
            //remocao do gato de dentro do abrigo
            auto condicao = [idEscolhido](const Gato& cat) {
                return cat.id == idEscolhido;
            };
            auto newEnd = remove_if(gatos.begin(), gatos.end(), condicao);

            if (newEnd!= gatos.end()) {
                gatos.erase(newEnd, gatos.end());
                string dataAtual = obterDataAtual();
                if (adocoesGatos.size() == 0) {
                    AdocaoGato novaAdocao(dataAtual, 1, *currentTutor, *gatoEscolhido);
                    adocoesGatos.push_back(novaAdocao);
                }
                else {
                int newID = adocoesGatos.back().id + 1;

                AdocaoGato novaAdocao(dataAtual, newID, *currentTutor, *gatoEscolhido);
                adocoesGatos.push_back(novaAdocao);
                }
                
                cout << "Gato removido do abrigo com sucesso! Agora ele tera um novo lar :)\n";
            } 
            else {
                cout << "Gato nao encontrado no abrigo...\n";
            }   

            }
            catch(const exception& e) {
                cout << "Erro: " << e.what() << '\n';
                return;
            }
            catch (...) {
                cout << "erro inesperado..\n";
                return;
            }
            
            return;
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
#include<stdio.h>
#include<iostream>
#include "includes/Pessoa.h"
#include "includes/Voluntario.h"
#include "includes/Tutor.h"
#include "includes/Animal.h"
#include "includes/Cachorro.h"
#include "includes/Gato.h"
#include "includes/Abrigo.h"
#include "includes/Adocao.h"
#include "includes/AdocaoCachorro.h"
#include "includes/AdocaoGato.h"


using namespace std;

void menuPrincipal(Abrigo &abrigo);
void gerenciarVoluntarios(Abrigo &abrigo);
void gerenciarAnimais(Abrigo &abrigo);
void gerenciarAdocoes(Abrigo &abrigo);

int main() {
    cout << "[ BEM VINDO AO SISTEMA DE GERENCIAMENTO DE ABRIGO DE ANIMAIS ]\n\n";

    string nome, cnpj, telefone, endereco;
    cout << "Por favor, insira as informacoes do abrigo:\n";
    cout << "Nome: ";
    getline(cin, nome);
    cout << "CNPJ: ";
    getline(cin, cnpj);
    cout << "Telefone: ";
    getline(cin, telefone);
    cout << "Endereco: ";
    getline(cin, endereco);

    // Criando a instancia do abrigo
    Abrigo abrigo(nome, cnpj, telefone, endereco);
    
    
    cout << "\nConfiguracao inicial concluida!\n";
    while (abrigo.funcionarios.size() == 1) {
        cout << "O sistema requer pelo menos um voluntario real cadastrado.\n";
        cout << "Por favor, realize o cadastro de um novo voluntario para entao prosseguir ao menu principal:\n";
        abrigo.cadastrarVoluntario();
    }


    while (true) {
        cout << "\n[ MENU DE ACESSO ]\n";
        cout << "1 -  Efetuar login\n";
        cout << "2 -  Sair\n";
        cout << "Escolha uma das opcoes (1 ou 2): ";
        int opcao;
        cin >> opcao;
        cin.ignore();

        switch (opcao) {
            case 1: {
                string login, senha;
                cout << "Insira seus dados de login:\n";
                cout << "Login: ";
                cin >> login;
                cout << "Senha: ";
                cin >> senha;

                if (abrigo.voluntarioLogin(login, senha)) {
                    
                    cout << "Login efetuado com sucesso!!\n";
                    menuPrincipal(abrigo);
                } else {
                    
                    cout << "Login ou senha incorretos...\n";
                }
                break;
            }
            case 2:
                cout << "Saindo do sistema...\n";
                return 0;
            default:
                
                cout << "Opcao invalida... Tente novamente.\n";
                break;
        }
    }

    // Menu principal
    menuPrincipal(abrigo);
    return 0;
}

void menuPrincipal(Abrigo &abrigo) {
    while (true) {
        cout << "\n[ MENU PRINCIPAL ]\n";
        cout << "1 - Gerenciar voluntarios\n";
        cout << "2 - Gerenciar animais\n";
        cout << "3 - Gerenciar adocoes\n";
        cout << "4 - Sair\n";
        cout << "Escolha uma das opcoes (1, 2, 3 ou 4): ";
        int opcao;
        cin >> opcao;
        cin.ignore();

        switch (opcao) {
            case 1:
                gerenciarVoluntarios(abrigo);
                break;
            case 2:
                gerenciarAnimais(abrigo);
                break;
            case 3:
                gerenciarAdocoes(abrigo);
                break;
            case 4:
                cout << "Saindo do sistema...\n";
                return;
            default:
                cout << "Opcao invalida... Tente novamente.\n";
                break;
        }
    }
}

void gerenciarVoluntarios(Abrigo &abrigo) {
    cout << "\n[ GERENCIA DE VOLUNTARIOS ]\n";
    cout << "1 - Cadastrar novo voluntario\n";
    cout << "2 - Remover voluntario\n";
    cout << "3 - Retornar ao menu principal\n";
    cout << "Escolha uma das opcoes (1, 2 ou 3): ";
    int opcao;
    cin >> opcao;
    cin.ignore(); // Limpar buffer

    switch (opcao) {
        case 1:
            abrigo.cadastrarVoluntario();
            
            break;
        case 2:
            abrigo.removerVoluntario();
            
            break;
        case 3:
            return;
        default:
            cout << "Opcao invalida. Retornando ao menu principal.\n";
            break;
    }
}

void gerenciarAnimais(Abrigo &abrigo) {
    cout << "\n[ GERENCIA DE ANIMAIS ]\n";
    cout << "1 - Cadastrar novo animal\n";
    cout << "2 - Remover animal\n";
    cout << "3 - Listar animais disponiveis para adocao\n";
    cout << "4 - Retornar ao menu principal\n";
    cout << "Escolha uma das opcoes (1, 2, 3 ou 4): ";
    int opcao;
    cin >> opcao;
    cin.ignore(); 

    switch (opcao) {
        case 1:
            abrigo.cadastrarAnimal();   
            break;
        case 2:
            abrigo.removerAnimal();
            break;
        case 3:
            abrigo.listarAnimais();
            break;
        case 4:
            return;
        default:
            cout << "Opcao invalida... Retornando ao menu principal.\n";
            break;
    }
}

void gerenciarAdocoes(Abrigo &abrigo) {
    cout << "\n[ GERENCIAR ADOCOES ]\n";
    cout << "1 - Realizar adocao\n";
    cout << "2 - Listar adocoes\n";
    cout << "3 - Retornar ao menu principal\n";
    cout << "Escolha uma das opcoes (1, 2 ou 3): ";
    int opcao;
    cin >> opcao;
    cin.ignore();

    switch (opcao) {
        case 1:
            abrigo.realizarAdocao();
            break;
        case 2:
            abrigo.listarAdocoes();
            break;
        case 3:
            return;
        default:
            cout << "Opcao invalida... Retornando ao menu principal.\n";
            break;
    }
}

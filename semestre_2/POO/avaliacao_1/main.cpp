#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

//Nome: Cauã Felipe de França Nascimento
//OBS.: [Atualizado] erros de compilação resolvidos.

//classe Empresa
class Empresa {
    public:
        string nome;
        string cnpj;
        void setNome(string n) {
            nome = n;
        }
        void setCnpj(string c) {
            cnpj = c;
        }
        string getNome() const {
            return nome;
        };
        
};


//classe Pessoa
class Pessoa {
    public:
        string nome;
        int idade;
        void setNome(string n) {
            nome = n;
        }
        void setIdade(int i) {
            idade = i;
        }
        string getNome() const {
            return nome;
        }
};


//classe Trabalhador herdada de Pessoa com um atributo do tipo Empresa
class Trabalhador: public Pessoa {
    private:
        Empresa empresa;
        string cargo;
    public:
        void setEmpresa(Empresa &e) {
            empresa = e;
        }
        void setCargo(string c) {
            cargo = c;
        }

};

//classe Predio (principal do programa)
class Predio {
    public:
        std::vector<Empresa> salasComerciais;
        std::vector<Empresa> visitantesEmpresa;
        std::vector<Trabalhador> trabalhadores;
        std::vector<Pessoa> visitantePessoa;
        std::vector<Empresa> exVisitanteEmpresa;
        std::vector<Pessoa> exVisitantePessoa;

        void registrarEmpresa(Empresa &e) {
            salasComerciais.push_back(e);
        }

        //metodo que consultam quantos visitantes estao no predio
        int consultarVisitantesAtuais() {
            int total = visitantesEmpresa.size() + visitantePessoa.size();
            return total;
        }

        //metodo que consulta quantos visitantes estao no predio atualmente
        //somado aos que ja sairam do predio
        int consultarVisitantesTotais() {
            int total = visitantePessoa.size() + visitantesEmpresa.size() + exVisitanteEmpresa.size() + exVisitantePessoa.size();
            return total;
        }
        
    
};

//classe responsavel por realizar as operacoes do predio
//de forma resumida, essa classe é responsável por operar no prédio 
//optei por fazer apenas um método que poderá ser sobrescrito, pois utilizarei essa classe nas proximas que
//farão operações específicas no prédio
class OperacoesPredio {
    virtual void operar(Predio &predio) = 0;
};


//classe da operacao de entrada de empresa visitante
class EntradaEmpresa : public OperacoesPredio {
    private:
        Empresa empresa;
    public:
        EntradaEmpresa(Empresa &e) : empresa(e) {}

        void operar(Predio &predio) override {
            cout << "empresa visitante recebeu seu cracha" << endl;
            cout << "empresa visitante entrou" << endl;
            predio.visitantesEmpresa.push_back(empresa);
        }
};


//classe da operacao de entrada de pessoa visitante
class EntradaPessoaVisitante : public OperacoesPredio {
    private:
        Pessoa pessoa;
    public:
        EntradaPessoaVisitante(Pessoa p) : pessoa(p) {
            
        }
        
        void operar(Predio & predio) override {
            cout << "pessoa visitante recebeu seu cracha" << endl;
            cout << "pessoa visitante entrou" << endl;

            predio.visitantePessoa.push_back(pessoa);
        }
};


//classe da operacao de saida de empresa visitante
class SaidaEmpresaVisitante : public OperacoesPredio {
private:
    Empresa empresa;
public:
    SaidaEmpresaVisitante(Empresa &e) : empresa(e) {}


    void operar(Predio &predio) override {
        //funcao que remove a empresa da lista de visitantes
        auto it = remove_if(predio.visitantesEmpresa.begin(), predio.visitantesEmpresa.end(),
        [this](const Empresa &emp) {
            return emp.getNome() == empresa.getNome(); 
        });

        if (it != predio.visitantesEmpresa.end()) {
            predio.visitantesEmpresa.erase(it, predio.visitantesEmpresa.end());
            cout << "empresa visitante devolveu seu cracha" << endl;
            cout << "empresa visitante saiu" << endl;
        } else {
            cout << "erro: a empresa nao foi encontrada como visitante" << endl;
        }
        //a empresa é adicionada à lista de ex-visitantes
        predio.exVisitanteEmpresa.push_back(empresa);
    }
};


//classe da operacao de saida de pessoa visitante
class SaidaPessoaVisitante : public OperacoesPredio {
private:
    Pessoa pessoa;
public:
    SaidaPessoaVisitante(Pessoa p) : pessoa(p) {}

    void operar(Predio &predio) override {
        // função que remove a pessoa da lista de visitantes
        auto it = remove_if(predio.visitantePessoa.begin(), predio.visitantePessoa.end(),
        [this](const Pessoa &p) {
            return p.getNome() == pessoa.getNome();
        });

        if (it != predio.visitantePessoa.end()) {
            predio.visitantePessoa.erase(it, predio.visitantePessoa.end());
            cout << "pessoa visitante devolveu seu cracha" << endl;
            cout << "pessoa visitante saiu" << endl;
        } else {
            cout << "erro: a pessoa nao foi encontrada como visitante" << endl;
        }
        // Adiciona a pessoa à lista dos ex-visitantes
        predio.exVisitantePessoa.push_back(pessoa);
    }
};



int main() {
    Predio ifc;
    int choice;
    cout << "Olá! Seja bem vindo ao sistema de gerenciamento de entradas do predio XYZ!\n";
    while(1) {
        cout << "*********      Menu      *********\n";
        cout << "-- Escolha uma opcao abaixo\n";
        cout<<"---- 1) Registrar a entrada de uma pessoa visitante\n";
        cout<<"---- 2) Registrar a entrada de uma empresa visitante\n";
        cout<<"---- 3) Registrar a saida de uma pessoa visitante\n";
        cout<<"---- 4) Transference\n";
        cout<<"---- 5) Whithdrawal\n";
        cout<<"---- 6) Account details\n";
        cout<<"---- 7) Exit menu\n";
        cout<<"Enter your choice (1, 2, 3, 4, 5, 6 or 7): ";
        cin>>choice;
        cin.ignore();

        switch (choice) {
            case 1: {
                Pessoa newPessoa;
                string nome;
                int idade;
                cout << "Você escolheu registrar a entrada de uma pessoa visitante!\n";
                cout << "Insira os dados da pessoa visitante:\n";
                cout << "Nome: ";
                cin >> nome;
                cout << "\nIdade: ";
                cin >> idade;
                newPessoa.setNome(nome);
                newPessoa.setIdade(idade);
                EntradaPessoaVisitante entrada(newPessoa);
                entrada.operar(ifc);
                cout << "\nO (a) visitante " << nome << " recebeu o cracha de identificação e entrou no predio!\n";
                break;
            }
            case 2: {
                Empresa newEmpresa;
                string nome;
                string cnpj;
                cout << "Você escolheu registrar a entrada de uma empresa visitante!\n";
                cout << "Insira os dados da empresa visitante:\n";
                cout << "Nome: ";
                cin >> nome;
                cout << "\nCNPJ: ";
                cin >> cnpj;
                newEmpresa.setNome(nome);
                newEmpresa.setCnpj(cnpj);
                EntradaEmpresa empresaVisitando(newEmpresa);
                empresaVisitando.operar(ifc);
                cout << "\nA empresa " << nome << " recebeu o cracha de identificação e entrou no predio!\n";
                break;
            }
            /*
            case 3: {
                int number;
                double amount;
                cout << "You choose to deposit a certain amount to an account!\n";
                cout << "Enter the number of the account you wanna deposit: ";
                cin >> number;
                cout << "Enter the amount you wanna deposit: ";
                cin>>amount;
                DepositOperation accountDeposit(number, amount);
                accountDeposit.operate(bank);
                break;
            }
            case 4: {
                int number1;
                int number2;
                int amount;
                cout << "You choose the transference option!\n";
                cout << "Enter the number of the account you wanna transfer the amount from: ";
                cin >> number1;
                cout << "Enter the number of the account you wanna transfer the amount for: ";
                cin >> number2;
                cout << "Enter the transference amount: ";
                cin>>amount;
                TransferOperation transference(number1, number2, amount);
                transference.operate(bank);
                break;
            }
            case 5: {
                int number;
                double amount;
                cout << "You choose the whithdrawal option!\n";
                cout << "Enter the number of the account you wanna whithdraw: ";
                cin >> number;
                cout << "Enter the amount you wanna whithdraw: ";
                cin>>amount;
                WithdrawalOperation accountWhithdraw(number, amount);
                accountWhithdraw.operate(bank);
                break;
            }
            case 6: {
                int number;
                cout << "You choose the account details option!\n";
                cout << "Enter the number of the account you wanna check details: ";
                cin >> number;
                StatusOperation accountDetails(number);
                accountDetails.operate(bank);
                break;
            }
            case 7: {
                cout << "Exiting... Thank you!\n";
                return 0;
            }
            default:
                cout << "Invalid choice! Please try again.\n";
        }
    char again;
        cout << "Do you want to return to the menu? (Y/N): ";
        cin >> again;
        if (again != 'Y' && again != 'y') {
            cout << "Exiting... Thank you!\n";
            break;
        }
*/
}


    //exemplos de teste

    //criacao do predio

    //criacao de uma empresa
    Empresa schneider;
    schneider.setNome("schneider");
    schneider.setCnpj("231342135412");

    //criacao de um trabalhador
    Trabalhador caua;
    caua.setEmpresa(schneider);
    caua.setCargo("Estagiario");

    //criacao de uma pessoa aleatoria que sera visitante
    Pessoa ronaldo;

    //operacao de entrada do visitante ronaldo
    EntradaPessoaVisitante entrada(ronaldo);
    entrada.operar(ifc);

    //operacao de saida do ronaldo visitante
    
    
    SaidaPessoaVisitante pessoaSaindo(ronaldo);
    pessoaSaindo.operar(ifc);


    //operacao de entrada da empresa schneider
    EntradaEmpresa empresaVisitando(schneider);
    empresaVisitando.operar(ifc);

    //operacao de saida da empresa
    SaidaEmpresaVisitante empresaSaindo(schneider);
    empresaSaindo.operar(ifc);
    
    //registro de empresa no predio ifc
    ifc.registrarEmpresa(schneider);

    Pessoa junior;

    EntradaPessoaVisitante entraJunior(junior);
    entraJunior.operar(ifc);

    cout << "Numero de visitantes atuais no predio: " << ifc.consultarVisitantesAtuais() << endl;
    cout << "Numero de visitantes totais: " << ifc.consultarVisitantesTotais() << endl;



    return 0;
}

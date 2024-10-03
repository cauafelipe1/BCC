#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;
/*
Tarefa: Crie um sistema bancário para gerenciar contas e aplicações de uma pessoa, com as operações de depósito,
saque, transferência, extrato, abertura e encerramento de contas. 
Task: Create a bank system to manage accounts and applications of someone, with the operations of deposit, withdrawal,
transference, extract, account register and account closure.

PS: This is a 1.0 version, something you can call the 'skeleton' of this system.
Eventually, the system will be updated and incorporate more polished methods, make sure to check new updates on:
 https://github.com/cauafelipe1/BCC/tree/main/semestre_2/POO/bank_system
*/

//Account class with name, number and balance as it respectives attributes
class Account {
    public:
        Account( std::string name, int number, double balance) {
            this->name = name;
            this->number = number;
            this->balance = balance;    
        }
        
        std::string name;
        int number;
        double balance;
};

//Bank class holding a vector/list of accounts
class Bank {
    public:
        std::vector<Account> accounts;

        //method to return an account of the list
        Account* getAccountByNumber(int accountNumber) {
        for (auto& account : accounts) {
            if (account.number == accountNumber) {
                return &account; // return the pointer of an account if it is in the vector
            }
        }
        return nullptr; // return a null pointer (nullptr) if no account matched
    }
};

//"abstract" class where bank operations are made
class BankOperation {
    virtual void operate(Bank &bank) = 0;

};

//classes for especific operations inheriting the BankOperation class 
class RegisterOperation: public BankOperation{
    public:
    RegisterOperation(std::string name) : name(std::move(name)), number(rand()), balance(0) {}

    std::string name;
    int number;
    double balance;

    void operate(Bank &bank) override {
        cout << "Account created with success! Your account number is " << number << endl;
        bank.accounts.emplace_back(name, number, balance);
    }
};
    
class DepositOperation: public BankOperation {
    public:
        DepositOperation(int accountNumber, double amount) {
                this->accountNumber = accountNumber;
                this->amount = amount;
            }
        int accountNumber;
        double amount;

    void operate(Bank &bank) override {

        Account* account = bank.getAccountByNumber(accountNumber);
        account->balance += amount;
    }
        
};

class WithdrawalOperation: public BankOperation {
    public:
        WithdrawalOperation(int accountNumber, double amount) {
                this->accountNumber = accountNumber;
                this->amount = amount;
            }
        int accountNumber;
        double amount;

    void operate(Bank &bank) override {
        Account* account = bank.getAccountByNumber(accountNumber);
        if (account->balance > amount) {
            account->balance -= amount;
        }
    }
        
};

class TransferOperation: public BankOperation {
    public:
        TransferOperation(int accountNumber1, int accountNumber2, double amount) {
                this->accountNumber1 = accountNumber1;
                this->accountNumber2 = accountNumber2;
                this->amount = amount;
            }
        int accountNumber1;
        int accountNumber2;
        double amount;

    void operate(Bank &bank) override {
        Account* account1 = bank.getAccountByNumber(accountNumber1);
        Account* account2 = bank.getAccountByNumber(accountNumber2);
        account1->balance -= amount;
        account2->balance += amount;
    }
        
};

class StatusOperation: public BankOperation {
    public:
        StatusOperation(int accountNumber) {
                this->accountNumber = accountNumber;
            }
        int accountNumber;
    void operate(Bank &bank) override {
        Account* account = bank.getAccountByNumber(accountNumber);
        cout << "Account status:" << endl;
        cout << "Name: " << account->name << endl;
        cout << "Number: " << account->number << endl;
        cout << "Balance: " << account->balance << endl;
    }
        
};

class RemoveOperation: public BankOperation {
public:
    RemoveOperation(int accountNumber) : accountNumber(accountNumber) {}

    int accountNumber;

    void operate(Bank &bank) override {
        auto it = std::remove_if(bank.accounts.begin(), bank.accounts.end(),
            [this](const Account& account) {
                return account.number == accountNumber;
            });

        if (it != bank.accounts.end()) {
            bank.accounts.erase(it, bank.accounts.end());
            cout << "Account removed successfully!" << endl;
        } else {
            cout << "Account not found!" << endl;
        }
    }
};

//User Interface
int main() {
    Bank bank;
    int choice;
    cout << "Hello there! Welcome to the 1.0 version of a bank system\n";
    cout << "Beware! Im giving you the POWER to manage every account of this system as you want, so be careful...\n";
    while(1) {
        cout << "*********      Menu      *********\n";
        cout << "-- Choose your option bellow\n";
        cout<<"---- 1) Register a new account\n";
        cout<<"---- 2) Remove an existing account\n";
        cout<<"---- 3) Deposit\n";
        cout<<"---- 4) Transference\n";
        cout<<"---- 5) Whithdrawal\n";
        cout<<"---- 6) Account details\n";
        cout<<"---- 7) Exit menu\n";
        cout<<"Enter your choice (1, 2, 3, 4, 5, 6 or 7): ";
        cin>>choice;
        cin.ignore();

        switch (choice) {
            case 1: {
                std::string name;
                cout << "You choose to create a new account!\n";
                cout << "Set the name of the account owner: ";
                cin >> name;
                RegisterOperation accountRegistered(name);
                accountRegistered.operate(bank);
                break;

            }
            case 2: {
                int number;
                cout << "You choose to remove an existing account!\n";
                cout << "Enter the number of the account you wanna remove: ";
                cin >> number;
                RemoveOperation accountRemoved(number);
                accountRemoved.operate(bank);
                break;
            }
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
}
    return 0;
}
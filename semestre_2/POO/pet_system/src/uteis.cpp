#include <iostream>
#include <exception>
#include <ctime>
#include "../includes/uteis.h"
using namespace std;

string criptografar(const string& senha, char chave) {
   string result = senha;
    for (size_t i = 0; i < senha.size(); i++)
    {
        result[i] ^= chave;
    }
    return result;
    
}

void clearInputBuffer() {
    cin.clear();
    cin.ignore();
}

string obterDataAtual() {
    time_t agora = time(nullptr);
    tm* tempoLocal = localtime(&agora);

    char buffer[9];
    strftime(buffer, sizeof(buffer), "%d/%m/%Y", tempoLocal);

    return string(buffer);
}

#include<iostream>
#include<cmath>
using namespace std;

/*
Crie uma classe chamada Quadrado que tenha o atributo lado e os métodos area(), diagonal() e perimetro(). Faça uma classe de teste que permita:
    - imprimir o lado do quadrado
    - modificar o lado do quadrado
    - mostrar a área do quadrado
    - mostrar a diagonal do quadrado
    - mostrar o perímetro do quadrado
*/
class Quadrado {
    //atributo lado
    private:
        int lado;
    public:
        //setter
        void set_lado(int l) {
            lado = l;
        }
        //getter
        int get_lado() {
            return lado;
        }

        //funcoes de operacoes
        int area(int lado) {
            int result = lado * lado;
            return result;
        }

        float diagonal(int lado) {
            float result = (lado * sqrt(2));
            return result;
        }
        int perimetro(int lado) {
            int result = lado * 4;
            return result;
        }

};

//classe de teste
class TestarQuadrado {
    public:
        void imprimirQuadrado(Quadrado &quadrado) {
            cout << "Seu quadrado tem " << quadrado.get_lado() << " de lado" << endl;
        }
        void modificarQuadrado(Quadrado &quadrado) {
            cout << "[Modificando o valor do lado]" << endl;
            int novo_lado;
            cout << "Insira um valor novo para o lado do quadrado: ";
            cin >> novo_lado;
            quadrado.set_lado(novo_lado);
        }
        void mostrarArea(Quadrado &quadrado) {
            cout << "A area do quadrado tem valor de " << quadrado.area(quadrado.get_lado()) << endl;
        }
        
        void mostrarDiagonal(Quadrado &quadrado) {
            cout << "A diagonal do quadrado tem valor aproximado de " << quadrado.diagonal(quadrado.get_lado()) << endl;
        }
        void mostrarPerimetro(Quadrado &quadrado) {
            cout << "O perimetro do quadrado tem valor de " << quadrado.perimetro(quadrado.get_lado()) << endl;
        }
};

int main() {
    //execucao de testes
    Quadrado quadrado;
    int lado;
    cout << "Insira um valor para o lado do quadrado: ";
    cin >> lado;
    quadrado.set_lado(lado);
    TestarQuadrado teste;

    teste.imprimirQuadrado(quadrado);
    teste.modificarQuadrado(quadrado);
    teste.mostrarArea(quadrado);
    teste.mostrarDiagonal(quadrado);
    teste.mostrarPerimetro(quadrado);
    return 0;
}
#include<iostream>
using namespace std;

/*Crie uma classe chamada Retângulo que tenha os atributos altura e largura. Faça uma classe de teste para:
   - modificar os atributos
   - imprimir a área do retângulo
   - imprimir o perímetro do retângulo
*/
class Retangulo {
    //atributos privados altura e largura
    private:
        int altura;
        int largura;
    public:
        //setters
        void set_altura(int a){
            altura = a;
        }

        void set_largura(int l) {
            largura = l;
        }

        //getters
        int get_altura() {
            return altura;
        }
        int get_largura() {
            return largura;
        }
};

class TestarRetangulo {
    //objeto retangulo
    Retangulo retangulo;
    public:

        //classe modificadora de valores
        void modificarValores(Retangulo &retangulo) {
            int nova_altura;
            cout << "Insira uma nova altura: ";
            cin >> nova_altura;
            int nova_largura;
            cout << "Insira uma nova largura: ";
            cin >> nova_largura;
            retangulo.set_altura(nova_altura);
            retangulo.set_largura(nova_largura);
        }
        //classe que imprime a area do retangulo
        void imprimirArea(int altura, int largura) {
            cout << "Area do retangulo: " << (altura * largura) << "\n";
        }
        //classe que imprime o perimetro do retangulo
        void imprimirPerimetro(int altura, int largura) {
            cout << "Perimetro do retangulo: " << ((altura * 2) + (largura * 2));
        }
};


int main() {
    Retangulo retangulo;
    int altura_local;
    int largura_local;

    //testes
    cout << "Insira um valor para a altura do retangulo: ";
    cin >> altura_local;
    cout << "Insira um valor para a largura do retangulo: ";
    cin >> largura_local;
    retangulo.set_altura(altura_local);
    retangulo.set_largura(largura_local);

    cout << "Seu retangulo tem altura de " << retangulo.get_altura() << " e largura de " << retangulo.get_largura() << "\n";

    //testes utilizando a classe de teste
    TestarRetangulo teste;
    cout << "[Teste de modificacao de valores]\n";
    teste.modificarValores(retangulo);

    altura_local = retangulo.get_altura();
    largura_local = retangulo.get_largura();

    cout << "Seu retangulo agora com o valores modificados tem " << altura_local << " de altura e " << largura_local << " de largura\n";
    teste.imprimirArea(altura_local, largura_local);
    teste.imprimirPerimetro(altura_local, largura_local);
    return 0;
}
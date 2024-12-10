SRC := ./src
INC := ./includes

output: main.o Pessoa.o Voluntario.o Animal.o Gato.o Cachorro.o Tutor.o Adocao.o AdocaoGato.o AdocaoCachorro.o Abrigo.o
	g++ main.o Pessoa.o Voluntario.o Animal.o Gato.o Cachorro.o Tutor.o Adocao.o AdocaoGato.o AdocaoCachorro.o Abrigo.o -o output

main.o: main.cpp
	g++ -c main.cpp	

Pessoa.o: $(SRC)/Pessoa.cpp $(INC)/Pessoa.h
	g++ -c $(SRC)/Pessoa.cpp

Voluntario.o: $(SRC)/Voluntario.cpp $(INC)/Voluntario.h
	g++ -c $(SRC)/Voluntario.cpp

Animal.o: $(SRC)/Animal.cpp $(INC)/Animal.h
	g++ -c $(SRC)/Animal.cpp

Gato.o: $(SRC)/Gato.cpp $(INC)/Gato.h
	g++ -c $(SRC)/Gato.cpp

Cachorro.o: $(SRC)/Cachorro.cpp $(INC)/Cachorro.h
	g++ -c $(SRC)/Cachorro.cpp


Tutor.o: $(SRC)/Tutor.cpp $(INC)/Tutor.h
	g++ -c $(SRC)/Tutor.cpp

Adocao.o: $(SRC)/Adocao.cpp $(INC)/Adocao.h
	g++ -c $(SRC)/Adocao.cpp


AdocaoGato.o: $(SRC)/AdocaoGato.cpp $(INC)/AdocaoGato.h
	g++ -c $(SRC)/AdocaoGato.cpp

AdocaoCachorro.o: $(SRC)/AdocaoCachorro.cpp $(INC)/AdocaoCachorro.h
	g++ -c $(SRC)/AdocaoCachorro.cpp

Abrigo.o: $(SRC)/Abrigo.cpp $(INC)/Abrigo.h
	g++ -c $(SRC)/Abrigo.cpp


clean:
	rm *.o output
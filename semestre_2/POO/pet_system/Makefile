SRC := ./src
INC := ./includes
BIN := ./bin

all: $(BIN) $(BIN)/output

$(BIN):
	if [ ! -d $(BIN) ]; then mkdir $(BIN); fi

$(BIN)/output: $(BIN)/main.o $(BIN)/Pessoa.o $(BIN)/Voluntario.o $(BIN)/Animal.o $(BIN)/Gato.o $(BIN)/Cachorro.o $(BIN)/Tutor.o $(BIN)/Adocao.o $(BIN)/AdocaoGato.o $(BIN)/AdocaoCachorro.o $(BIN)/Abrigo.o $(BIN)/uteis.o
	g++ $(BIN)/main.o $(BIN)/Pessoa.o $(BIN)/Voluntario.o $(BIN)/Animal.o $(BIN)/Gato.o $(BIN)/Cachorro.o $(BIN)/Tutor.o $(BIN)/Adocao.o $(BIN)/AdocaoGato.o $(BIN)/AdocaoCachorro.o $(BIN)/Abrigo.o $(BIN)/uteis.o -o $(BIN)/output

$(BIN)/main.o: main.cpp
	g++ -c main.cpp	-o $(BIN)/main.o 

$(BIN)/Pessoa.o: $(SRC)/Pessoa.cpp $(INC)/Pessoa.h
	g++ -c $(SRC)/Pessoa.cpp -o $(BIN)/Pessoa.o

$(BIN)/Voluntario.o: $(SRC)/Voluntario.cpp $(INC)/Voluntario.h
	g++ -c $(SRC)/Voluntario.cpp -o  $(BIN)/Voluntario.o 

$(BIN)/Animal.o: $(SRC)/Animal.cpp $(INC)/Animal.h
	g++ -c $(SRC)/Animal.cpp -o $(BIN)/Animal.o

$(BIN)/Gato.o: $(SRC)/Gato.cpp $(INC)/Gato.h
	g++ -c $(SRC)/Gato.cpp -o $(BIN)/Gato.o 

$(BIN)/Cachorro.o: $(SRC)/Cachorro.cpp $(INC)/Cachorro.h
	g++ -c $(SRC)/Cachorro.cpp -o $(BIN)/Cachorro.o 


$(BIN)/Tutor.o: $(SRC)/Tutor.cpp $(INC)/Tutor.h
	g++ -c $(SRC)/Tutor.cpp -o $(BIN)/Tutor.o 

$(BIN)/Adocao.o: $(SRC)/Adocao.cpp $(INC)/Adocao.h
	g++ -c $(SRC)/Adocao.cpp -o $(BIN)/Adocao.o 


$(BIN)/AdocaoGato.o: $(SRC)/AdocaoGato.cpp $(INC)/AdocaoGato.h
	g++ -c $(SRC)/AdocaoGato.cpp -o $(BIN)/AdocaoGato.o 

$(BIN)/AdocaoCachorro.o: $(SRC)/AdocaoCachorro.cpp $(INC)/AdocaoCachorro.h
	g++ -c $(SRC)/AdocaoCachorro.cpp -o $(BIN)/AdocaoCachorro.o 

$(BIN)/Abrigo.o: $(SRC)/Abrigo.cpp $(INC)/Abrigo.h
	g++ -c $(SRC)/Abrigo.cpp -o $(BIN)/Abrigo.o 
	
$(BIN)/uteis.o: $(SRC)/uteis.cpp $(INC)/uteis.h
	g++ -c $(SRC)/uteis.cpp -o $(BIN)/uteis.o

clean:
	@if [ -d $(BIN) ]; then rm $(BIN)/*; fi
	@if [ -d $(BIN) ]; then rmdir $(BIN); fi
# HeliK -- Makefile

CC := g++
CXXFLAGS := $(pkg-config --cflags SDL2) -Iinclude -std=c++11 -Wall -Wextra
LDFLAGS :=  $(pkg-config --libs SDL2) -static-libgcc -static-libstdc++ -Wl,-Bstatic -lstdc++ --static
EXE := HeliK

OBJS := obj/main.o obj/app.o obj/board.o

.PHONY: all clean

all: bin/${EXE}

clean:
	@echo "[ RM ] bin"
	@rm -rf bin
	@echo "[ RM ] obj"
	@rm -rf obj

bin obj:
	@echo "[ MD ] $@"
	@mkdir -p "$@"

obj/%.o: src/%.cc | obj
	@echo "[  CXX  ] $< => $@"
	@${CXX} ${CXXFLAGS} -c "$<" -o "$@"

bin/${EXE}: ${OBJS} | bin
	@echo "[  LD  ] $@"
	@${CXX} -o "$@" ${OBJS} ${LDFLAGS}

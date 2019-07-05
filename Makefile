
all: clean build run
	./a.out

build:
	g++ puzzle1.cpp

run: a.out
	./a.out

clean:
	rm -f temp
	rm -f a.out

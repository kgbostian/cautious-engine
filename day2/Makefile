
all: clean build run

build:
	g++ -g puzzle2.cpp -o Day2

run: Day2
	./Day2

clean:
	rm -f temp
	rm -f Day2

debug: Day2
	gdb Day2

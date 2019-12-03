
all: clean build run

build:
	g++ -g puzzle3.cpp -o Day3

run: Day3
	./Day3

clean:
	rm -f temp
	rm -f Day3

debug: Day3
	gdb Day3

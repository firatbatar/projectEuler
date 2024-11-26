GCC := g++
CFLAGS := -Wall

all:
# Empty

%: cpp/%.cpp cpp/main.cpp
	$(GCC) $(CFLAGS) -o $@.out $^

clean:
	rm -f *.out
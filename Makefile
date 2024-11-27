GCC := g++
CFLAGS := -Wall

all:
# Empty

.PHONY: cpp cpp/%.cpp clean

%: cpp/%.cpp cpp/main.cpp
	@$(GCC) $(CFLAGS) -o $@.out $^

clean:
	@rm -f *.out
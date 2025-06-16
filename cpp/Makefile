GCC := g++
CFLAGS := -Wall

all:
# Empty

.PHONY: cpp cpp/%.cpp clean

%: cpp/%.cpp cpp/main.cpp
	@$(GCC) $(CFLAGS) -o $@.out $^

create:
	@cp cpp/.template cpp/$(name).cpp
	@echo "Created cpp/$(name).cpp"

clean:
	@rm -f *.out
GCC := g++
CFLAGS := -Wall

all:
# Empty

.PHONY: problems/%.cpp clean

%: problems/%.cpp main.cpp
	@$(GCC) $(CFLAGS) -o $@.out $^

create:
	@cp .template problems/$(name).cpp
	@echo "Created problems/$(name).cpp"

clean:
	@rm -f *.out
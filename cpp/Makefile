GCC := g++
CFLAGS := -Wall -I.

all:
# Empty

.PHONY: problems/%.cpp clean

%: problems/%.cpp
	$(GCC) $(CFLAGS) -o $@.out $^

clean:
	@rm -f *.out
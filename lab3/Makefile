CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2

TARGET = app
SOURCES = main.cpp Account.cpp Transaction.cpp
OBJECTS = $(SOURCES:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET)

main.o: main.cpp Account.h Transaction.h
Account.o: Account.cpp Account.h
Transaction.o: Transaction.cpp Transaction.h

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: all clean

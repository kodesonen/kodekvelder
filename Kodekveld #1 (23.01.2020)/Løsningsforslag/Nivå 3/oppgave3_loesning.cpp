#include "pch.h"
#include <iostream>
#include <string>

int primes[] = { 2, 11, 17, 19 };

std::string foo[] = {"Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
					 "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima",
					 "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo",
					 "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray",
					 "Yankee", "Zulu"};

struct B {
	virtual char foo(std::string b) {
		char a = b.at(0);
		int B = (int)a - 65;

		for (int j = 0; j < (sizeof(primes) / sizeof(primes[0])); j++) {
			if (B == primes[j]) {
				return a;
			}
		}
	}
};

struct A : B {
	virtual char foo(char b) = 0;
};

char A::foo(char b) {
	return b;
}

struct D : A {
	char foo(std::string a) override {}
};

char a(std::string a) {
	B b;
	char D;

	D = b.foo(a);

	return D;

}

char b(std::string b) {
	char B;
	int A = b.length();

	for (int j = 0; j < A; ++j) {
		B = a(b);
	}

	return B;
}

int main() {
	std::cout << std::endl;
	for (int i = 0; i < 25; i++) {
		std::cout << b(foo[i]);
	}
	std::cout << std::endl;
}
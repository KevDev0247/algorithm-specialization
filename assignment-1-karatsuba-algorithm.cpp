#include <iostream>
#include <stdio.h>
#include <sstream>
#include <math.h>

int karatsubaAlgorithm(std::string num1, std::string num2) {
	int a, b, c, d, ac, bd, multiple_ab_cd;

	std::string a_string = num1;
	std::string b_string = num1;
	std::string c_string = num2;
	std::string d_string = num2;

	std::cout << "1 length: " << num1.length() << "; 2 length: " << num2.length() << std::endl;

	a_string.erase((num1.length() / 2), num1.length() - 1);
	b_string.erase(0, (num1.length() / 2));
	c_string.erase((num2.length() / 2), num2.length() - 1);
	d_string.erase(0, (num2.length() / 2));

	std::cout << "a " << a_string << "; b " << b_string << "; c " << c_string << "; d " << d_string << std::endl;

	std::istringstream(a_string) >> a;
	std::istringstream(b_string) >> b;
	std::istringstream(c_string) >> c;
	std::istringstream(d_string) >> d;

	if (a_string.length() > 2) {
		ac = karatsubaAlgorithm(a_string, b_string);
		bd = karatsubaAlgorithm(c_string, d_string);
	}
	else {
		ac = a * c;
		bd = b * d;
	}

	std::cout << "ac: " << ac << "; bd: " << bd << std::endl;

	int sum_ab = a + b;
	int sum_cd = c + d;

	if (std::to_string(sum_ab).length() > 2 && std::to_string(sum_cd).length() > 2) {
		multiple_ab_cd = karatsubaAlgorithm(std::to_string(sum_ab), std::to_string(sum_cd));
	}
	else {
		multiple_ab_cd = sum_ab * sum_cd;
	}

	int sum_ad_bc = multiple_ab_cd - ac - bd;

	std::cout << "sum_ad_bc: " << multiple_ab_cd << std::endl;

	std::cout << "ad + bc: " << multiple_ab_cd - ac - bd << std::endl;

	std::cout << "result: " << pow(10, 2 * a_string.length()) * ac + pow(10, a_string.length()) * sum_ad_bc + bd << std::endl;

	return pow(10, 2 * a_string.length()) * ac + pow(10, a_string.length()) * sum_ad_bc + bd;
}

int main() {
	std::string num1 = "1234";
	std::string num2 = "5678";

	std::cout << karatsubaAlgorithm(num1, num2) << std::endl;
}
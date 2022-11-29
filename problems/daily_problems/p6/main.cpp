
#include <iostream>
#include "List.h"

int main (int argc, char *argv[]) {
    std::cout << "Hello world" << std::endl;
    XorList* list = new XorList();
    list->add(0);
    list->add(1);
    list->add(2);
    list->add(3);
    list->add(4);
    list->add(5);

    std::cout << list->get(0) << std::endl;
    std::cout << list->get(1) << std::endl;
    std::cout << list->get(2) << std::endl;
    std::cout << list->get(3) << std::endl;
    std::cout << list->get(4) << std::endl;
    std::cout << list->get(5) << std::endl;
}
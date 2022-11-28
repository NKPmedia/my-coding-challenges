//
// Created by pauli on 28.11.22.
//

#ifndef MY_CODING_CHALLENGES_LIST_H
#define MY_CODING_CHALLENGES_LIST_H


#include "Element.h"

class XorList {
public:
    XorList();
    void add(int val);
    int get(int index);
private:
    Element* first;
    Element* last;
};


#endif //MY_CODING_CHALLENGES_LIST_H

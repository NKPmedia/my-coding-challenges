//
// Created by pauli on 28.11.22.
//

#include "List.h"
#include <stdint.h>

XorList::XorList() {
    this->first = nullptr;
    this->last = nullptr;
}

void XorList::add(int val) {
    auto* newEle = new Element(val);
    if (this->first == nullptr) {
        this->first = newEle;
        this->last = newEle;
    } else {
        this->last->both = (Element*) ((uintptr_t) this->last->both ^ (uintptr_t) newEle);
        newEle->both = this->last;
        this->last = newEle;
    }
}

int XorList::get(int index) {
    Element* currentElem = this->first;
    Element* lastElem = nullptr;
    if (index == 0) {
        return currentElem->val;
    }
    for (int i = 1; i <= index; i++) {
        Element* tmp = currentElem;
        currentElem = (Element*) ((uintptr_t) lastElem ^ (uintptr_t) currentElem->both);
        lastElem = tmp;
    }
    return currentElem->val;
}

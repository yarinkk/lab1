#include "Account.h"
#include <iostream>

Account::Account(const std::string &owner, double initialBalance)
    : owner_(owner), balance_(initialBalance) {}

void Account::deposit(double amount) {
    if (amount > 0) {
        balance_ += amount;
        std::cout << "Поповнення: +" << amount << " грн\n";
    } else {
        std::cout << "Сума має бути більшою за 0!\n";
    }
}

bool Account::withdraw(double amount) {
    if (amount <= 0) {
        std::cout << "Сума має бути більшою за 0!\n";
        return false;
    }
    if (amount > balance_) {
        std::cout << "Недостатньо коштів на рахунку!\n";
        return false;
    }
    balance_ -= amount;
    std::cout << "Зняття: -" << amount << " грн\n";
    return true;
}

double Account::balance() const {
    return balance_;
}

const std::string &Account::owner() const {
    return owner_;
}

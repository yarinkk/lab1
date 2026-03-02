// Файл: Account.h

#ifndef ACCOUNT_H
#define ACCOUNT_H

#include <string>

class Account {
private:
    std::string owner_;
    double balance_;

public:
    Account(const std::string &owner, double initialBalance = 0.0);

    void deposit(double amount);
    bool withdraw(double amount);
    double balance() const;
    const std::string &owner() const;
};

#endif 

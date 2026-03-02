#ifndef TRANSACTION_H
#define TRANSACTION_H

#include <string>
#include <ctime>

class Transaction {
private:
    std::string type_;   // "deposit" або "withdraw"
    double amount_;
    std::string date_;   // дата у вигляді "YYYY-MM-DD HH:MM"

    std::string currentDateTime() const;

public:
    Transaction(const std::string &type, double amount);

    std::string info() const;
};

#endif 

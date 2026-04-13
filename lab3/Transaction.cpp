#include "Transaction.h"
#include <sstream>
#include <iomanip>

Transaction::Transaction(const std::string &type, double amount)
    : type_(type), amount_(amount), date_(currentDateTime()) {}

std::string Transaction::currentDateTime() const {
    std::time_t now = std::time(nullptr);
    std::tm *ltm = std::localtime(&now);
    std::ostringstream oss;
    oss << std::put_time(ltm, "%Y-%m-%d %H:%M");
    return oss.str();
}

std::string Transaction::info() const {
    std::ostringstream oss;
    oss << "[" << date_ << "] "
        << (type_ == "deposit" ? "Поповнення" : "Зняття")
        << ": " << amount_ << " грн";
    return oss.str();
}

#include <iostream>
#include <vector>
#include "Account.h"
#include "Transaction.h"

int main() {
    std::cout << "=== Банківський рахунок ===\n";

    Account acc("Ярина", 1000.0);
    std::vector<Transaction> history;

    std::cout << "Початковий баланс: " << acc.balance() << " грн\n";

    // Поповнення
    acc.deposit(500);
    history.emplace_back("deposit", 500);

    // Спроба зняти більше, ніж є
    acc.withdraw(2000);
    history.emplace_back("withdraw", 2000);

    // Зняття допустимої суми
    acc.withdraw(300);
    history.emplace_back("withdraw", 300);

    std::cout << "\nІсторія транзакцій:\n";
    for (const auto &t : history) {
        std::cout << " - " << t.info() << "\n";
    }

    std::cout << "\nПоточний баланс: " << acc.balance() << " грн\n";
    std::cout << "===========================\n";

    return 0;
}

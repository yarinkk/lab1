#include <iostream>
#include <vector>
#include <windows.h>
using namespace std;

struct Transaction {
    string category;
    double amount;
};

vector<Transaction> transactions;

void addTransaction() {
    Transaction t;
    cout << "Введіть категорію: ";
    cin >> t.category;
    cout << "Введіть суму: ";
    cin >> t.amount;

    transactions.push_back(t);
    cout << "Транзакцію додано!\n";
}

void showTransactions() {
    if (transactions.empty()) {
        cout << "Список витрат порожній\n";
        return;
    }

    cout << "\nСписок витрат:\n";
    for (auto t : transactions) {
        cout << t.category << " - " << t.amount << endl;
    }
}

void totalSum() {
    double sum = 0;
    for (auto t : transactions) {
        sum += t.amount;
    }
    cout << "Загальна сума витрат: " << sum << endl;
}

int main() {
    // ✅ Фікс української мови
    SetConsoleOutputCP(65001);
    SetConsoleCP(65001);

    int choice;

    do {
        cout << "\n--- Меню ---\n";
        cout << "1. Додати витрату\n";
        cout << "2. Показати всі витрати\n";
        cout << "3. Загальна сума\n";
        cout << "0. Вихід\n";
        cout << "Ваш вибір: ";
        cin >> choice;

        switch(choice) {
            case 1: addTransaction(); break;
            case 2: showTransactions(); break;
            case 3: totalSum(); break;
            case 0: cout << "Вихід з програми...\n"; break;
            default: cout << "Невірний вибір!\n";
        }

    } while(choice != 0);

    return 0;
}
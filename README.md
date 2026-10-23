# Bank Account: The 4 Pillars of OOP

A small Python bank account example that shows the four pillars of Object-Oriented Programming. You can deposit money, withdraw money, and check the balance. A `SavingsAccount` adds a rule that it must always keep a minimum balance.

## The four pillars in this code

| Pillar | Where you can see it |
|---|---|
| **Encapsulation** | The account number and balance are private (`__accno`, `__bal`). They can only be changed through methods. |
| **Abstraction** | You just call `deposit()` or `withdraw()`. You do not need to know how the balance is updated inside. |
| **Inheritance** | `SavingsAccount` gets deposit, balance check and more from `BankAccount`. |
| **Polymorphism** | `withdraw()` works on both account types, but a savings account behaves differently because it keeps a minimum balance. |

## How to run
You need Python 3. In a terminal:

```
python 4_pillars_of_OOP_example.py
```

## Sample output
```
You have deposited 20000.
Bank balance is 30000

You withdraw successfully 1000.
Bank balance is 29000

Bank balance is 29000

You cannot withdraw 4500.
A savings account must keep at least 1000.
Bank balance is 5000

You withdraw successfully 3000.
Bank balance is 2000

You withdraw successfully 100.
Bank balance is 28900

You withdraw successfully 100.
Bank balance is 1900
```

## Concepts used
- Classes, objects, and constructors
- Private attributes
- Inheritance with `super()`
- Method overriding
- Input checks (no deposits or withdrawals of zero or negative amounts)

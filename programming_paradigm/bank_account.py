#!/usr/bin/python3
"""
Module: bank_account
Defines a simple BankAccount class for basic banking operations.
"""


class BankAccount:
    """
    A simple bank account class that supports deposits,
    withdrawals, and displaying the current balance.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initialize the bank account with an optional initial balance.
        Defaults to 0.0 if no balance is provided.
        """
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful,
                  False if there were insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance}")

"""Core domain logic for the budget CLI application."""

from typing import TypedDict


class Transaction(TypedDict):
    """Transaction record stored by the budget application."""

    date: str
    type: str
    category: str
    description: str
    amount: int
    memo: str


def add_transaction(
    transactions: list[Transaction],
    transaction: Transaction,
) -> list[Transaction]:
    """Add a transaction and return a new transaction collection."""
    updated_transactions = transactions.copy()
    updated_transactions.append(transaction)
    return updated_transactions


def get_balance(transactions: list[Transaction]) -> float:
    """Return the total balance from all transaction amounts."""
    return float(sum(transaction["amount"] for transaction in transactions))

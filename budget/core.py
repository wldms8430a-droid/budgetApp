"""Core domain logic for the budget CLI application."""

import csv
from pathlib import Path

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


def filter_by_category(
    transactions: list[Transaction],
    category: str,
) -> list[Transaction]:
    """Return transactions whose category matches the requested value."""
    normalized_category = category.lower()
    return [
        transaction
        for transaction in transactions
        if transaction["category"].lower() == normalized_category
    ]


def load_transactions_from_csv(file_path: str) -> list[Transaction]:
    """Load transaction records from a BOM-compatible CSV file."""
    path = Path(file_path)
    with path.open(encoding="utf-8-sig", newline="") as csv_file:
        return [
            {
                "date": row["date"],
                "type": row["type"],
                "category": row["category"],
                "description": row["description"],
                "amount": int(row["amount"]),
                "memo": row["memo"],
            }
            for row in csv.DictReader(csv_file)
        ]

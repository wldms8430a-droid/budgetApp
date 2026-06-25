"""Core module tests."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the collection length."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        },
        {
            "date": "2026-01-07",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 3500000,
            "memo": "1월급여",
        },
    ]
    new_transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    updated_transactions = add_transaction(transactions, new_transaction)

    assert len(updated_transactions) == len(transactions) + 1


def test_add_transaction_keeps_negative_amount_expense() -> None:
    """Expense transactions should preserve a negative amount."""
    transactions: list[dict[str, object]] = []
    new_transaction = {
        "date": "2026-01-12",
        "type": "지출",
        "category": "식비",
        "description": "편의점",
        "amount": -5800,
        "memo": "",
    }

    updated_transactions = add_transaction(transactions, new_transaction)

    assert updated_transactions[-1]["amount"] == -5800


def test_add_transaction_keeps_positive_amount_income() -> None:
    """Income transactions should preserve a positive amount."""
    transactions: list[dict[str, object]] = []
    new_transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "중고 판매",
        "amount": 25000,
        "memo": "중고마켓",
    }

    updated_transactions = add_transaction(transactions, new_transaction)

    assert updated_transactions[-1]["amount"] == 25000


def test_add_transaction_allows_empty_description() -> None:
    """Transactions should be stored even when description is empty."""
    transactions: list[dict[str, object]] = []
    new_transaction = {
        "date": "2026-01-20",
        "type": "지출",
        "category": "교통",
        "description": "",
        "amount": -15000,
        "memo": "",
    }

    updated_transactions = add_transaction(transactions, new_transaction)

    assert updated_transactions[-1]["description"] == ""

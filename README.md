# FinTech Pytest QA

A Python practice project for testing a simulated bank with pytest. It uses fictional accounts and keeps balances and transaction history in memory. Each new `Bank()` starts with the same account data.

## Project files

- `bank_app.py` contains the simulated banking application.
- `test_bank_app.py` contains the pytest suite.
- `.github/workflows/pytest.yml` runs the suite in GitHub Actions.

## Run the tests locally

From the project folder, run these commands with Python 3.13 installed.

```powershell
python -m pip install pytest
python -m pytest test_bank_app.py -v
```

The tests cover login, deposits, withdrawals, transfers, balance lookups, and transfer history. For example, the successful transfer test checks that the sender's balance decreases and the recipient's balance increases by the same amount.

## GitHub Actions

The **Bank tests** workflow runs pytest on pushes and pull requests. Open the repository's [Actions tab](https://github.com/sijuade11/FinTech-Pytest-QA/actions) to see the results. The workflow uses the simulated accounts created by the Python code.

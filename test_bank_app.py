from bank_app import Bank
def test_successful_login():
    bank = Bank()
    result = bank.login(1001, "pass123")
    assert result is True
def test_wrong_password():
    bank = Bank()
    result = bank.login(1001, "wrong456")
    assert result is False
def test_nonexistent_account():
    bank = Bank()
    result = bank.login(9999, "pass123")
    assert result is False
def test_successful_deposit():
    bank = Bank()
    result = bank.deposit(1001, 1000)
    assert result == "Deposit successful"
    assert bank.get_balance(1001) == 501000
def test_invalid_deposit_amount():
    bank = Bank()
    result = bank.deposit(1001, -500)
    assert result == "Invalid amount" 
def test_successful_login_account_1002():
    bank = Bank()
    result = bank.login(1002, "secure456")
    assert result is True       
def test_successful_withdrawal():
    bank = Bank()
    result = bank.withdraw(1002, 20000)
    assert result == "Withdrawal successful"
    assert bank.get_balance(1002) == 180000
def test_insufficient_funds_withdrawal():
    bank = Bank()
    result = bank.withdraw(1002, 300000)
    assert result == "Insufficient funds"
def test_successful_transfer():
    bank = Bank()
    result = bank.transfer(1001, 1002, 50000)
    assert result == "Transfer successful"
    assert bank.get_balance(1001) == 450000
    assert bank.get_balance(1002) == 250000
def test_zero_amount_transfer():
    bank = Bank()
    result = bank.transfer(1001, 1002, 0)
    assert result == "Invalid amount"
def test_wrong_password_account_1002():
    bank = Bank()
    result = bank.login(1002, "wrongpass")
    assert result is False
def test_insufficient_funds_transfer():
    bank = Bank()
    result = bank.transfer(1002, 1001, 600000)
    assert result == "Insufficient funds"  
def test_insufficient_funds_transfer_account_1003():
    bank = Bank()
    result = bank.transfer(1003, 1001, 1500000)
    assert result == "Insufficient funds" 
def test_invalid_deposit_amount_account_1003():
    bank = Bank()
    result = bank.deposit(1003, 0)
    assert result == "Invalid amount"
def test_successful_login_account_1003():
    bank = Bank()
    result = bank.login(1003, "bank789")
    assert result is True
def test_successful_deposit_account_1003():
    bank = Bank()
    result = bank.deposit(1003, 50000)
    assert result == "Deposit successful"
    assert bank.get_balance(1003) == 150000
def test_successful_withdrawal_account_1003():
    bank = Bank()
    result = bank.withdraw(1003, 50000)
    assert result == "Withdrawal successful"
    assert bank.get_balance(1003) == 50000
def test_fetch_balance():
    bank = Bank()
    balance = bank.get_balance(1001)
    assert balance == 500000
def test_deposit_valid_amount_1001():
    bank = Bank()
    result = bank.deposit(1001, 2000)
    assert result == "Deposit successful"
    assert bank.get_balance(1001) == 502000
def test_transaction_history_after_transfer():
    bank = Bank()
    result = bank.transfer(1002, 1001, 50000)
    assert result == "Transfer successful"

    sender_history = bank.get_transactions(1002)
    receiver_history = bank.get_transactions(1001)

    assert sender_history == [{"type": "transfer_out", "amount": 50000}]
    assert receiver_history == [{"type": "transfer_in", "amount": 50000}]
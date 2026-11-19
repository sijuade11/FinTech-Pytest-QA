class Bank:
    def __init__(self):
        self.accounts = {
            1001: {"password": "pass123", "balance": 500000, "transactions": []},
            1002: {"password": "secure456", "balance": 200000, "transactions": []},
            1003: {"password": "bank789", "balance": 100000, "transactions": []}
        }

    def login(self, account_id, password):
        if account_id not in self.accounts:
            return False
        return self.accounts[account_id]["password"] == password

    def get_balance(self, account_id):
        if account_id not in self.accounts:
            return "Account not found"
        return self.accounts[account_id]["balance"]

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            return "Account not found"
        if amount <= 0:
            return "Invalid amount"

        self.accounts[account_id]["balance"] += amount
        self.accounts[account_id]["transactions"].append(
            {"type": "deposit", "amount": amount}
        )
        return "Deposit successful"

    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            return "Account not found"
        if amount > self.accounts[account_id]["balance"]:
            return "Insufficient funds"

        self.accounts[account_id]["balance"] -= amount
        self.accounts[account_id]["transactions"].append(
            {"type": "withdrawal", "amount": amount}
        )
        return "Withdrawal successful"

    def transfer(self, sender_id, receiver_id, amount):
        if sender_id not in self.accounts or receiver_id not in self.accounts:
            return "Account not found"
        if amount <= 0:
            return "Invalid amount"
        if amount > self.accounts[sender_id]["balance"]:
            return "Insufficient funds"

        self.accounts[sender_id]["balance"] -= amount
        self.accounts[receiver_id]["balance"] += amount

        self.accounts[sender_id]["transactions"].append(
            {"type": "transfer_out", "amount": amount}
        )
        self.accounts[receiver_id]["transactions"].append(
            {"type": "transfer_in", "amount": amount}
        )
        return "Transfer successful"

    def get_transactions(self, account_id):
        if account_id not in self.accounts:
            return "Account not found"
        return self.accounts[account_id]["transactions"]

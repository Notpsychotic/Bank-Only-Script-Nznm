import random
import time

class POS:
    def __init__(self, marketplace_name, bank_account):
        self.marketplace_name = marketplace_name
        self.bank_account = bank_account
        self.sales = []

    def process_sale(self, amount, payment_method):
        sale_id = random.randint(1000, 9999)
        sale = {
            'id': sale_id,
            'amount': amount,
            'payment_method': payment_method,
            'timestamp': time.time()
        }
        self.sales.append(sale)
        self.notify_sale(sale)
        self.deposit_to_bank(amount)

    def notify_sale(self, sale):
        print(f"Sale Notification: ID={sale['id']}, Amount=${sale['amount']}, Payment Method={sale['payment_method']}")

    def deposit_to_bank(self, amount):
        print(f"Depositing ${amount} to bank account {self.bank_account} via GPay")

if __name__ == '__main__':
    pos = POS(marketplace_name='Zettle', bank_account='notpsychotic@gmail.com')
    pos.process_sale(100, 'Venmo')
    pos.process_sale(200, 'Square')
    pos.process_sale(150, 'Zettle')

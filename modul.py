import pandas as pd
import random

class Transaction():
  '''
  Class Transaction berisi menu-menu untuk menjalankan
  sistem kasir pada Online Supermarket
  '''
  __current_id = []

  def __init__(self):
    self.item_name = list()
    self.item_qty = list()
    self.item_price = list()
    self.cart={}

#Membuat ID transaction
  def id_no(self):
    id_generator = random.randint(11,99)
    self.__current_id = id_generator
    print(f':::Welcome to Online Supermarket::: \n\nYour ID Transaction number is {id_generator} \n This 2-digit number will be added into the bill for unique code \n\n\
    1. To put items in shopping cart, use .add_item(<item name>, <item quantity>, <item price>)\n\
    2. To check whether the entries are correct, use .check_order()\n\
    3. To To delete items, use .delete_item()\n\
    4. To delete all items, use .reset_transaction()\n\
    5. To display the total bill, use .total_price() ')

#Menambahkan item pada shopping cart
  def add_item(self, nama, jumlah, harga):
      self.item_name.append(nama.lower())
      self.item_qty.append(jumlah)
      self.item_price.append(harga)
      for i in range(len(self.item_name)):
        self.cart[self.item_name[i]] = [self.item_qty[i], self.item_price[i]]
      print('Your order summary: \n', self.cart)

#Mengupdate nama item
  def update_item_name(self, current_name, new_name):
    if type(current_name) == str:
      for i, item in enumerate(self.item_name):
        if item == current_name.lower():
          self.item_name[i] = new_name.lower()
          print('Your change has been successfully updated.\nTo check your order, please use def check_order()')
    else:
      print("Enter new item's name in a string data-type")

#Untuk cek hasil sementara (UJICOBA)
  def order_summary(self):
    cart = dict()
    for i in range(len(self.item_name)):
      cart[self.item_name[i]] = [self.item_qty[i], self.item_price[i]]
    print('Your order summary: \n', cart)


#Menampilkan item apa saja yang ada pada shopping cart
  def check_order(self):
    for i in range(len(self.item_name)):
      if type(self.item_name[i]) != str or type(self.item_qty[i]) != int or type(self.item_price[i]) != int or self.item_price[i] < 1 or self.item_qty[i] <1:
        raise Exception('Warning: Errors in data entry - Please make sure you have input the data correctly. To see whats currently on your shopping cart, use .order_summary()')
    print('All data entries are correct')

    #Mencetak items pada shopping cart dalam tabel jika entry sudah sesuai
    total_tag=[]
    for i in range(len(self.item_name)):
      x = self.item_qty[i] * self.item_price[i]
      total_tag.append(x)

    list_order = {'Item': self.item_name, 'Item Quantity': self.item_qty, 'Price/Item': self.item_price, 'Total': total_tag}

    df = pd.DataFrame(list_order)
    df.index = df.index + 1
    return df

#Mengupdate item quantity pada shopping cart
  def update_item_qty(self, current_name, new_qty):
    if type(new_qty) == int:
      for i, item in enumerate(self.item_name):
        if item == current_name.lower():
          self.item_qty[i] = new_qty
          print('Your change has been successfully updated.\nTo check your order, please use def check_order()')
    else:
      print('Enter new quantity with positive integer')

#Mengupdate item price pada shopping cart
  def update_item_price(self, current_name, new_price):
    if type(new_price) == int:
      for i, item in enumerate(self.item_name):
        if item == current_name.lower():
          self.item_price[i] = new_price
          print('Your change has been successfully updated.\nTo check your order, please use def check_order()')
    else:
      print('Enter new price with positive integer')

#Menghapus certain item pada cart
  def delete_item(self, remove_key):
    for i, item in enumerate(self.item_name):
      if item == remove_key.lower:
        self.item_name.pop(i)
        self.item_qty.pop(i)
        self.item_price.pop(i)
        print(f'Item {item} has been removed from shopping cart')

#Menghapus semua item pada cart
  def reset_transaction(self):
    self.item_name.clear()
    self.item_qty.clear()
    self.item_price.clear()
    print('Your shopping cart is empty !')

#Perhitungan total belanja
  def total_price(self):
    try:
      total_bill = 0
      for i in range(len(self.item_name)):
        total_bill += self.item_price[i] * self.item_qty[i]
      if total_bill > 200000:
        total_bill = total_bill * 0.95 + self.__current_id
      elif total_bill > 300000:
        total_bill = total_bill * 0.92 + self.__current_id
      elif total_bill > 500000:
        total_bill = total_bill * 0.9 + self.__current_id
      else:
        total_bill = total_bill + self.__current_id
      print(f'Here is your total amount of payment: Rp {total_bill}')
    except (ValueError, TypeError):
      print('Errors in data entry - Please make sure you have input item data in the shopping cart correctly.')

from asyncore import read
#from bitcoinlib.wallets import Wallet, wallet_exists, db_update
#from bitcoinlib.db import Db


import data.listings as listings
import data.users as users


# DELETE ALL WALLETS! 
#Db.drop_db(Db(), yes_i_am_sure=True)


def InitiateTransaction(user_id, listing_id):
   listing_data = listings.getlisting(listing_id)
   user_data = users.getUser(user_id)
   total_price = listing_data["price"]

   if user_data["balance"] >= total_price:
      users.addBalance(user_id, -total_price)
      return listings.getProduct(listing_id)
   else:
      print("ERROR")


   #if not wallet_exists(user_id):
   #   w = Wallet.create(user_id)
   #   print(f"\nNew account created! {w}\n")

   

# INITIATE TRANSACTION
#InitiateTransaction("123", 1, 2)

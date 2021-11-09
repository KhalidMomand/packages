import json
import os.path

class Inventory:
    store = {}
    
    
    def __init__(self):
        self.load()
        
          
    def add(self, key, qty):
        if not key in self.store.keys():
            self.store[key] = qty
        else:
            current_stock = self.store[key]
            self.store[key] = qty + current_stock
            
    
    def remove(self,key, qty):
        if not key in self.store.keys():
            self.store[key] = 0
        else:
            current_stock = self.store[key]
            if current_stock > qty:
                self.store[key] = current_stock - qty
            else:
                print("Not Enough Stock to remove.")
                          
    
    def save(self):
        print('Saving Inventory....')
        with open('inventory.txt', 'w') as file:
            json.dump(self.store, file)
        print('Inventory Saved.')
    
    
    
    def display(self):
        for item, qty in self.store.items():
            print(f'{item} : {qty}')
    
            
    def load(self):
        print('Loading Inventory....')
        if os.path.exists('inventory.txt'):
            with open('inventory.txt', 'r') as file:
                self.store = json.load(file)
            print('Loaded Successfully.')
        else:
            print('Skkiping the loading.')
    
    
    def __str__(self):
        return "This is the simplest Inventory Application."
    



    
from Apps.inventory import Inventory

def main():
    inv = Inventory()
    
    while True:
        
        actions = input('Actions: add, remove, list, save, exit: ')
        
        if actions == "exit":
            break
    
        elif actions == 'add' or actions == 'remove':
            
            item = str(input('Enter Item name: '))
            qty = int(input('Enter Qty: '))
            
            if actions == 'add':
                inv.add(item, qty)
                
            elif actions == 'remove':
                inv.remove(item, qty)
            
        elif actions == 'save':
            inv.save()
            
        elif actions == 'list':
            inv.display()
            
    inv.save()

if __name__ == '__main__':
    main()
    
    
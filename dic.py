def update_inventory(inventory_dict, item, quantity):
    #for i in inventory_dict:
    if item not in inventory_dict:
        inventory_dict[item] = quantity
    else:
        inventory_dict[item] += quantity
    print(inventory_dict)

#{"apples":50,"bananas":30} apples 20
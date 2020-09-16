from consolemenu import *
from consolemenu.items import *
from consolemenu.screen import Screen
import sys



def main_menu(pj, mob, shop):
    selection_menu = SelectionMenu.get_selection(['Pelear', 'Personaje', 'Inventario', 'Tienda'], title="")
    if selection_menu == 0:
        player_combat_resolve = pj._physicalattack(mob)
        if not player_combat_resolve:
            gold_drop = mob.drop_gold(pj)
            Screen.println("{} monedas de oro fueron guardadas en tu billetera".format(gold_drop))
            item_drop_object = mob.drop_item()
            loot_menu_response = loot_menu(item_drop_object.name)
            if loot_menu_response == 0:
                pj.add_to_inventory(item_drop_object)
                return
        mob_combat_resolve = mob._physicalattack(pj)
        if not mob_combat_resolve:
            return False
    elif selection_menu == 1:
        Screen.println(pj)
    elif selection_menu == 2:
        inv = pj.show_inventory()
        inv_obj = [x for x in inv.values()]
        inv_name = [x for x in inv.keys()]
        try:
            inv_menu, index = inventory_menu(inv_obj, inv_name)
        except Exception as e:
            Screen.println("Tu inventario está vacío!")
            return
        if inv_menu == 0:
            pj.use_item(inv_obj[index])
        elif inv_menu == 1:
            pj.examine_item(inv_obj[index])
        elif inv_menu == 2:
            inv_obj[index].equip(pj)
        elif inv_menu == 3:
            inv_obj[index].unequip(pj)
    elif selection_menu == 3:
        shop_stock = shop.item_stock()
        shop_menu_opt, shop_index = shop_menu(shop_stock)
        if shop_menu_opt == 0:
            shop.buy(shop_stock[shop_index], pj)
        elif shop_menu_opt == 1:
            return
    elif selection_menu == 4:
        sys.exit("\nTu racha de victorias fue de {}!\n\nGracias por jugar! :)".format(pj.wins))
    return

def shop_menu(shop_stock):
    item_names = [x.name for x in shop_stock]
    item_values = [x.value for x in shop_stock]
    item_size = len(item_names)
    shop_size = len(shop_stock)
    for name, value in zip(item_names, item_values):
        Screen.println("{} -- {} monedas de oro".format(name, value))
    shop_menu_option = SelectionMenu.get_selection(item_names, title="Comprar items")
    for index_position in range(item_size):
        if shop_menu_option == index_position:
            shop_menu_action = SelectionMenu.get_selection(['Comprar {} por {} de oro'.format(item_names[index_position], item_values[index_position])], title="Confirmar compra")
            index = index_position
            break
    return (shop_menu_action, index)
    


def loot_menu(item):
    loot_item_menu = SelectionMenu.get_selection([item], title="Loot")
    loot_action_menu = SelectionMenu.get_selection(['Guardar {} en el inventario'.format(item), 'Descartar'], title="Confirmar acción")
    return loot_action_menu 
    
def inventory_menu(inv_obj, inv_name):
    inv_size = len(inv_name)
    if inv_size > 0:
        inventory_menu_option = SelectionMenu.get_selection(inv_name, title="Inventario")
        for index_position in range(inv_size):
            if inventory_menu_option == index_position:
                inventory_menu_action = SelectionMenu.get_selection(['Usar {}'.format(inv_name[index_position]), 'Examinar {}'.format(inv_name[index_position]), 'Equipar {}'.format(inv_name[index_position]), 'Desequipar {}'.format(inv_name[index_position])], title="Confirmar acción")
                index = index_position
                break
        return (inventory_menu_action, index)
    else:
        return None




    

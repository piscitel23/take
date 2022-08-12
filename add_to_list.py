import inquirer
global item_list 
item_list = []
def get_from_b(add):
    #add.get("name")
    add_to(add.get("name"))
    add_to(add.get("unit"))
    add_to(add.get("brew_type"))
    add_to(add.get("SW Version (UI)"))
    add_to(add.get("SW Version (PW)"))
    add_to(add.get("e_res"))
    add_to(add.get("f_res"))
    add_to(add.get("empty brew basket"))
    add_to(add.get("grounds"))
    add_to(add.get("pre water temp"))
    #print(item_list)

def get_from_d(add):
    item_list.append(add)
    #print(item_list)

def get_from_a(add):
    add_to(add.get("voltage"))
    add_to(add.get("post vessel weight"))
    add_to(add.get("post basket weight"))
    add_to(add.get("post res weight"))
    add_to(add.get("post temp"))
    add_to(add.get("TDS"))
    add_to(add.get("TDS2"))
    add_to(add.get("TDS3"))
    #print(item_list)
    return item_list

def add_to(item):
    item_list.append(item)
    
def eq(before, after):
    b = before.get("f_res")
    a = after.get("post res weight")
    c = float(b)-float(a)
    print(c)


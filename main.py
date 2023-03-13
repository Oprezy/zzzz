import json

all_transactions = []
with open("transactions.txt", mode="r") as file:
    line = file.readline()
    formatted = line.split("|")
    # print(formatted[1])
    counter = 0
    while line:
        line = file.readline()
        item = line.split("|")
        if len(item) == 5:
            the_amount = float(item[1].strip())
            the_balance = float(item[2])
            txn = {
                "id": int(counter),
                "amount": the_amount,
                "balance": the_balance,
                "time": item[3]
            }
            all_transactions.append(txn)
            counter += 1
            
valid = True
major_list = []
minor_list = []

minor_lock = []
major_lock = []

def check_txn(txn):
    global valid
    global minor_list
    global major_list
    amount = txn["amount"]
    if amount > 0:
        temp_list = []
        for i in minor_list:
            # print(i)
            temp_list.append(i)
        # major_list.append("NEW LOCK HERE")
        major_list.append(temp_list)
        # print("MINOR STOPS HERE")
        valid = False
        minor_list.clear()
    else:
        minor_list.append(txn)
        valid = True
   
   
def check_locks(txn):
    global valid
    amount = txn["amount"]
    if amount > 0:
        minor_lock.append(txn)
    else:
        valid = True
        
county = 0
for txn in all_transactions:
    if txn["id"] < 2454:
        if valid:
            county += 1
            check_txn(txn)
        else:
            county += 1
            check_locks(txn)
    else:
        # major_list.append("NOW FINISHED")
        print(county)
        

writtable = json.dumps(major_list)

with open("info.json", mode="w") as file:
    file.write(writtable)


# list storing errors
error_list = []
# function to check for inconsistency
def formula(head_list, child_id):
    # print(child_id)
    if child_id == 0:
        pass
        # print("Checking New lock... .")
    else:
        parent_against = head_list[child_id-2]
        against = head_list[child_id-1]
        current = head_list[child_id]
        against_amount = against["amount"]
        current_amount = current["amount"]
        current_balance = current["balance"]
        against_balance = against["balance"]
        key = against_balance+current_amount
        if child_id == len(head_list)-1:
            pass
        else:
            next = head_list[child_id+1]

        if round(key, 1) == round(current_balance, 1):
            # print(child_id, "passed")
            pass
        else:
            # print(child_id, "failed")
            # print(current)
            if parent_against["balance"] + current_amount == current_balance:
                print("caught")
            # preparing report...
            report = [parent_against, against, current, next]
            error_list.append(report)
    # print(error_list)

        # print(current)
        # print(against)
        # print(against_balance, current_amount, current_balance, key)

# manipulate data

for head_id in range(len(major_list)):
    head_list = major_list[head_id]
    for child_id in range(len(head_list)):
        # print(child_id)
        formula(head_list, child_id)
    # print("stop")

    
# # # process result
# for i in error_list:
#     for items in i:
#         print(items)
#     print("next...")
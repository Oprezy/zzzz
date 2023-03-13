all_transactions = []
with open("transactions.txt", mode="r") as file:
    line = file.readline()
    formatted = line.split("|")
    print(formatted[1])
    counter = 0
    while line:
        line = file.readline()
        item = line.split("|")
        if len(item) == 5:
            the_amount = item[1].strip()
            
            txn = {
                "id": int(counter),
                "amount": the_amount,
                "balance": item[2],
                "time": item[3]
            }
            all_transactions.append(txn)
            counter += 1
            
   
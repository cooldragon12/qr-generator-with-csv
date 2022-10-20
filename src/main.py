from queue import Queue
from time import sleep
from data_reader.readers import get_data_csv
from qr import qr_generator
from settings import OUTPUT_LOCATION, file_path
from log import printProgressBar



q = Queue()
q.maxsize = 100
# Enqueue the datas
def insert_data(data):
    for i in data:
        print(f"Enqueue: {i}")
        # sleep(.5)
        q.put(i)

def main():
    # Let's give a little message that the program is running
    print(
'''===========================================
=     WELCOME LET's MAkE YOUR QR          =
=                                         =
=       Created by: GE WebDue3s           =
==========================================='''
    )

    # After Getting the Raw data from a csv , More Specifically at email column
    # NOTE: This can be change
    data = get_data_csv(file_path=file_path, to_get="GE Email")

    # We will remove any extensions at the email, only to get the name
    # By using splitting
    data = data.str.split('.', expand=True)

    # then we will slect only the names which is index zero
    names = data[0].tolist()
    size_inqueue = len(names)
    # After that we will use Queue package to manage multiple requests
    insert_data(names)

    # Then we will start the queue of each name, which each name will added in the payload
    # Execute the request for each names.
    printProgressBar(0, q.unfinished_tasks, prefix = 'Progress:', suffix = 'Complete', length = 50)
    while True:
        if q.empty():
            return;
        data = q.get()
        
        printProgressBar( size_inqueue- q.qsize(), size_inqueue, prefix = 'Progress:', suffix = 'Complete - '+data, length = 50)
        # Generate the Qr Code
        generated = qr_generator(data="https://gulamanentertainment.com/link/"+data)
        
        generated.save(f'{OUTPUT_LOCATION}{data}.png')

        sleep(1)
        
    
    

if __name__ == "main":
    main()
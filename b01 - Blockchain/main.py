from blockchain import Blockchain
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("\n2020-05-28 15h43 - My First Blockchain by Gazstao\nStarting Blockchain at :", dt_string ,"\n")

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('SpaceApps 2020 - Special Edition')
    blockchain.add_new_block('Blockchain é muito massa.')
    blockchain.add_new_block('Temos mais chances que juízo!')

    print('');
    for i in blockchain.get_all():
        print(i)

    print('');

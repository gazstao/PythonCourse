from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('SpaceApps 2020')
    blockchain.add_new_block('by Gazstao')
    blockchain.add_new_block('Temos mais chances que juízo!')

    print(blockchain.get_all())

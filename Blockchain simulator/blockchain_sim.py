import hashlib
import time


class Blockchain:
    def __init__(self, nonce_difficulty: int):
        self.chain = []
        self.nonce_requirement = nonce_difficulty * "0"
    
    def add_blocks(self):
        print("\nType end to stop adding blocks, and print the blockchain.")

        add_tx = True
        transactions = []
        while(add_tx):
            txinput = input("Enter sender, recipient and value seperated by commas: ").split(",")
            if txinput[0].lower() == "end":
                add_tx = False
                print("\nHere is the complete blockchain:")
                for i in self.chain:
                    print(vars(i))
                
            else:
                transactions.append({"Sender":txinput[0], "Recipient":txinput[1], "Value":txinput[2]})
                userinput = input("Do you wish to add another transaction to this block? Y/N: ")
                if (userinput.lower() == "n"):
                    add_tx = False
                    self.calc_nonce(Block(blockchain = self, transactions = transactions))
                    self.add_blocks()
    
    def calc_nonce(self, block):
        while(not self.get_hash(block).startswith(self.nonce_requirement)):
            block.nonce = 0 if block.nonce == None else block.nonce +1

        block.hash = self.get_hash(block)
        self.chain.append(block)
        print("\nBlock added successfully!")
    
    def get_hash(self, block = None):
        if (block):
            encoded = str(vars(block)).encode()
        else:
            encoded = str(vars((self.chain[len(self.chain) -1]))).encode()
        print(encoded)
        result = hashlib.sha256(encoded)
        print ("result: ", result.hexdigest())
        return(result.hexdigest())



class Block:
    def __init__(self, blockchain: Blockchain, transactions: dict):
        self.transactions = transactions
        self.height = len(blockchain.chain)
        self.timestamp = time.asctime(time.localtime())
        self.hash = None
        self.nonce = None
        self.previous_hash = blockchain.chain[len(blockchain.chain)-1].hash if len(blockchain.chain) else "0000000000000000000000000000000000000000000000000000000000000000"


def main():
    difficulty = input("How many zeroes should the hash blocks start with? Enter an int or 'd' for default\n")
    #nonce_difficulty is the amount of zeroes required at the start
    my_blockchain = Blockchain(nonce_difficulty = 2 if difficulty == "d" else int(difficulty))
    my_blockchain.calc_nonce(Block(blockchain = my_blockchain, transactions = {"Sender":"Genesis", "Recipient":"System", "Value":"Hello blockchain"}))
    my_blockchain.add_blocks()


if (__name__ == "__main__"):
    main()




import hashlib
import datetime

class Block:

    def __init__(self,index,data,previous_hash):
        self.index=index
        self.timestamp=str(datetime.datetime.now())
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.create_hash()

    def create_hash(self):
        block_string=str(self.index)+self.timestamp+self.data+self.previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:

    def __init__(self):
        self.chain=[]
        self.create_genesis_block()

    def create_genesis_block(self):
        block=Block(0,"Genesis Block","0")
        self.chain.append(block)

    def add_block(self,data):
        prev_block=self.chain[-1]
        new_block=Block(len(self.chain),data,prev_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print("Index:",block.index)
            print("Data:",block.data)
            print("Hash:",block.hash)
            print("Previous Hash:",block.previous_hash)
            print("--------------------")
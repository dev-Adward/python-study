# Module 1 - Create a Blockchain

# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain:
    # 생성자 생성
    def __init__(self):
        # chain과 crate_block이 초기화 될때마다 바뀜
        self.chain = []
        # 초기화 될 때 마다 proof는 1로 previous_hash는 0으로 초기화
        self.create_block(proof = 1, previous_hash = '0')

    # 블럭 생성 코드 : proof와 previous_hash를 파라미터로 갖고있다.
    def create_block(self, proof, previous_hash):
        # block은 4개의 값을 json형식으로 갖는다.
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        # 이 함수가 호출 되면 chain에 block이 추가된다.
        self.chain.append(block)
        # block을 리턴함
        return block

    def get_previous_block(self):
        # chain에 있는 가장 마지막 블록을 가져온다.
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        # check_proof는 처음엔 false임으로 무조건 실행된다.
        while check_proof is False:
            # hash_operation이 hashlib안에 sha256이라는 함수를 실행하고, 알고리즘을 만든다. new_proof의 제곱 - previous_proof의 제곱을 뺸다. 그리고 그걸 문자열로 만듦
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # 앞자리가 '0000'일때 check_proof가 true가 되고 while문을 탈출한다. 앞자리가 0000인것을 찾는건 매우 힘든 작업이기 때문에 이런 알고리즘으로 짠듯하다
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        # encoded_block은 파라미터로 받아온 블럭을 json으로 만들어서 인코딩 한다.
        encoded_block = json.dumps(block, sort_keys = True).encode()
        # 그리고 다시 한번 sha256으로 바꾼다.
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        # 이전블록을 왜 0번째로 하는거지? -1이 되어야되는거아닌가?
        previous_block = chain[0]
        block_index = 1
        # block_index는 가장 처음에 1이다. 만약 체인에 여러개가 있다면 이 while문이 실행된다. 당연히 1개이상 있어야 비교가 되기 떄문에
        while block_index < len(chain):
            # block은 체인의 두번째 인덱스를 갖는다.
            block = chain[block_index]
            # 만약 블록의 'previous_hash'라는 키의 벨류가 이전 블록의 해쉬값과 다르다면 false를 리턴한다.
            if block['previous_hash'] != self.hash(previous_block):
                return False
            # previous_proof를 정의 하는데 previous block의 proof라는 키를 가진 밸류값으로 정의한다.
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            # 만약에 앞자리가 0000이 아니라면 false니까 이해가 된다
            # 그러니까 0000이 무조건 나와야하는데 0000이 안나오니까 false라고 하는거지
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            # 0000이 맞으면 하나가 늘어나는 거지
            block_index += 1
        return True

# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200

# Running the app
app.run(host = '0.0.0.0', port = 5000)

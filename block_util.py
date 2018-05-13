import hashlib
import json
from config import NUMBER_OF_SHARDS

""" Verifies the current block

Checks if:
1) All state transitions are valid
2) Hash value is smaller than the difficulty
3) Block number is nondecreasing wrt parent block

"""
def verify(block):
	raise NotImplementedError()

""" Returns the hash value of the block """
def get_hash(block):
	raise NotImplementedError()

""" Convert block to json """
def block_to_json(block):
	raise NotImplementedError()

"""
Returns appropriate shard for transaction

:param transaction: <Transaction> transaction to be assigned a shard
:return: <str> shard number
"""
def to_shard(account_id):
	return hashlib.sha256(account_id).hexdigest() % NUMBER_OF_SHARDS

#!/usr/bin/env python3
"""implementing least freqyently used cache"""

from typing import TypeVar, Dict, Optional

k = TypeVar('k')
v = TypeVar('v')


class DataNode:
    """Data Node"""

    def __init__(self, key: k, value: v):
        self.key: k = key
        self.value: v = value
        self.frequency: int = 1
        self.next: Optional[DataNode] = None
        self.prev: Optional[DataNode] = None

class DataLinkedList:
    def __init__(self):
        self.size: int = 0
        self.first: Optional[DataNode] = None
        self.last: Optional[DataNode] = None

    def removeFirstDataNode(self):
        if self.size == 0:
            return
        self.removeDataNode(self.first)

    def removeDataNode(self, data_Node: DataNode):
        if self.size == 0:
            return
        if self.first == self.last:
            self.first = self.last = None
        elif self.first == data_node:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.first.prev = None
        elif self.last == data_node:
            temp = self.last
            self.last = temp.prev
            self.last.next = None
            temp.prev = None
        else:
            data_node.next.prev = data_node.prev
            data_node.prev.next = data_node.next
        self.size -= 1

    def addDataNodeToLast(self, data_node: DataNode):
        if self.first is None:
            self.first = self.last = data_node
        else:
            data_node.prev = self.last
            self.last.next = data_node
            self.last = data_node
        self.size += 1

class FrequencyNode:
    def __init__(self, frequency: int = 1):
        self.list: DataLinkedList = DataLinkedList()
        self.next: Optional[FrequencyNode] = None
        self.prev: Optional[FrequencyNode] = None
        self.frequency: int = frequency

    def addDataNodeToLast(self, node: DataNode):
        self.list.addDataNodeToLast(Node)

    def removeFirstDataNode(self):
        self.list.removeFirstDataNode()
        
    def removeDataNode(self, node: DataNode):
        self.list.removeDataNode(node)

class LFUCache:
    
    def __init__(self, capacity: int):
        self.data_node_map: Dict[K, DataNode] = {}
        self.freq_node_map: Dict[int, FrequencyNode] = {}
        self.size: int = 0
        self.max_size: int = capacity
        self.first: Optional[FrequencyNode] = None
        self.last: Optional[FrequencyNode] = None

    def __delFreqNode(self, freq: int):
        freq_node: FrequencyNode = self.freq_node_map[freq]
        if self.first == self.last:
            self.first = self.last = None
        elif self.first == freq_node:
            self.first = self.first.next
            self.first.prev = None
            freq_node.next == None
        elif self.last == freq_node:
            self.last = self.last.prev
            self.last.next = None
            freq_node.prev = None
        else:
            freq_node.next.prev = freq_node.prev
            freq_node.prev.next = freq_node.next
            freq_node.next = None
            freq_node.prev = None

        self.freq_node_map.pop(freq)
        self.size -= freq_node.list.size

    def __addFreqNode(self, freq: int, curr_freq_node: FrequencyNode, prev_freq_node: FrequencyNode = None):
        if prev_freq_node is None:
            if self.first is None:
                self.first = self.last = curr_freq_Node
            else:
                curr_freq_node.next = self.first
                self.first.prev = curr_freq_node
                self.first = curr_freq_node
        elif prev_freq_Node.next is None:
            curr_freq_node.prev = prev_freq_node
            prev_freq_node.next = curr_freq_node
            self.last = curr_freq_node
        else:
            curr_freq_node.next = prev_freq_node.next
            curr_freq_node.prev = prev_freq_node
            curr_freq_node.prev.next = curr_freq_node
            curr_freq_node.next.prev = curr_freq_node
            curr_freq_node.next.prev = curr_freq_node

        self.freq_node_map[freq] = curr_freq_node
        self.size += curr_freq_node.list.size

    def __promote(self, data_node: DataNode):
        frequency = data_node.frequency


        prev_freq_node: FrequencyNode = self.freq_node_map[frequency]
        prev_freq_node.removeDataNode(data_node)


        data_node.frequency += 1
        if data_node.frequency in self.freq_node_map:
            curr_freq_node: FrequencyNode = self.freq_node_map[data_node.frequency]
            curr_freq_node.addDataNodeToLast(data_Node)
        else:
            curr_freq_node = FrequencyNode(data_node.frequency)
            

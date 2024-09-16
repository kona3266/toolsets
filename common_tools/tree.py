#!/usr/bin/env python
from __future__ import print_function
class Tree(object):
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    @classmethod
    def tree_maker(cls, depth=1):
        num = 2 ** depth - 1
        values = []
        for i in range(num):
            values.append(i)
        # format binanry search tree: left < root < right
        return cls.tree_former(values)

    @classmethod
    def tree_former(cls, values):
        length = len(values)
        middle_value = values[length // 2]
        if len(values) > 1:
            left = cls.tree_former(values[: length // 2])
            right = cls.tree_former(values[length//2 + 1:])
            return cls(middle_value, left, right)
        else:
            return cls(middle_value)
    
    def __str__(self):
        self.print_tree(self)
        return ''

    @staticmethod
    def print_tree(tree):
        childs = [tree]
        rows = []
        depth = -1

        while childs:
            depth += 1
            values = []
            for c in childs[:]:
                values.append(c.root)
                childs.remove(c)

                if c.left is not None:
                    childs.append(c.left)
                if c.right is not None:
                    childs.append(c.right)

            rows.append(values)

        for j, r in enumerate(rows):
            width = 2**(depth - j + 1)
            for i, v in enumerate(r):
                ch_len = len(str(v))
                print((width-ch_len)*' ' + str(v) + width*' ', end='')
            print('')

    @staticmethod
    def get_childs(t):
        childs = []
        if t.left is not None:
            childs.append(t.left)
        if t.right is not None:
            childs.append(t.right)
        return childs

    def preorder(self):
        '''root -> left -> right'''
        stack = []
        result = []
        cur = self
        while(cur or stack):
            while cur:
                result.append(cur.root)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return result

    def postorder(self):
        '''left-right-root'''
        stack = []
        result = []
        cur = self
        prev = None
        
        while (stack or cur):
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not cur.right:
                result.append(cur.root)
                prev = cur
                cur = None
            elif cur.right == prev:
                result.append(cur.root)
                prev = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right

        return result

    def postorder_recursive(self):
        result = []
        if self.left:
            result += self.left.postorder_recursive()
        if self.right:
            result += self.right.postorder_recursive()
        result.append(self.root)
        return result
    
    def preorder_recursive(self):
        result = []
        result.append(self.root)
        if self.left:
            result += self.left.preorder_recursive()
        if self.right:
            result += self.right.preorder_recursive()
        return result
    
    def inorder_recursive(self):
        result = []
        if self.left:
            result += self.left.inorder_recursive()
        result.append(self.root)
        if self.right:
            result += self.right.inorder_recursive()
        return result

    def inorder(self):
        '''left-root-right'''
        stack = []
        result = []
        cur = self
        while (stack or cur):
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.root)
            cur = cur.right
        return result


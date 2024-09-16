#!/usr/bin/env python

from __future__ import print_function
from common_tools.tree import Tree
from optparse import OptionParser
import sys

def cmd_runner():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-d", action="store", dest="depth", default=None, type="int", help="tree depth")
    parser.add_option("-m", "--method", action="store", dest="method", default="",
                      help="visit method: recursive")
    parser.add_option("-t", "--treversal", action="store", dest="traversal", default="preorder",
                      help="visit each node of the tree in a certain order ")
 
    (options, args) = parser.parse_args()
    depth = options.depth
    if depth is None:
        parser.error("need specify the depth of tree")
    if depth >= 6:
        parser.error("max depth is 5")
    method = options.method
    if method and method != "recursive":
        parser.error("invalid visit method, use recursive or ''")
    traversal = options.traversal
    if traversal not in ["preorder", "inorder", "postorder"]:
        parser.error("invalid traversal order")
    tree = Tree.tree_maker(depth)
    print(tree)
    func_name = '%s' % traversal
    if method:
        func_name += '_' + method
    print("call %s" % func_name)
    print(getattr(tree, func_name)())


if __name__ == "__main__":
    cmd_runner()

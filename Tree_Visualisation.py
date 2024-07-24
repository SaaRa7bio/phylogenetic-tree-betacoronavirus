from ete3 import Tree, TreeStyle, NodeStyle


tree = Tree("consensus_tree.nwk")


ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_support = True
ts.show_branch_length = True



nstyle = NodeStyle()
nstyle["fgcolor"] = "brown"
nstyle["bgcolor"] = "lightblue"
nstyle["size"] = 10


for node in tree.traverse():
    node.set_style(nstyle)

tree.render("tree.png", tree_style=ts)




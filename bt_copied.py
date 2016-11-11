class Bt():
    """
    Binary tree operations
    """
    obj_tree = None
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def set_tree(self):
        Bt.obj_tree = self

    @classmethod
    def get_tree(cls):
        return cls.obj_tree

    def insert_on_left(self, value):
        self.left = Bt(value)

    def insert_on_right(self, value):
        self.right = Bt(value)

    def insert(self, value):
        if int(value) > int(self.value):
            # goto right
            if self.right == None:
                print "insert(%d) as right child of parent(%d)" %(
                    value, self.value)
                self.insert_on_right(value)
            else:
                self.right.insert(value)
        else:
            # goto left
            if self.left == None:
                print "insert(%d) as left child of parent(%d)" %(
                    value, self.value)
                self.insert_on_left(value)
            else:
                self.left.insert(value)

    def in_order_travesal(self):
        if self.value is not None:
            if self.left is not None:
                self.left.in_order_travesal()
            print self.value,
            if self.right is not None:
                self.right.in_order_travesal()

    def pre_order_travesal(self):
        if self.value is not None:
            print self.value,
            if self.left is not None:
                self.left.pre_order_travesal()
            if self.right is not None:
                self.right.pre_order_travesal()

    def view_tree(self, spec=1, rl = 'l'):
        print '-' * spec, rl, self.value
        if self.left == None and self.right == None:
            spec = 1
        else:
            spec = spec + 1

        if self.left is not None:
            self.left.view_tree(spec, rl = 'l')
        if self.right is not None:
            self.right.view_tree(spec, rl = 'r')

def init():
    node = raw_input('Initialize Root (Q to quit): > ')
    if node.isdigit() is not True :
        show_menu()

    obj_bt = Bt(int(node))
    obj_bt.set_tree()
    print "-"*10,'Now Insert nodes to tree.',"-"*10
    show_menu()

def check_for_tree():
    obj_bt = Bt.get_tree()
    if obj_bt == None:
        print "-"*10, "you need to initialize the tree first with root.","-"*10
        show_menu()
    return obj_bt

def tree_insertion():
    obj_bt = check_for_tree()

    while (True):
        node = raw_input('Initialize Node (Q to quit): > ')
        if node.isdigit() is not True :
            break
        obj_bt.insert(int(node))

    show_menu()

def tree_view():
    obj_bt = check_for_tree()
    # obj_bt = Bt.get_tree()
    obj_bt.view_tree(rl='R')

    show_menu()

def in_order_traveral_view():
    # obj_bt = Bt.get_tree()
    obj_bt = check_for_tree()
    obj_bt.in_order_travesal()
    print ''
    show_menu()

def pre_order_traveral_view():
    # obj_bt = Bt.get_tree()
    obj_bt = check_for_tree()
    obj_bt.pre_order_travesal()
    print ''
    show_menu()

def show_menu():
    print ''
    print "0. Initialize Tree"
    print "1. Insert to Tree"
    print "2. View Tree"
    print "3. In Order Travesal"
    print "4. Pre Order Travesal"
    print "5. For exit."
    option = raw_input("Enter option :")

    options = {0 : init,
               1 : tree_insertion,
               2 : tree_view,
               3 : in_order_traveral_view,
               4 : pre_order_traveral_view,
               }

    if option.isdigit() is not True or not(int(option) in options.keys()): #conditio pending
        print "Good Bye!!"
        exit(0)

    options[int(option)]()

# lets start
show_menu()

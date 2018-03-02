from Linked_List import LinkedList

LL1 = LinkedList(93)
LL2 = LinkedList(94, LL1)

print LL2.getChild().getData()
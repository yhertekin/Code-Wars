"""
Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.

Here's a simple Ruby example:

animals = ["cat", "dog", "duck", "cow", "donkey"]
partition(animals){|animal| animal.size == 3}
    #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
The equivalent in Python would be:

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
If you need help, here's a reference:

http://www.rubycuts.com/enum-partition
"""
def partition(arr, classifier_method):
    l1 = list()
    l2 = list()
    for item in arr:
        if classifier_method(item):
            l1.append(item)
        else:
            l2.append(item)
    return (l1, l2)
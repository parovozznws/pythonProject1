class IceCream:
    def __init__(self, name, sweet):
        self.name = name
        self.sweet = sweet

    @staticmethod
    def sweetest_icecream(IceCreams ):

        sweetests = {'Plain' : 0,
                     'Vanilla' : 5,
                     'ChocolateChip' : 5,
                     'Strawberry' : 10,
                     'Chocolate' : 10
                     }
        return max([x.sweet + sweetests[x.name] for x in IceCreams])


ice1 = IceCream("Chocolate", 13) # 10 + 13 = 23
ice2 = IceCream("Vanilla", 0) # 5 + 0 = 5
ice3 = IceCream("Strawberry", 7) # 10 + 7 = 17
ice4 = IceCream("Plain", 18) # 0 + 18 = 18
ice5 = IceCream("ChocolateChip", 3) # 5 + 3 = 8

print(IceCream.sweetest_icecream([ice2, ice3, ice4, ice5]))









# class Biryani:
#     def _init_(self,smell,taste,texture,meatcontent,color):
#         self.smell = smell,
#         self.taste = taste,
#         self.texture = texture,
#         self.meatcontent = meatcontent,
#         self.color = color,

           
# Hydarabadi = Biryani ("oniony","spicy","smooth",True,"red")
# Donne=Biryani("podhina","modarate","rough",True,"green")
# Avadhi=Biryani("haldhi/oniony","low-spice","sticky",False,"brown")

# print(Hydarabadi.taste)
# class Biryani:
#     def __init__(self, smell, taste, texture, meatcontent, color):
#         self.smell = smell
#         self.taste = taste
#         self.texture = texture
#         self.meatcontent = meatcontent
#         self.color = color

# Hyderabadi = Biryani("oniony", "spicy", "smooth", True, ["red", "brown", "white", "yellow"])
# Donne = Biryani("podhina", "moderate", "rough", True, "green")
# Awadhi = Biryani("haldi/oniony", "low-spice", "sticky", False, ["white", "brown"])

# # Access and print the taste attribute for each Biryani type
# print("Hyderabadi Biryani taste:", Hyderabadi.taste)
# print("Donne Biryani taste:", Donne.taste)
# print("Awadhi Biryani taste:", Awadhi.taste)
class Biryani:
    def __init__(self, smell, taste, texture, meatcontent, color):
        self.smell = smell
        self.taste = taste
        self.texture = texture
        self.meatcontent = meatcontent
        self.color = color
# Hydarabadi = Biryani('oniony','spicy','smooth',True,'red-brown-white-yellow')
# Donne = Biryani('podhina','modarate','rough',True,'green')
Avadhi = Biryani('haldhi/oniony','low-spice','sticky',False,'white-brown')

print(Avadhi.taste)
 
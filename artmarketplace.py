import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

class Art:
  def __init__(self,artist,title,medium,year,owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{artist}. \"{title}\". {year}, {medium}. {owner}, {location}.".format(artist=self.artist,title=self.title,medium=self.medium,year=self.year,owner=self.owner.name,location=self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self,new_listing):
    self.listings.append(new_listing)
  def remove_listing(self,listing):
    self.listings.remove(listing)
  def show_listings(self):
    for listing in self.listings:
      print("\"{title}\", ${price}, {name}.".format(title=listing[0],price=locale.format("%d", listing[1], grouping=True),name=listing[2]))

class Client():
  def __init__(self,name,location,is_museum,wallet):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    self.wallet = wallet
  def sell_artwork(self,artwork,price):
    if artwork.owner.name == self.name:
      veneer.add_listing([artwork.title,price,artwork.owner.name])
  def buy_artwork(self,artwork):
    if artwork.owner.name != self.name:
      for art in veneer.listings:
        if art[0] == artwork.title:
          if self.wallet >= art[1]:
            self.wallet -= art[1]
            artwork.owner.wallet += art[1]
            print("You have successfully purchased \"{title}\" from {name} for ${price}.".format(title=art[0],name=artwork.owner.name,price=locale.format("%d", art[1], grouping=True)))
            artwork.owner = self
            veneer.remove_listing(art)
          else:
            print("You have insufficient funds for this purchase!")
  def money(self):
    print("$"+locale.format("%d", self.wallet, grouping=True))
          
class Listing():
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{art}. {price}.".format(art=self.art,price=self.price)
  
veneer = Marketplace()

edytta = Client("Edytta Halpirt", "Private Collection",False,23)

moma = Client("THE MOMA", "New York", True,7000000)
  
girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)","oil on canvas",1910,edytta)
print(girl_with_mandolin)

veneer.show_listings()
edytta.sell_artwork(girl_with_mandolin,6000000)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
edytta.money()
moma.money()
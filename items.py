from scrapy.item import Item, Field

class Web(Item):
    campurl = Field()
    campname = Field()
    campcontactfirstname = Field()
    campcontactlastname = Field()
    campemail = Field()

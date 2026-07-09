# -*- coding: utf-8 -*-
from enum import StrEnum
from abc import ABC, abstractmethod

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.cap_quality()
            item.update_quality()
            item.update_sellin()

class Item(ABC):

    MAX_QUALITY = 50
    MIN_QUALITY = 0

    QUALITY_UNITS = {
        "REGULAR": 1,
        "CONJURED": 2,
        "AGED_BRIE": 1,
        "BACKSTAGE_FIRST_BATCH": 1,
        "BACKSTAGE_SECOND_BATCH": 2,
        "BACKSTAGE_THIRD_BATCH": 3
    }

    def __new__(cls, name, sell_in, quality):
        if name == ItemNames.AGED_BRIE:
            return super().__new__(AgedBrieItem)
        elif name == ItemNames.BACKSTAGE_PASSES:
            return super().__new__(BackstagePassItem)
        elif name == ItemNames.SULFURAS:
            return super().__new__(SulfurasItem)
        elif name == ItemNames.CONJURED:
            return super().__new__(ConjuredItem)
        else:
            return super().__new__(RegularItem)
        
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def cap_quality(self):
        if self.quality > self.MAX_QUALITY:
            self.quality = self.MAX_QUALITY
        elif self.quality < self.MIN_QUALITY:
            self.quality = self.MIN_QUALITY
    
    @abstractmethod
    def update_quality(self):
        pass

    @abstractmethod
    def update_sellin(self):
        pass

class RegularItem(Item):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= self.QUALITY_UNITS["REGULAR"]
        else:
            self.quality -= 2 * self.QUALITY_UNITS["REGULAR"]
        Item.cap_quality(self)
    
    def update_sellin(self):
        self.sell_in -= 1

class AgedBrieItem(Item):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality += self.QUALITY_UNITS["AGED_BRIE"]
        elif self.sell_in <= 0:
            self.quality += 2 * self.QUALITY_UNITS["AGED_BRIE"]
        Item.cap_quality(self)

    def update_sellin(self):
        self.sell_in -= 1

class BackstagePassItem(Item):
    FIRST_BATCH = 10
    SECOND_BATCH = 5

    def update_quality(self):
        if self.sell_in > 0:
            if self.sell_in > self.FIRST_BATCH:
                self.quality += self.QUALITY_UNITS["BACKSTAGE_FIRST_BATCH"]
            elif self.SECOND_BATCH < self.sell_in <= self.FIRST_BATCH:
                self.quality += self.QUALITY_UNITS["BACKSTAGE_SECOND_BATCH"]
            elif self.sell_in <= self.SECOND_BATCH:
                self.quality += self.QUALITY_UNITS["BACKSTAGE_THIRD_BATCH"]
        else:
            self.quality = 0
        Item.cap_quality(self)

    def update_sellin(self):
        self.sell_in -= 1

class ConjuredItem(Item):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= self.QUALITY_UNITS["CONJURED"]
        else:
            self.quality -= 2 * self.QUALITY_UNITS["CONJURED"]
        Item.cap_quality(self)
    
    def update_sellin(self):
        self.sell_in -= 1

class SulfurasItem(Item):
    def update_quality(self):
        return super().update_quality()
    
    def update_sellin(self):
        return super().update_sellin()

class ItemNames(StrEnum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED = "Conjured"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

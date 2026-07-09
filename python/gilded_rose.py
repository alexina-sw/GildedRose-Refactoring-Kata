# -*- coding: utf-8 -*-

class GildedRose(object):

    ITEM_MAX_QUALITY = 50
    ITEM_MIN_QUALITY = 0
    aged_brie = "Aged Brie"
    backstage_passes = "Backstage passes to a TAFKAL80ETC concert"
    conjured = "Conjured"
    sulfuras = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items
        for item in items:
            self.__cap_quality(item)

    def __cap_quality(self, item):
        if item.quality > self.ITEM_MAX_QUALITY:
            item.quality = self.ITEM_MAX_QUALITY
        elif item.quality < self.ITEM_MIN_QUALITY:
            item.quality = self.ITEM_MIN_QUALITY
    
    @staticmethod
    def __update_quality_regular(item):
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2
        
    @staticmethod
    def __update_quality_aged_brie(item):
        if item.sell_in > 0:
            item.quality += 1
        elif item.sell_in <= 0:
            item.quality += 2
    
    @staticmethod
    def __update_quality_backstage_passes(item):
        if item.sell_in > 0:
            if item.sell_in > 10:
                item.quality += 1
            elif item.sell_in <= 10 and item.sell_in > 5:
                item.quality += 2
            elif item.sell_in <= 5:
                item.quality += 3
        else:
            item.quality = 0

    @staticmethod
    def __update_quality_conjured(item):
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4

    def update_quality(self):
        for item in self.items:

            if item.name == self.sulfuras:
                continue
            elif item.name == self.aged_brie:
                self.__update_quality_aged_brie(item)
            elif item.name == self.backstage_passes:
                self.__update_quality_backstage_passes(item)
            elif item.name == self.conjured:
                self.__update_quality_conjured(item)
            else:
                self.__update_quality_regular(item)
            
            self.__cap_quality(item)

            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

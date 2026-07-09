# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    
    def test_regular_item_quality_decreases_before_sellin(self):
        items = [Item("regular", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_regular_item_quality_decreases_by_two_after_sellin(self):
        items = [Item("regular", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_regular_item_quality_zero_remains_zero_before_sellin(self):
        items = [Item("regular", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_regular_item_quality_zero_remains_zero_after_sellin(self):
        items = [Item("regular", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_quality_is_capped_at_0_before_sellin(self):
        items = [Item("regular", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_quality_is_capped_at_0_after_sellin(self):
        items = [Item("regular", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_bie_quality_increases_before_sellin(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_quality_increases_by_two_after_sellin(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)
    
    def test_quality_is_capped_at_50_before_sellin(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_quality_is_capped_at_50_after_sellin(self):
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_sulfuras_quality_and_sellin_remain_the_same(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_backstage_more_then_ten_days_to_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_backstage_less_then_ten_days_and_more_then_five_to_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_less_then_five_days_to_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(3, items[0].quality)
    
    def test_backstage_after_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 13)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_show_item_name_sellin_quality_as_string(self):
        item = Item("Aged Brie", 10, 20)
        result = repr(item)
        self.assertEqual("Aged Brie, 10, 20", result)
        
if __name__ == '__main__':
    unittest.main()

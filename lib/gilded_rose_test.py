import unittest

from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
  # Normal Item
  def test_normal_item_before_sell_date(self):
    gilded_rose = GildedRose(name = 'Normal Item', days_remaining = 5, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Normal Item', 'days_remaining': 4, 'quality': 9})

  def test_normal_item_on_sell_date(self):
    gilded_rose = GildedRose(name = 'Normal Item', days_remaining = 0, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Normal Item', 'days_remaining': -1, 'quality': 8})

  def test_normal_item_after_sell_date(self):
    gilded_rose = GildedRose(name = 'Normal Item', days_remaining = -10, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Normal Item', 'days_remaining': -11, 'quality': 8})

  def test_normal_item_of_zero_quality(self):
    gilded_rose = GildedRose(name = 'Normal Item', days_remaining = 5, quality = 0)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Normal Item', 'days_remaining': 4, 'quality': 0})

  # Aged Brie
  def test_aged_brie_before_sell_date(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = 5, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': 4, 'quality': 11})

  def test_aged_brie_with_max_quality(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = 5, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': 4, 'quality': 50})

  def test_aged_brie_on_sell_date(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = 0, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': -1, 'quality': 12})

  def test_aged_brie_on_sell_date_near_max_quality(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = 0, quality = 49)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': -1, 'quality': 50})

  def test_aged_brie_on_sell_date_with_max_quality(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = 0, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': -1, 'quality': 50})

  def test_aged_brie_after_sell_date(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = -10, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': -11, 'quality': 12})

  def test_aged_brie_after_sell_date_with_max_quality(self):
    gilded_rose = GildedRose(name = 'Aged Brie', days_remaining = -10, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Aged Brie', 'days_remaining': -11, 'quality': 50})

  # Sulfuras
  def test_sulfuras_before_sell_date(self):
    gilded_rose = GildedRose(name = 'Legendary Sulfuras, Hand of Ragnaros', days_remaining = 5, quality = 80)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Legendary Sulfuras, Hand of Ragnaros', 'days_remaining': 5, 'quality': 80}
    )

  def test_sulfuras_on_sell_date(self):
    gilded_rose = GildedRose(name = 'Legendary Sulfuras, Hand of Ragnaros', days_remaining = 0, quality = 80)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Legendary Sulfuras, Hand of Ragnaros', 'days_remaining': 0, 'quality': 80}
    )

  def test_sulfuras_after_sell_date(self):
    gilded_rose = GildedRose(name = 'Legendary Sulfuras, Hand of Ragnaros', days_remaining = -10, quality = 80)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Legendary Sulfuras, Hand of Ragnaros', 'days_remaining': -10, 'quality': 80}
    )

  # Backstage Pass
  def test_backstage_pass_long_before_sell_date(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 11, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 10, 'quality': 11}
    )

  def test_backstage_pass_long_before_sell_date_at_max_quality(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 11, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 10, 'quality': 50}
    )

  def test_backstage_pass_medium_close_to_sell_date_upper_bound(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 10, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 9, 'quality': 12}
    )

  def test_backstage_pass_medium_close_to_sell_date_upper_bound_at_max_quality(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 10, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 9, 'quality': 50}
    )

  def test_backstage_pass_medium_close_to_sell_date_lower_bound(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 6, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 5, 'quality': 12}
    )

  def test_backstage_pass_medium_close_to_sell_date_lower_bound_at_max_quality(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 6, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 5, 'quality': 50}
    )

  def test_backstage_pass_very_close_to_sell_date_upper_bound_at_max_quality(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 5, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 4, 'quality': 50}
    )

  def test_backstage_pass_very_close_to_sell_date_upper_bound_at_max_quality(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 5, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 4, 'quality': 50}
    )

  def test_backstage_pass_very_close_to_sell_date_lower_bound(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 1, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 0, 'quality': 13}
    )

  def test_backstage_pass_very_close_to_sell_date_lower_bound_at_max_quality(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 1, quality = 50)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': 0, 'quality': 50}
    )

  def test_backstage_pass_on_sell_date(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = 0, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': -1, 'quality': 0}
    )

  def test_backstage_pass_after_sell_date(self):
    gilded_rose = GildedRose(name = 'Backstage passes to a TAFKAL80ETC concert', days_remaining = -10, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(),
      {'name': 'Backstage passes to a TAFKAL80ETC concert', 'days_remaining': -11, 'quality': 0}
    )

  # Conjured Mana

  @unittest.skip('functionality not implemented')
  def test_conjured_manage_before_sell_date(self):
    gilded_rose = GildedRose(name = 'Conjured Mana Cake', days_remaining = 5, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Conjured Mana Cake', 'days_remaining': 4, 'quality': 8})

  @unittest.skip('functionality not implemented')
  def test_conjured_manage_before_sell_date_at_zero_quality(self):
    gilded_rose = GildedRose(name = 'Conjured Mana Cake', days_remaining = 5, quality = 0)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Conjured Mana Cake', 'days_remaining': 4, 'quality': 0})

  @unittest.skip('functionality not implemented')
  def test_conjured_manage_on_sell_date(self):
    gilded_rose = GildedRose(name = 'Conjured Mana Cake', days_remaining = 0, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Conjured Mana Cake', 'days_remaining': -1, 'quality': 6})

  @unittest.skip('functionality not implemented')
  def test_conjured_manage_on_sell_date_at_zero_quality(self):
    gilded_rose = GildedRose(name = 'Conjured Mana Cake', days_remaining = 0, quality = 0)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Conjured Mana Cake', 'days_remaining': -1, 'quality': 0})

  @unittest.skip('functionality not implemented')
  def test_conjured_manage_after_sell_date(self):
    gilded_rose = GildedRose(name = 'Conjured Mana Cake', days_remaining = -10, quality = 10)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Conjured Mana Cake', 'days_remaining': -11, 'quality': 6})

  @unittest.skip('functionality not implemented')
  def test_conjured_manage_after_sell_date_at_zero_quality(self):
    gilded_rose = GildedRose(name = 'Conjured Mana Cake', days_remaining = -10, quality = 0)

    gilded_rose.tick()

    self.assertEquals(gilded_rose.inspect(), {'name': 'Conjured Mana Cake', 'days_remaining': -11, 'quality': 0})


if __name__ == '__main__':
    unittest.main()
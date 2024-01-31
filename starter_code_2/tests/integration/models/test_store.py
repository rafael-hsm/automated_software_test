from models.store import StoreModel
from models.item import ItemModel

from tests.integration.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_item_empty(self):
        store = StoreModel('test')
        
        self.assertListEqual(store.items, [],
                            "The store's items length was not 0 even though no items were added.")
        
    def test_crud(self):
        with self.app_context:
            store =StoreModel('test')
            
            self.assertIsNone(StoreModel.find_by_name('test'))
            
            store.save_to_db()
            
            self.assertIsNotNone(StoreModel.find_by_name('test'))
            
            store.delete_from_db()
            
            self.assertIsNone(StoreModel.find_by_name('test'))
    
    def test_store_relationship(self):
        with self.app_context:
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            self.assertEqual(len(store.items), 1)
            self.assertEqual(store.items[0].name, 'test_item')
            
    def test_store_json_with_item(self):
        with self.app_context:
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            expected = {
                'name': 'test',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }
            
            self.assertDictEqual(store.json(), expected)
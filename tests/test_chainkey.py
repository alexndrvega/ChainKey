# /tests/test_chainkey.py

import unittest
from src.chainkey.encryption import data_encryptor, data_decryptor
from src.chainkey.utils import data_segmentation, data_restored

class TestChainKey(unittest.TestCase):
    def test_encrypt_decrypt(self):
        # data provided by https://satoristudio.net/delorean-ipsum/
        data = "Alright, McFly, you're asking for it, and now you're gonna get it. Let me show you my plan for sending you home. Please excuse the crudity of this model, I didn't have time to build it to scale or to paint it. I got enough practical jokes for one evening. Good night, future boy. What's with the life preserver? What, what, ma?"
        # password provided by random pass generator.
        password = "ec?Jy78mbDztbAEeC6$X"

        encrypt_dat = data_encryptor(data, password)
        decrypt_dat = data_decryptor(encrypt_dat, password)

        self.assertEqual(data, decrypt_dat)

    def test_segmentation(self):
        # data provided by http://www.catipsum.com/
        data = "Cough enslave the hooman yet climb into cupboard and lick the salt off rice cakes. Always hungry this human feeds me, i should be a god, murder hooman toes show belly sleep in the bathroom sink refuse to drink water except out of someone's glass love. Scratch so owner bleeds cats secretly make all the worlds muffins all of a sudden cat goes crazy climb leg, for trip on catnip or missing until dinner time. I could pee on this if i had the energy mewl for food at 4am always ensure to lay down in such a manner that tail can lightly brush human's nose but grab pompom in mouth and put in water dish or ooh, are those your $250 dollar sandals? lemme use that as my litter box nyan nyan goes the cat."
        num_chunks = 9

        segmented_data, chunk_order = data_segmentation(data, num_chunks)
        restored_data = data_restored
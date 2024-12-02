# File: nostr/utils/key_manager.py

import os
import base64
import nacl.signing
import nacl.encoding
from lib.logger import Logger

logger = Logger("KeyManager")


class KeyManager:
    def __init__(self, key_file="nostr_keys.json"):
        self.key_file = key_file
        self.private_key = None
        self.public_key = None
        self.load_or_generate_keys()

    def load_or_generate_keys(self):
        """
        Load keys from a file or generate new ones if none exist.
        """
        if os.path.exists(self.key_file):
            self.load_keys()
        else:
            self.generate_keys()

    def generate_keys(self):
        """
        Generate a new key pair.
        """
        key = nacl.signing.SigningKey.generate()
        self.private_key = key.encode(encoder=nacl.encoding.HexEncoder).decode("utf-8")
        self.public_key = key.verify_key.encode(encoder=nacl.encoding.HexEncoder).decode("utf-8")
        self.save_keys()
        logger.info("Generated new key pair.")

    def save_keys(self):
        """
        Save the keys to a file.
        """
        keys = {"private_key": self.private_key, "public_key": self.public_key}
        with open(self.key_file, "w") as f:
            json.dump(keys, f)
        logger.info(f"Keys saved to {self.key_file}.")

    def load_keys(self):
        """
        Load keys from the key file.
        """
        try:
            with open(self.key_file, "r") as f:
                keys = json.load(f)
                self.private_key = keys["private_key"]
                self.public_key = keys["public_key"]
            logger.info("Keys loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load keys: {e}")
            self.generate_keys()


def sign_event(event, private_key):
    """
    Sign a Nostr event using the private key.
    """
    signing_key = nacl.signing.SigningKey(private_key, encoder=nacl.encoding.HexEncoder)
    serialized_event = f"{event['pubkey']}{event['created_at']}{event['kind']}{event['tags']}{event['content']}"
    signature = signing_key.sign(serialized_event.encode("utf-8"))
    return base64.b64encode(signature.signature).decode("utf-8")


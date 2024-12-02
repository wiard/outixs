# File: nostr/utils/nostr_crypt.py

import nacl.signing
import nacl.encoding
import nacl.exceptions
from lib.logger import Logger

logger = Logger("NostrCrypt")


def verify_signature(event, public_key, signature):
    """
    Verify the signature of a Nostr event.
    """
    try:
        verify_key = nacl.signing.VerifyKey(public_key, encoder=nacl.encoding.HexEncoder)
        serialized_event = f"{event['pubkey']}{event['created_at']}{event['kind']}{event['tags']}{event['content']}"
        verify_key.verify(serialized_event.encode("utf-8"), base64.b64decode(signature))
        logger.debug("Signature verification successful.")
        return True
    except nacl.exceptions.BadSignatureError:
        logger.warning("Signature verification failed.")
        return False


def encrypt_message(message, recipient_pubkey):
    """
    Encrypt a message for a recipient using their public key.
    """
    # Placeholder for actual encryption logic
    logger.debug("Encrypting message.")
    return f"encrypted({message})"


def decrypt_message(encrypted_message, private_key):
    """
    Decrypt a message using the recipient's private key.
    """
    # Placeholder for actual decryption logic
    logger.debug("Decrypting message.")
    return encrypted_message.replace("encrypted(", "").replace(")", "")


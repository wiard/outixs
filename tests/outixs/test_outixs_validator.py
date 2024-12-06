import unittest
from outixs.outixs_validator import OutixsValidator

class TestOutixsValidator(unittest.TestCase):
    def setUp(self):
        self.validator = OutixsValidator()

    def test_validate_valid_outixs(self):
        valid_outixs = {
            "utxo": "abcd1234",
            "metadata": {
                "key": "value",
                "timestamp": "2024-12-06T12:00:00Z"
            },
            "conditions": {
                "time_lock": 1672531200,
                "escrow": True
            }
        }
        result = self.validator.validate(valid_outixs)
        self.assertTrue(result)

    def test_validate_missing_utxo(self):
        invalid_outixs = {
            "metadata": {
                "key": "value",
                "timestamp": "2024-12-06T12:00:00Z"
            },
            "conditions": {
                "time_lock": 1672531200,
                "escrow": True
            }
        }
        result = self.validator.validate(invalid_outixs)
        self.assertFalse(result)

    def test_validate_invalid_metadata(self):
        invalid_outixs = {
            "utxo": "abcd1234",
            "metadata": "invalid",
            "conditions": {
                "time_lock": 1672531200,
                "escrow": True
            }
        }
        result = self.validator.validate(invalid_outixs)
        self.assertFalse(result)

    def test_validate_missing_conditions(self):
        invalid_outixs = {
            "utxo": "abcd1234",
            "metadata": {
                "key": "value",
                "timestamp": "2024-12-06T12:00:00Z"
            }
        }
        result = self.validator.validate(invalid_outixs)
        self.assertFalse(result)

    def test_validate_empty_outixs(self):
        empty_outixs = {}
        result = self.validator.validate(empty_outixs)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()


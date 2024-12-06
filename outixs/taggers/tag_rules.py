from tags.tag_rules import TagRules

outixs_object = {
    "metadata": {"tags": ["art"]},
    "value": 0.5,
    "original_txid": "abcd1234"
}

# Validate a single tag
print(TagRules.validate_tag("art"))  # True
print(TagRules.validate_tag("invalid_tag"))  # False

# Apply default tags
updated_outixs = TagRules.apply_default_tags(outixs_object)
print(updated_outixs["metadata"]["tags"])  # ["art", "marketplace"]


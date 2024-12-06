class MetadataUtils:
    @staticmethod
    def add_tag(metadata, tag):
        metadata["tags"] = metadata.get("tags", [])
        if tag not in metadata["tags"]:
            metadata["tags"].append(tag)

    @staticmethod
    def filter_by_tag(outixs_list, tag):
        return [outixs for outixs in outixs_list if tag in 
outixs["metadata"].get("tags", [])]


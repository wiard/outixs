class AutoTagger:
    def __init__(self, rules):
        self.rules = rules

    def tag(self, data):
        tags = []
        for rule in self.rules:
            if rule["condition"](data):
                tags.append(rule["tag"])
        return tags


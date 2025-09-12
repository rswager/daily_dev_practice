import json

class FeatureFlagManager:
    def __init__(self, config_file):
        with open(config_file, "r") as f:
            self.config = json.load(f)

    def is_enabled(self, feature_name, user=None):
        # Check user-specific overrides
        if user and user in self.config["user_overrides"]:
            if feature_name in self.config["user_overrides"][user]:
                return self.config["user_overrides"][user][feature_name]

        # Fall back to global flag
        return self.config["global_flags"].get(feature_name, False)

    def toggle_feature(self, feature_name, value):
        self.config["global_flags"][feature_name] = value
        print(f"Feature '{feature_name}' set to {value}")

    def toggle_user_feature(self, user_name, feature_name, value):
        self.config['user_overrides'][user_name][feature_name] = value
        print(f"User [{user_name}] Feature [{feature_name}] set to {value}")

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.config, f, indent=2)

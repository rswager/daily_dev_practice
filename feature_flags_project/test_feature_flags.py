from feature_flags import FeatureFlagManager

flags = FeatureFlagManager("config.json")

assert flags.is_enabled("new_dashboard") == True
assert flags.is_enabled("dark_mode", "alice") == True
assert flags.is_enabled("beta_feature", "bob") == True
assert flags.is_enabled("dark_mode", "bob") == False

print("✅ All tests passed!")
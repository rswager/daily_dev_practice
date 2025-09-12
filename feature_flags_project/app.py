from feature_flags import FeatureFlagManager

config_file = 'config.json'
flags = FeatureFlagManager(config_file)


def clamp(value, lower, upper):
    return max(lower, min(value, upper))


def check_features(user_in):
    print("\n=== Feature Check ===")
    if flags.is_enabled("new_dashboard", user_in):
        print("✅ New Dashboard is enabled!")
    else:
        print("❌ New Dashboard is disabled.")

    if flags.is_enabled("dark_mode", user_in):
        print("🌙 Dark mode activated.")
    else:
        print("🌞 Using light mode.")

    if flags.is_enabled("beta_feature", user_in):
        print("🧪 Beta feature active.")
    else:
        print("🚫 Beta feature unavailable.")


def main_menu(user_in):
    if user_in != 'admin':
        print("\n=== Main Menu ===")
        print("1. Toggle New Dashboard\n2. Toggle Light Mode\n3. Toggle Beta Feature\n4. Exit")
        selection = clamp(int(input("Select option: ")), 1, 3)

        if selection == 1:
            flags.toggle_user_feature(user_name=user_in, feature_name='new_dashboard',
                                      value=not (flags.is_enabled('new_dashboard', user_in)))
        elif selection == 2:
            flags.toggle_user_feature(user_name=user_in, feature_name='dark_mode',
                                      value=not (flags.is_enabled('dark_mode', user_in)))
        elif selection == 3:
            flags.toggle_user_feature(user_name=user_in, feature_name='beta_feature',
                                      value=not (flags.is_enabled('beta_feature', user_in)))
        elif selection == 4:
            quit()
        flags.save(config_file)
    else:
        print("\n=== Main Menu ===")
        print("1. Toggle New Dashboard\n2. Toggle Light Mode\n3. Toggle Beta Feature\n4. Exit")
        selection = clamp(int(input("Select option: ")), 1, 3)

        if selection == 1:
            flags.toggle_feature(feature_name='new_dashboard',
                                 value=not (flags.is_enabled('new_dashboard', user_in)))
        elif selection == 2:
            flags.toggle_feature(feature_name='dark_mode',
                                 value=not (flags.is_enabled('dark_mode', user_in)))
        elif selection == 3:
            flags.toggle_feature(feature_name='beta_feature',
                                 value=not (flags.is_enabled('beta_feature', user_in)))
        elif selection == 4:
            quit()
        flags.save(config_file)


def main():
    user = input("Enter your username: ").strip()
    check_features(user)
    main_menu(user)
    check_features(user)


if __name__ == "__main__":
    main()

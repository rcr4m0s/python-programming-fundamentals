class SecretVault:
    def __init__(self, code):
        self.__code = code

    def get_code(self):
        return self.__code

vault =SecretVault(1234)

print(f"Code via Getter: {vault.get_code()}")


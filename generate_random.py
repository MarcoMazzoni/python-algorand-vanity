from algosdk import account, mnemonic


if __name__ == '__main__':
    private_key, public_address = account.generate_account()
    mnemo = mnemonic.from_private_key(private_key)
    print(f"Algorand Address: {public_address}")
    print(f"Private Key: {private_key}")
    print(f"Mnemonic:\n{mnemo}")

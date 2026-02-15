import bux

if __name__ == "__main__":
    try:
        bux.validate_license()
    except Exception as e:
        print(f"Error: {e}")
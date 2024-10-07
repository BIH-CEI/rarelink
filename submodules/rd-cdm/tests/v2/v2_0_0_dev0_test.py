from tests import validate_schemas

def main():
    version = "2.0.0" 
    if validate_schemas(version):
        print(f"{version} JSON Schema pass! 🎉")
    else:
        print("JSON Schema validation failed.")

if __name__ == "__main__":
    main()
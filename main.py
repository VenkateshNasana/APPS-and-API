# Root entry point for INTEGRAX
import os
import sys

def main():
    print("Initializing INTEGRAX Enterprise Platform...")
    os.system("docker-compose up -d")

if __name__ == "__main__":
    main()

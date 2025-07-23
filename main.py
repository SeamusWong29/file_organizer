import argparse
import os
import sys
from utils import organize_by_extension, organize_by_date

def main():
    ap = argparse.ArgumentParser(description= "Organize files by extension or date")
    ap.add_argument("--path", required=True, help="Folder path to organize")
    ap.add_argument("--mode", required=True, choices=["ext", "date"], help= "Organize by 'ext' or 'date'")
    ap.add_argument("--dry-run", action="store_true", help="Print actions without making changes")
    args = ap.parse_args()

    if not os.path.exist(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        sys.exit(1)
    if not os.access(args.path, os.R_OK, os.W_OK):
        print(f"Error: No read/write permission for {args.path}")
        sys.exit(1)

    if args.mode == "ext":
        organize_by_extension(args.path, args.dry_run)  # string
    elif args.mode == "date":
        organize_by_date(args.path, args.dry_run)
  
  
# main.py
if __name__ == "__main__":
    main()
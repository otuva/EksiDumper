import sys
from src import extract_entry_ids
from src import dump_all_entries_to_csv

username = sys.argv[1]

print("    Getting all entry ids")
extract_entry_ids.main(username)
print("    Got all entries.")

print("    Starting to dump")
dump_all_entries_to_csv.main(username)
print("    Dumping completed.")

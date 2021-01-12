# Malvertising scanning

This software can scan a list of domains for redirects. 

It will save the result to a sqlite3 database. 

Just remember that it only does this in one level.

Usage:
```
python skanner.py <file with domain names>
```

See all redirects that could be bad
```
cat all_results.sql | sqlite3 malvertasingdb.db
```


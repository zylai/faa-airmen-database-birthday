# FAA Airmen Database Birthday Brute Force Tool

### Work in progress

### WARNING: This is a proof of concept and is not intended to be used for malicious purposes

The Federal Aviation Administration (FAA)'s airmen database lets anyone look up information about a pilot. The only required field is last name. However, other fields such as first name, certificate number, date of birth, etc. are available to narrow down the results. If these optional fields are used, their values must be an exact match for the database to return a result.

Using Charles Lindbergh as an example (yes, the FAA's database goes back that far): 

```
Query: Lindbergh, 02/04/1902
Total names found is 1 based on the search criteria provided above.
```

Note that the DOB cannot be partial and must be an exact match.

```
Query: Lindbergh, 02/05/1903
No records found based on search criteria provided above. 
```

This is a design flaw as it allows a pilot's DOB to be discovered via brute forcing. One just has to loop through every possible date until the query returns a match. On a good day, the FAA database takes about 8 seconds per query. If you can narrow down a person's birthday to a 10-year range, you can find out someone's DOB in about 10 hours. A dedicated attacker can run this in parallel and discover an individual's DOB in a matter of hours in a spear phishing attack.

For this tool to work, you must provide enough information about an airman so that the query only returns one results. The script automatically stops as soon as it finds a query with at least one result. Also note that if a query returns more than 50 results, you must provide more information to narrow down the results. There is also a bug in the FAA's database where 01/01/1900 matches everyone.

Requires Selenium and WebDriver. Tested on Python 3.9 on macOS Big Sur (11.0).

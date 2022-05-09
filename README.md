# FAA Airmen Database Birthday Brute Force Tool

### WARNING: This is a proof of concept and is not intended to be used for malicious purposes

The Federal Aviation Administration (FAA)'s airmen database lets anyone look up information about a pilot. The only required field is last name. However, other fields such as first name, certificate number, date of birth, etc. are available to narrow down the results. If these optional fields are used, their values must be an exact match for the database to return a result.

Using Charles Lindbergh as an example (yes, the FAA's database goes back that far): 

```
Query
----
Last name: Lindbergh
First name: Char
DOB: Feb 04, 1902

Result
----
Total names found is 1 based on the search criteria provided above.
```

Note that the DOB cannot be partial and must be an exact match.

```
Query
----
Last name: Lindbergh
First name: Char
DOB: Feb 05, 1903

Result
----
No records found based on search criteria provided above. 
```

This is a design flaw as it allows a pilot's DOB to be discovered via brute forcing. One just has to loop through every possible date until the query returns a match. On a good day, the FAA database takes about 5-7 seconds per query. In addition, there appears to not be a throttling mechainism in place to limit the amount of queries one can send. If you can narrow down a person's birthday to a 10-year range, you can find out their DOB in about 10 hours. In a spear phishing attack, a dedicated attacker can run this in parallel and discover an individual's DOB in a matter of hours. In this day and age where most identity verification is done by providing your DOB and last 4 of SSN, I consider this a pretty significant design flaw. 

For this tool to work, you must provide enough information about an airman so that the query only returns one result. The script automatically stops as soon as it a query returns at least one match. Also note that if a query returns more than 50 results, you must provide more information to narrow down the results.

Requires Selenium and WebDriver. Tested on Python 3.9 on macOS Big Sur (11.0).

### Additional notes

- There is a bug in the FAA's database where 01/01/1900 matches everyone
- This same method could also be used to discover a pilot's certificate number since the FAA assigns certificate numbers incrementally, although much harder as there are 7 digits
  - We're in the 4xxxxxx range beginning ~2017
  - Note that a certificate number is only generated once (typically after an airman's first approved 8710) and they're stuck with that number for life
    - For pilots that soloed before April 1, 2016, this is typically a sport, recreational, or private pilot certificate
    - For pilots that soloed after April 1, 2016, this will always be a student pilot certificate
  - For some older pilots, the certificate number is their social security number
    - Though the FAA has discontinued this practice a while ago and allows anyone with a SSN certificate number to request a new number
- This design flaw does not affect the city and state fields since the FAA allows an airman to opt out of making their address publicly visible
  - In that case, the database returns no results even if your query is correct

### Roadmap

- Allow user to define a narrower date range (only search through specific year or month)
- Allow user to define narrower search parameters (certificate number, country, or city and state)

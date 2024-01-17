# FAA Airmen Database Birthday Brute Force Tool

The US Federal Aviation Administration's Airmen Database Inquiry tool lets anyone look up information about a pilot. The only required field is last name.

If a query returns more than 50 results, you must provide additional information (such as first name, certificate number, date of birth, etc.) to narrow down the results. If these optional fields are used, their values must be an exact match for the database to return a result.

Tested on Python 3.9 on macOS Big Sur (11.0).

### Example

Using Charles Lindbergh as an example (yes, the FAA's database goes back that far): 

```
========
Query
========
Last name: Lindbergh
First name: Charles
DOB: Feb 04, 1902    # Correct birth date

========
Result
========
Total names found is 1 based on the search criteria provided above.

CHARLES A LINDBERGH
```

Note that the DOB cannot be partial and must be an exact match.

```
========
Query
========
Last name: Lindbergh
First name: Charles
DOB: Feb 05, 1902    # Incorrect birth date

========
Result
========
No records found based on search criteria provided above. 
```
### Issue

This is a design flaw as it allows a pilot's date of birth to be discovered via brute forcing. One just has to loop through every possible date (which is not that many) until the query returns a match.

On a good day, the FAA database takes about 2-3 seconds per query, and there appears to not be a throttling mechainism in place to limit the amount of queries one can send. If you can narrow down a person's age to a 10-year range, you can discover their date of birth in about 3 hours. In a spear phishing attack, a dedicated attacker can run this in parallel, cutting down the time.

In this day and age where most identity verification is done by providing your DOB and last 4 digits of SSN, I consider this a pretty significant design oversight.

However, it seems like the FAA disagrees that date of birth is personally identifiable information (PII) and will freely hand it out under a Freedom of Information Act (FOIA) request.

### Additional notes

- There is a bug in the FAA's database where 01/01/1900 matches everyone.
- This same method could also be used to discover a pilot's certificate number since the FAA assigns certificate numbers incrementally, although much harder as there are 7 digits.
 - For some older pilots, the certificate number is their social security number, though the FAA has discontinued this practice a while ago and allows anyone with a SSN certificate number to request a new number.
- This design flaw does not affect the city and state fields since the FAA allows an airman to opt out of making their address publicly visible.
  - In that case, the database returns no results even if your query is correct.

### Roadmap

- Allow user to define a narrower date range (only search through specific year or month)
- Allow user to define narrower search parameters (certificate number, country, or city and state)

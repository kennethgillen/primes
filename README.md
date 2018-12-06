# Primes

### Travis-CI test status:
#### Branch: master
[![Build Status](https://travis-ci.org/kennethgillen/primes.svg?branch=master)](https://travis-ci.org/kennethgillen/primes)
#### Branch: getting_started - initial development
[![Build Status](https://travis-ci.org/kennethgillen/primes.svg?branch=getting_started)](https://travis-ci.org/kennethgillen/primes)

### How to run this application

The application itself is a python script, `primes.py`.

I have included a docker-compose file which will take care of the creation of the execution environment for the `primes.py` script, for which I've chosen to use Docker. This will ensure that anyone executing the script will have the same experience as the developer, and also will allow functional testing of the container with Travis-CI.

`docker-compose run --rm primes 5`
```
|   | 2 | 3 | 5 | 7 | 11 |
| 2 | 4 | 6 | 10 | 14 | 22 |
| 3 | 6 | 9 | 15 | 21 | 33 |
| 5 | 10 | 15 | 25 | 35 | 55 |
| 7 | 14 | 21 | 35 | 49 | 77 |
| 11 | 22 | 33 | 55 | 77 | 121 |
```

### What I'm pleased with
- The prime generation with numpy was surprisingly performant.

### What I would do with it if you had more time
- There are various TODO or RFE comments in the source. 
- Not instantiating a second array would be a good start. That's costing twice the ram. 
- I used docker-compose with a view to doing something multi-container with, e.g. redis, but I quickly realised that was way too complex. But given how long the multiplication table takes to execute (15m for 20k primes), I think we need to scale across multiple containers.

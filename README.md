# Binomial option pricing

A Python exercise in pricing European and American calls and puts with a binomial tree. The `option()` function constructs terminal payoffs. European prices use a weighted terminal sum; American prices work backwards through the tree and compare continuation with early exercise.

It uses only `math`. Inputs cover expiry and spot price, with strike, rates and volatility supplied as function arguments. Four included examples ran during review and rounded to their commented values: 6.18, 7.43, 53.93 and 4.85. The original textbook reference is not recorded.

## Run the examples

Python 3, from this folder:

```sh
python3 "Binomial Option Pricing.py"
```

Edit the calls at the bottom to try other inputs. There is no CLI argument parser or CSV ingestion; the pandas idea in the source is only a comment.

The routine has no input validation. Its discount factor uses `r - q`, and the American branch applies put-style exercise before checking the option kind. The included examples do not verify general correctness, especially for nonzero dividends or American calls. An American call with every terminal price below the strike returned 99 rather than zero in a review counterexample. These cases need independent reference tests before the output is relied on.

# Binomial option pricing

A Python exercise in pricing European and American calls and puts with a binomial tree. The `option()` function constructs terminal payoffs. European prices use a weighted terminal sum; American prices work backwards through the tree and compare continuation with early exercise.

It uses only `math`. Inputs cover expiry and spot price, with strike, rates and volatility supplied as function arguments. Four included examples reproduce the textbook values 4.49, 7.43, 53.39 and 4.66, matching an independent backward-induction reference.

## Run the examples

Python 3, from this folder:

```sh
python3 "Binomial Option Pricing.py"
```

Edit the calls at the bottom to try other inputs. There is no CLI argument parser or CSV ingestion; the pandas idea in the source is only a comment.

The routine has no input validation. Discounting uses the risk-free rate `r` (the dividend yield `q` only enters the risk-neutral probability), and early exercise is checked according to the option kind (call or put).

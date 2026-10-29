# Binomial option pricing

A Python binomial-tree pricer for European and American calls and puts, with a slide deck covering theory and a worked walkthrough.

- **Method:** European prices use a weighted terminal sum; American prices work backwards and compare continuation with early exercise. Standard library (`math`) only.
- **Validation:** four textbook examples (4.49, 7.43, 53.39, 4.66) reproduce, and input checks include a no-arbitrage test on the up probability.
- **Tests:** convergence to Black–Scholes, put–call parity, American ≥ European, and American call = European call without dividends.

## Run

```sh
python3 "Binomial Option Pricing.py"   # edit the calls under __main__ to try other inputs
python3 -m unittest -v
```

Slides: `Binomial Option Pricing.pptx`.

## Limits

No command-line interface or file input; inputs are function arguments. The dividend yield `q` only enters the risk-neutral probability.

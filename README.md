# Binomial option pricing

A Python binomial-tree pricer for European and American calls and puts, with a slide deck covering theory and a worked walkthrough.

- **Method:** European prices use a weighted terminal sum; American prices work backwards and compare continuation with early exercise. Standard library (`math`) only; the `option()` function builds the terminal payoffs.
- **Validation:** four textbook examples (4.49, 7.43, 53.39, 4.66) reproduce and match an independent backward-induction reference. Inputs are validated (option kind, positive T, S, K, sigma, integer n, and a no-arbitrage check on the up probability).
- **Tests:** convergence to Black–Scholes, put–call parity, American ≥ European, and American call = European call without dividends.

## Run

```sh
python3 "Binomial Option Pricing.py"   # edit the calls under __main__ to try other inputs
python3 -m unittest -v
```

Slides: `Binomial Option Pricing.pptx`.

## Limits

No command-line interface or file input; expiry and spot are inputs and strike, rates and volatility are function arguments. Discounting uses the risk-free rate `r`; the dividend yield `q` only enters the risk-neutral probability.

[MIT licence](LICENSE)

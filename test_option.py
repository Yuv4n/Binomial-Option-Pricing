"""Reference tests for option(): run with  python3 -m unittest -v"""
import importlib.util
import math
import unittest

_spec = importlib.util.spec_from_file_location("bop", "Binomial Option Pricing.py")
bop = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bop)
option = bop.option


def black_scholes(T, S, K, r, sigma, q, kind):
    d1 = (math.log(S / K) + (r - q + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    N = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
    if kind == "Call":
        return S * math.exp(-q * T) * N(d1) - K * math.exp(-r * T) * N(d2)
    return K * math.exp(-r * T) * N(-d2) - S * math.exp(-q * T) * N(-d1)


class TextbookExamples(unittest.TestCase):
    def test_examples(self):
        cases = [
            ((0.75, 31, 30, 0.05, 0.3, 3, 0, "American", "Call"), 4.49),
            ((2, 50, 52, 0.05, 0.3, 2, 0, "American", "Put"), 7.43),
            ((0.5, 810, 800, 0.05, 0.2, 2, 0.02, "European", "Call"), 53.39),
            ((2, 50, 52, 0.05, 0.2, 2, 0.02, "European", "Put"), 4.66),
        ]
        for args, expected in cases:
            self.assertAlmostEqual(option(*args), expected, places=2)


class Properties(unittest.TestCase):
    def test_converges_to_black_scholes(self):
        for kind in ("Call", "Put"):
            bs = black_scholes(1, 100, 95, 0.05, 0.2, 0.02, kind)
            self.assertAlmostEqual(option(1, 100, 95, 0.05, 0.2, 200, 0.02, "European", kind), bs, delta=0.03)

    def test_put_call_parity(self):
        T, S, K, r, q = 1, 100, 95, 0.05, 0.02
        c = option(T, S, K, r, 0.2, 50, q, "European", "Call")
        p = option(T, S, K, r, 0.2, 50, q, "European", "Put")
        self.assertAlmostEqual(c - p, S * math.exp(-q * T) - K * math.exp(-r * T), places=8)

    def test_american_at_least_european(self):
        for kind in ("Call", "Put"):
            for q in (0, 0.03):
                a = option(1, 100, 100, 0.05, 0.25, 20, q, "American", kind)
                e = option(1, 100, 100, 0.05, 0.25, 20, q, "European", kind)
                self.assertGreaterEqual(a, e - 1e-12)

    def test_american_call_no_dividend_equals_european(self):
        a = option(1, 100, 100, 0.05, 0.25, 20, 0, "American", "Call")
        e = option(1, 100, 100, 0.05, 0.25, 20, 0, "European", "Call")
        self.assertAlmostEqual(a, e, places=10)

    def test_deep_out_of_the_money_american_call_is_not_strike(self):
        self.assertLess(option(1, 10, 100, 0.05, 0.2, 3, 0, "American", "Call"), 1e-6)

    def test_american_put_at_least_intrinsic(self):
        self.assertGreaterEqual(option(1, 50, 100, 0.05, 0.2, 10, 0, "American", "Put"), 50 - 1e-9)


class Validation(unittest.TestCase):
    def test_bad_inputs(self):
        bad = [(1, 100, 100, .05, .2, 3, 0, "Bermudan", "Call"), (1, 100, 100, .05, .2, 3, 0, "European", "Straddle"),
               (1, 100, 100, .05, .2, 0, 0, "European", "Call"), (-1, 100, 100, .05, .2, 3, 0, "European", "Call"),
               (1, 100, 100, .5, .01, 1, 0, "European", "Call")]
        for args in bad:
            with self.assertRaises(ValueError):
                option(*args)


if __name__ == "__main__":
    unittest.main()

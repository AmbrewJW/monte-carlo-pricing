# Monte Carlo Option Pricing

This project uses Monte Carlo simulation to model stock price paths and
estimate the value of European call options.

## Motivation
Closed-form formulas require advanced calculus. Monte Carlo simulation
provides a numerical alternative that is intuitive and flexible.

## Method
- Simulate random returns using a normal distribution
- Convert returns into stock price paths
- Estimate option payoffs at maturity
- Average and discount payoffs to estimate price

## Current Status
- [x] Random return simulation
- [ ] Stock price path generation
- [ ] Option payoff calculation

## Future Work
- Compare results to Black-Scholes formula
- Improve performance with vectorization

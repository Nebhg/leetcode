# Phase 3 — Interview Simulation

## When to start this phase
- You can solve Phase 1 easy problems cold in under 10 minutes
- You recognise Two Pointers, Sliding Window, and Hashmap patterns on sight
- You're at least into Week 2 of the plan

## How to run a mock session

### Setup
1. Pick 2 problems from the Phase 2 medium list in README.md
2. Set a 30 minute timer per problem
3. No AI, no hints, no discussion posts
4. Talk through your approach out loud before writing any code

### Structure per problem (30 mins)
- 0-5 mins: Read, understand, think about approach, state it out loud
- 5-25 mins: Code the solution
- 25-30 mins: Test with examples, fix bugs

### After the timer
- Review your solution
- Look at the optimal solution on NeetCode
- Write down what you would do differently

## Mock interview questions — practice answering out loud

### About your work
- Walk me through a complex data problem you've solved
- How did you design the Cap IQ ingestion pipeline?
- How do you ensure data quality at scale?
- What would you do differently if you rebuilt it?
- How does your ETL agent framework work?
- What's the hardest engineering problem you've faced?

### Technical concepts
- What's the difference between a stack and a queue?
- When would you use a hashmap vs a set?
- What's the time and space complexity of your solution?
- Can you optimise this further?
- What edge cases does your solution handle?
- Walk me through your approach before you start coding

## Point72 Specific Prep

### System design — be able to explain these clearly
- How you'd design a pipeline to ingest market data for 1,500 companies daily
- How database indexing works and when to use it
- Batch vs streaming — when to use each and trade-offs
- How you'd debug a slow running query
- How your Cap IQ pipeline handles 500M+ rows — what are the bottlenecks?

### SQL window functions — must know cold
```sql
-- ROW_NUMBER: unique row number per partition
SELECT ticker, date, price,
    ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY date DESC) as rn
FROM prices;

-- RANK: same rank for ties, gaps after ties
SELECT ticker, revenue,
    RANK() OVER (PARTITION BY sector ORDER BY revenue DESC) as revenue_rank
FROM companies;

-- LAG: access previous row value
SELECT ticker, date, price,
    LAG(price, 1) OVER (PARTITION BY ticker ORDER BY date) as prev_price,
    price - LAG(price, 1) OVER (PARTITION BY ticker ORDER BY date) as price_change
FROM prices;

-- LEAD: access next row value
SELECT ticker, date, price,
    LEAD(price, 1) OVER (PARTITION BY ticker ORDER BY date) as next_price
FROM prices;

-- Running total
SELECT ticker, date, volume,
    SUM(volume) OVER (PARTITION BY ticker ORDER BY date ROWS UNBOUNDED PRECEDING) as cumulative_volume
FROM prices;

-- Moving average
SELECT ticker, date, price,
    AVG(price) OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as ma_30
FROM prices;
```

### Pandas equivalents — know these for the interview
```python
import pandas as pd

# groupby + rank (like RANK() OVER PARTITION BY)
df['revenue_rank'] = df.groupby('sector')['revenue'].rank(ascending=False)

# shift (like LAG/LEAD)
df['prev_price'] = df.groupby('ticker')['price'].shift(1)
df['next_price'] = df.groupby('ticker')['price'].shift(-1)
df['price_change'] = df['price'] - df['prev_price']

# rolling window (like moving average)
df['ma_30'] = (
    df.groupby('ticker')['price']
    .transform(lambda x: x.rolling(30, min_periods=1).mean())
)

# cumulative sum (like running total)
df['cumulative_volume'] = df.groupby('ticker')['volume'].cumsum()

# top N per group (like ROW_NUMBER + filter)
df['rn'] = df.groupby('sector')['revenue'].rank(ascending=False)
top3_per_sector = df[df['rn'] <= 3]
```

### Cap IQ project — have this story ready
Be able to explain:
1. What the pipeline does (consensus estimates, 1,500 companies, 500M+ rows)
2. How data flows end to end (ingestion → transformation → storage → serving)
3. The architecture decisions you made and why
4. What the main challenges were at that scale
5. How you'd do it differently now
6. How it connects to what Point72 would need

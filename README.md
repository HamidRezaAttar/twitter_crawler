<h1 align="center">Twitter Crawler 🐦</h1>
 
## A simple script for crawling twitter data using [snscrape](https://github.com/JustAnotherArchivist/snscrape).

<br>

# How to use


## Pre Requirements (Python 3.7.15)

```bash
snscrape == 0.3.4
pandas == 1.5.2
```

## How to get result

```python
t = Twitter()

res1 = t.search(
    query="Bitcoin", 
    start="2021-01-01 00:00:00",
    end="2021-05-32 00:00:00", 
    n_tweet=10
)

res2 = t.search_account(
    user_ls=["tim_cook", "BillGates"],
    start="2021-01-01 00:00:00",
    end="2021-05-32 00:00:00",
    n_tweet=10,
)
```

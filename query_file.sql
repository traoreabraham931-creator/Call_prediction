CREATE TABLE call_data( 
    strike DECIMAL,
    bid DECIMAL,
    bid_size DECIMAL,
    ask DECIMAL,
    ask_size DECIMAL,
    delta DECIMAL, 
    gamma DECIMAL,
    theta DECIMAL,
    vega DECIMAL,
    implied_volatility DECIMAL,
    expiration DATE);

COPY call_data (expiration, strike, bid, bid_size, ask, ask_size, delta, gamma, theta, vega, implied_volatility) From '/var/lib/postgresql/data/call_usa_options.csv' DELIMITER ',' CSV HEADER;



Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.


Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
Output:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation:
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.
























SQL Schema:
    Create table If Not Exists Tweets(tweet_id int, content varchar(50))
    Truncate table Tweets
    insert into Tweets (tweet_id, content) values ('1', 'Let us Code')
    insert into Tweets (tweet_id, content) values ('2', 'More than fifteen chars are here!')











Pandas Schema:
    data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
    tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
















Solution:
    ### SQL Solution

    sql

    ```sql
    SELECT tweet_id
    FROM Tweets
    WHERE LENGTH(content) > 15;
    ```

    ### Pandas Solution

    python

    ```python
    import pandas as pd

    def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
        return tweets[tweets['content'].str.len() > 15][['tweet_id']]
    ```

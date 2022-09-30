# Input format
To align with the given example, I assume the input data should be in **json format** and encoded in **'UTF-8 with BOM'**.
Besides, the data should be represented as a 3-dims array.
```commandline
Example:
[
  [
    [1, 0.74912488, 0.94462675, 0.81221404],
    [1.33489092, 1, 1.31850973, 1.19237963],
    [1.05861919, 0.75843202, 1, 0.94786255],
    [1.23120255, 0.83866098, 1.05500529, 1]
  ]
]
```

# Setup

```
cd InstaDeep_Coding_Challenge
pip install -r dependencies/requirements.txt
```

- Requirements
  * numpy>=1.21.6
  * pytest>=7.1.3 
  * python>=3.7.3
# Usage

```
cd InstaDeep_Coding_Challenge
python3 -m src.main max_profit -input currency_data.txt -output aaa.txt -name_list A,B,C,D -start 0 -end 0
```

- -input (required): The file path of input data file.
- -output (optional): The file path of output data file.
  - Default: 'output.txt'
- -name\_list (optional): The names of currencies. You can use 'GBP,USD,EUR,JPY'.
  - Default: '1,2,3,...'
- -start (optional): The index of starting currency such as 'GBP' in the example.
  - Default: 0
- -end (optional): The index of ending currency such as 'GBP' in the example. 
  - Default: 0
# Test
```
cd InstaDeep_Coding_Challenge
python3 -m pytest
```

# Algorithm
  I used dynamic programming to solve this problem.
  Because the maximum value of each currency in i-th month is depending on the maximum value of
   each currency in (i-1)-th month and the trading condition in i-th month,
  we can formulate the relation as

```python
max_val[i][j] = max(max_val[i-1]*trading_condition[i])
#The max_val of j-th currency in i-th month is the maximum of
#the max_val of each currencies in (i-1)-th month multiple
#the exchange rate it can be exchange to j-th currency.
```

First, we need to set the max_val of the first month as the
exchange rate of GBP, because we can only start from GBP. Then,
we can use this formula and the max_val[0] to calculate the following
statements and pick the max_val of GBP in the final statement as our return.

- Time complexity: O(n\*(m^2)), We need to do **n** times **m\*m** multiplication to get each statement. **n** for the number of months; **m** for the number of currencies.
- Space complexity: O(m\*max(m,n)). We need O(n\*m) to store the max\_val of each month
  and O(m^2) to do matrix element-wise multiplication.
# Worth to talk

* **Corresponding elements in the matrix should be reciprocal but not**
  - I thought it's reasonable that in each month the corresponding exchange rate should be reciprocal
   but it's not in data[10][1][0] and data[10][0][1]. Thus, I assume that it's normal that two corresponding 
   exchange rates are not in reciprocal relation.
* **Output file**

  - I make the result saved as a file so that user can manipulate the result conveniently.

* **Transition steps**

  - Not only the max\_profit, I also provide the detail of transitions to make user know how
   to reach it.

* **Changeable start and end currencies**
  - Because this is a production code, I think it's reasonable to let user change these parameters. You
   can do this by changing optional parameters.

# Big Data Course - Hadoop Assignment

## Exercise 1

### Q1. How many files are there?
There are **7** items in total in the output directory: **6** output part-files (`part-00000` to `part-00005`) and **1** status file named `_SUCCESS`.

### Q2. Did the number of mappers change?
**No.** The number of map tasks remained **9** across both runs. The number of mappers is determined by the input data and its splits across HDFS blocks, not by the reducer configuration.

### Q3. Did the number of reducers change?
**Yes.** In the baseline run, the cluster used the default of **3** reducers. In the second run, it increased to **6** because we explicitly specified the `-numReduceTasks 6` flag.

### Q4. Did the number of output files change? Why?
**Yes.** The number of part-files increased from 3 (`part-00000` to `part-00002`) to 6 (`part-00000` to `part-00005`). In Hadoop MapReduce, each reducer task writes its final partition results into its own independent output file. Therefore, 6 reducers produce exactly 6 part-files.

### Q5. What does the value of 'Merged Map outputs' represent, and how is it calculated?
The 'Merged Map outputs' counter tracks the total number of map output partitions transferred (shuffled) and merged by all reducers prior to reducing.
It is calculated as:
`Merged Map outputs = Launched map tasks * Launched reduce tasks`
* In the first run: 9 mappers * 3 reducers = **27**
* In the second run: 9 mappers * 6 reducers = **54**

---

## Exercise 2

### Q1. Is your change in the mapper or in the reducer?
The change is in the **mapper** (`mapper.py`). 
The mapper is responsible for parsing initial input tokens. Cleaning trailing punctuation (dots and commas) and normalizing text to lower-case must occur before the shuffle-and-sort phase so identical words with different casings or punctuation are grouped under the exact same key.

---

## Exercise 3

### Q1. Is your change in the mapper or in the reducer?
The change is in the **reducer** (`reducer.py`). 
The reducer aggregates the total counts for all occurrences of each word. Global sorting and selecting the top 3 highest scores must take place after all counts have been summed. Additionally, the job was executed with `-numReduceTasks 1` to ensure a single reducer produces a globally sorted top 3 output.

### Q3. Output Screenshot
Below is the screenshot showing the execution of `hadoop fs -ls /user/hduser/gutenberg-output` and the resulting top 3 word counts:

![Top 3 Output](top3_output.png)

# Memorization Tool
Work with the SQLAlchemy ORM and an SQLite database to create a tool for memorizing.

It would be great to remember anything at any time. Alas, our mental capacity is limited. The good thing is that there are a lot of tools to help us memorize things. This project is a tool for memorizing lines, poems, speeches, and other text-based materials.

This project implement the Leitner system. In short, it introduces the concept of spaced repetition proposed by Sebastian Leitner, a German scientist. Leitner's system suggests reviewing cards at increased intervals.

We can divide the memorization process into several parts. First, you create several boxes (usually from 3 to 5) that will store your flashcards. You mark each box with time periods that show how frequently the cards should be reviewed. For example, Box 1 will contain the most difficult cards, so they should be reviewed every day; Box 2 will have easier cards that you will check more rarely, every two days, and so on.

## Examples

Example
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2
There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1
1. Add a new flashcard
2. Exit
> 1

Question:
> What is the Capital of Turkey?
Answer:
> Ankara

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital of Croatia?
Answer:
> Zagreb

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2
There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```
Example 2
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 6
6 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1
1. Add a new flashcard
2. Exit
> 3
3 is not  an option

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
> what is the capital of Iran?
Answer:
> Tehran

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: what is the capital of Iran?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> 6
6 is not an option

press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Tehran
press "y" if your answer is correct:
press "n" if your answer is wrong:
>>
 is not an option

press "y" if your answer is correct:
press "n" if your answer is wrong:
>> b
b is not an option

press "y" if your answer is correct:
press "n" if your answer is wrong:
>> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7e424ca3",
   "metadata": {},
   "outputs": [],
   "source": [
    "actual_list = [' ','O',' ']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f6cf74ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shuffle_list(actual_list):\n",
    "\n",
    "    shuffle(actual_list)\n",
    "    \n",
    "    return actual_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a7aafea3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[' ', 'O', ' ']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "actual_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e625f438",
   "metadata": {},
   "outputs": [],
   "source": [
    "shuffle(actual_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c688f74b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['O', ' ', ' ']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "actual_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ecc56f7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_guess():\n",
    "    \n",
    "    guess =''\n",
    "    \n",
    "    while guess not in [\"0\",\"1\",\"2\"]:\n",
    "        \n",
    "        guess = input(\"Pick a Number: 0 1 or 2: \" )\n",
    "        \n",
    "        \n",
    "    return int(guess)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0f94646f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pick a Number: 0 1 or 2: 2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_guess()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bda16680",
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_guess_check(actual_list,guess):\n",
    "    \n",
    "    if actual_list[guess] =='O':\n",
    "        \n",
    "        print(\"Correct! you have guess is Awesome!!\")\n",
    "        \n",
    "    else:\n",
    "        \n",
    "        print(\"Sorry Wrong Guess!! Better Luck Nexttime!!\")\n",
    "        \n",
    "        print(actual_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d2349193",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pick a Number: 0 1 or 2: 2\n",
      "Sorry Wrong Guess!! Better Luck Nexttime!!\n",
      "[' ', 'O', ' ']\n"
     ]
    }
   ],
   "source": [
    "actual_list=[' ','O',' ']\n",
    "\n",
    "shuffled_list = shuffle(actual_list)\n",
    "\n",
    "guess = user_guess()\n",
    "\n",
    "user_guess_check(actual_list,guess)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

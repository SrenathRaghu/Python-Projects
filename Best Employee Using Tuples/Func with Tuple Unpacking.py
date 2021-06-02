{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "49a6ec8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Employee_List = [('Srenath',310),('Vijay',320),('Sundu',300)]\n",
    "\n",
    "\n",
    "def best_emp(Employee_List):\n",
    "    \n",
    "    curr_hours = 0\n",
    "    \n",
    "    emp_of_month = ''\n",
    "    \n",
    "    \n",
    "    for emp_name,hours in Employee_List:\n",
    "        \n",
    "        if hours > curr_hours:\n",
    "            \n",
    "            curr_hours = hours\n",
    "            \n",
    "            emp_of_month = emp_name\n",
    "            \n",
    "        else:\n",
    "            \n",
    "            pass\n",
    "        \n",
    "        \n",
    "        \n",
    "    return (emp_of_month,curr_hours)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "158b6632",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Vijay', 320)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_emp(Employee_List)"
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

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[34, 6, 78, 4]\n"
     ]
    }
   ],
   "source": [
    "lst = [34,5,6,78,89,4]\n",
    "result = list(filter(lambda x:x%2==0,lst))\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[34, 6, 78, 4]\n",
      "34\n",
      "6\n",
      "78\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "lst = [34,5,6,78,89,4]\n",
    "result = list(filter(lambda x:x%2==0,lst))\n",
    "print(result)\n",
    "for i in result : print (i)\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

#!/usr/bin/env python
# coding=utf-8

def meetALovelyGirl(walk):
    if walk =='yes':
        print """
        You find a lovely girl in front of You.
        She has a water shine black eyes.
        In a yellow dress.
        A cute and  naive face.
        What a beautiful girl she is.
        You are crashed into her.
        What do you do?
        """
        des = makeDecision()
    else:
        print """
        When you are going to apartment.
        You meet a girl with cute face in a blue dress.
        She is so nice that you cannot move you sight away her.
        What do you do?
        """
        des = makeDecision()

    return des

def makeDecision():

    decision = raw_input('1 talk with her, 2 avoid to eye contact, 3 say love to her >')
    result = []

    if decision == '1':
        print """
        you make a friend with her. She is single and you can persue her.
        """
        result.append('you make a friend')
    elif decision == '2':
        print """
        You lost the chance to get  a girl, pitty, do not be shame next time.
        """
        result.append('lost a girl')

    elif decision == '3':
        print """
        She reject  you, you are too hugerry.
        """
        result.append('rejected')

    else:
        print """
        No way to do that.
        """
        result.append(makeDecision())
    
    return result.pop()


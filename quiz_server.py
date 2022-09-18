import socket
from threading import Thread
import random
from tkinter.messagebox import QUESTION
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000
server.bind((ip_address,port))
server.listen()
list_of_clients=[]
questions=[
    "what is the italian name of PIE? \n a.mozzerala\nb.pastry\nc.patty\nd.pizza",
    "who is loki?\na.god of thunder\nb.god of dwarves\nc.god of mischeif\nd.god of gods",
    "how many wonders are there in our earth\n a.5\nb.6\nc.7\nd.8",
    "which planet is closest to the sun\na.mercury\nb.earth\nc.venus\nd.jupiter"
]
answers=[
    'd','c','c','a'
]
print("server has started")
remove=questions
def get_random_question(conn):
    random_index=random.randint(0,len(questions)-1)
    random_questions=questions[random_index]
    random_answers=answers[random_index]
    conn.send(random_questions.encode('utf-8'))
    return random_index,random_questions,random_answers

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientThread(conn):
    score=0
    conn.send("welcome to quiz game".encode('utf-8'))
    conn.send("you will a recieve questions".encode('utf-8'))
    conn.send("good luck\n\n".encode('utf-8'))
    index, questions, answers=get_random_question(conn)
    while True:
        try:
            message=conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                 score += 1
                 conn.send(f"BRAVO! YOUR SCORE IS {score}\n\n".encode('utf-8'))
                else:
                   conn.send("INCORRECT BETTER LUCK NEXT TIME\n\n".encode('utf-8'))
                   remove_question(index)
                   index ,question,answer=get_random_question(conn)
            else:
              remove(conn)
        except:
            continue








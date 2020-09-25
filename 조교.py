import asyncio
import discord
import time
import random
global team_score
team_score = [["1조",0],["2조",0],["3조",0],["4조",0]]
client = discord.Client()

@client.event
async def on_ready():
  print("------------")
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------")


@client.event
async def on_message(message):
  if message.content.startswith("!안녕"):
    channel = message.channel
    await channel.send("안녕하세요")

  if message.content.startswith("!조별 점수"):
    channel = message.channel
    for i in range(1, 5):
      await channel.send(str(i)+"조 "+str(team_score[i-1][1])+"점")

  if message.content.startswith("!타이머 "):
    channel = message.channel
    Text = ""
    learn = message.content.split(" ")
    vrsize = len(learn)  # 배열크기
    vrsize = int(vrsize)
    for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
      Text = Text + " " + learn[i]
    sec = int(Text)
    for i in range(sec, 0, -1):
      await channel.send("타이머 작동중 : "+str(i)+"초")
      time.sleep(0.9)
    else:
      await channel.send("타이머 종료!")

  if message.content.startswith("!조 "):
    channel = message.channel
    learn = message.content.split(" ")
    team_score[int(learn[1])-1][1]+=int(learn[2])
    await channel.send("조별 점수입니다.")
    for i in range(1, 5):
      await channel.send(str(i)+"조 "+str(team_score[i-1][1])+"점")

  if message.content.startswith("!점수 초기화"):
    channel = message.channel
    for i in range(1, 5):
      team_score[i-1][1]=0
    await channel.send("조별 점수 초기화 완료!")

  if message.content.startswith("!벌칙"):
    channel = message.channel
    menu = ['방에서 제일 큰 물건 찍어오기','비밀 한 개 말하기','TMI 하나 말하기', '10분동안 패딩입고 있기', '눈동자로 이름쓰기', '콧구멍으로 이름쓰기', '방에 있는 물건으로 하트 만들기']
    await channel.send(random.choice(menu))
  
client.run(token)


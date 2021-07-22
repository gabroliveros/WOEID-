#
# ^^* WOEID? *^^
#
# Por: Gabriel Oliveros
#=========================

import tweepy

# Cadenas de autenticación (indica tus propias claves)
consumer_key= '' 
consumer_secret= ''
access_token= ''
access_token_secret= ''

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# llamadas a la API
api= tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

trends= api.trends_available()

lugares= {}
for t in trends:
  nom,con,val= '','',''
  for k,v in t.items():
      if k == 'name':
          nom= v
      elif k == 'country':
          con= v
      elif k == 'woeid':
          val= v
  if con != 'Venezuela':  #Sustituye por el país de tu preferencia
      continue
  else:
      lugares[nom]= val
print()

print('Hay {} WOEIDs identificados en Venezuela'.format(len(lugares)))
print(lugares)   

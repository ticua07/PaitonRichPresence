from pypresence import Presence
import time

"""
You need to upload your image(s) here:
https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
"""

client_id = "743550752437567511"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

# Make sure you are using the same name that you used when uploading the image
print(RPC.update(state="Aplastando bugs",
    details="Programando solo",
    large_image="python",
    large_text="Paiton",
    ))

while 1:
    time.sleep(15) #Can only update presence every 15 seconds

from telethon import TelegramClient, events, sync


api_id = 11111111 # api_id
api_hash = 'api hash'



client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if '.d' in event.raw_text:
        await event.edit("d")
        await event.edit("")
        await event.edit("a")
        await event.edit("")
        await event.edit("r")
        await event.edit("")
        await event.edit("k")
        await event.edit("")
        await event.edit("n")


    elif '.a' in event.raw_text:
        await event.edit("S|")
        await event.edit("Sa|")
        await event.edit("Sal|")
        await event.edit("Salo|")
        await event.edit("Salom")
        await event.edit("Salom")
        await event.edit("Salom")
        await event.edit("╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X X║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝")

    elif '.ddx' in event.raw_text:
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("Tugadi...")
        


    
    elif '.ddos' in event.raw_text:
        await event.edit("seach:ip")
        await event.edit("seach:ip")
        await event.edit("seach:ip")
        await event.edit("ip:102,12,23,33")
        await event.edit("ip:102,12,23,33")
        await event.edit("Start:DDoS")
        await event.edit("Start:DDoS")
        await event.edit("finish DDoS")
        await event.edit("hacked")



    elif '.disko' in event.raw_text:
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")

    
    elif '.caput' in event.raw_text:
        await event.edit("✈️")
        await event.edit("ㅤ✈️")
        await event.edit("ㅤㅤ✈️")
        await event.edit("ㅤㅤ🛩")
        await event.edit("ㅤ🛩")
        await event.edit("🛩")
        await event.edit("💥")





	



client.start()
client.run_until_disconnected()

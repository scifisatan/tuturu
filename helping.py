BASE_PAT = "assign/"


def getPat(message):
    return BASE_PAT + str(message.channel.guild.id) + ".txt"

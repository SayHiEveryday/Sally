# List of all commands

**Permission = 0 is any user can use it**

**Type = prefix only or slash only or both (p & s)**

## Fun

|              Commands             |                                          description                                         |    Type    | Default Permission |
| :-------------------------------: | :------------------------------------------------------------------------------------------: | :--------: | :----------------: |
|                help               |                                      Bring up help menu                                      |    p & s   |          0         |
|         8ball \[question]         |                Stuck with something? just use 8ball! help decide your question               |    p & s   |          0         |
|            kill \[user]           |                 Hate someone? just kill them! (we do not support any volient)                |    p & s   |          0         |
|           cuddle \[user]          |                                  Like someone? cuddle them!                                  |    p & s   |          0         |
|            slap \[user]           |                  Dislike someone? slap them! (we do not support any volient)                 |    p & s   |          0         |
|            pat \[user]            |                                 Someone being cute? pat them!                                |    p & s   |          0         |
| fakemod \[user]\[reason]\[action] |                                        Fake Moderation                                       | slash only |          0         |
|            gay \[user]            |                            Feeling like someone is gay? Test them!                           |    p & s   |          0         |
|            hug \[user]            |                                 Someone being cute? hug them!                                |    p & s   |          0         |
|            pout \[user]           |                                         Send pout gif                                        |    p & s   |          0         |
|            kiss \[user]           |                             Have feeling with someone? kiss them!                            |    p & s   |          0         |
|         stealnitro \[user]        |                          Being poor? just steal other people nitro!                          |    p & s   |          0         |
|           history today           |                      Show what happened today in history today date(UTC)                     | slash only |          0         |
|   history thatday \[month]\[day]  | Show what happened today in history You can input a month and day to get history of that day | slash only |          0         |
|           urban \[word]           |                                    Search urban dictionary                                   | slash only |          0         |
|           rps \[choice]           |                               Play rock paper scissor with bot                               | slash only |          0         |

## Misc

|           Commands          |            description            |     Type    | Default Permission |
| :-------------------------: | :-------------------------------: | :---------: | :----------------: |
| get\_profile \[user]\[type] |  Get profile of mentioned member  |  Slash only |          0         |
|        avatar \[user]       |   View mentioned member's avatar  | prefix only |          0         |
|        banner \[user]       |   View mentioned member's banner  | prefix only |          0         |
|        whois \[user]        | Show basic info of mentioned user |    p & s    |          0         |
|          guildinfo          |     Get info of current guild     |    p & s    |          0         |
|          emojisteal         |        Steal inputed emoji        | prefix only |          0         |
|     role \[user]\[role]     |     add role to mentioned user    |    p & s    |     manage role    |

## Bot related

|            Commands           |    description    |  Type | Default Permission |
| :---------------------------: | :---------------: | :---: | :----------------: |
|              ping             |  Check bot's ping | p & s |          0         |
| change\_prefix \[new\_prefix] | Change bot prefix | p & s |    Administrator   |

## Moderation

|           Commands           |               description               |  Type | Default Permission |
| :--------------------------: | :-------------------------------------: | :---: | :----------------: |
|        purge \[amount]       | Delete message in the channel by amount | p & s |   Manage\_message  |
|     kick \[user]\[reason]    |          Kick mentioned member          | p & s |    Kick\_members   |
|     Ban \[user]\[reason]     |           Ban mentioned member          | p & s |    Ban\_Members    |
| nick set \[user]\[new\_nick] |   Set a nickname for mentioned member   | p & s |  Manage\_Nicknames |
|      nick clear \[user]      |  clear a nickname for mentioned member  | p & s |    Ban\_Members    |

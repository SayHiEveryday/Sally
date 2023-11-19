import random , platform , socket , re , uuid , json , psutil , logging , datetime , json , requests

def urban(term):
    return json.loads(requests.get(f'https://api.urbandictionary.com/v0/define?term={term}').text)['list'][0]

def today():
    today = datetime.datetime.utcnow()
    date = today.strftime('%m/%d')
    return json.loads(requests.get(url=f'https://today.zenquotes.io/api/{date}').text)["data"]["Events"][random.randint(0,20)]

def thatday(month,day):
    return json.loads(requests.get(url=f'https://today.zenquotes.io/api/{month}/{day}').text)["data"]["Events"][random.randint(0,20)]

def get_prefix(bot , guild):

    with open("prefix.json" , "r") as f:
        prefix = json.load(f)
    
    return prefix[str(guild.id)]


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def rammore(get):
    return "https://rra.ram.moe" + json.loads(requests.get(f"https://rra.ram.moe/i/r?type={get}").text)['path']

def quote():
    return json.loads(requests.get("https://api.api-ninjas.com/v1/quotes", headers={'X-Api-Key': 'o6LhjnbOakeH6tKXMZ1OJA==jXuveAbMmClLIYDX'}).text)

answer = [
    "Indeed",
    "Absolutely",
    "of course",
    "Certainly",
    "Naturally",
    "Yup",
    "Okay",
    "Negative",
    "Nope",
    "Not at all",
    "Never",
    "No way"
]


kill = [
    "$author after a long day, plops down on the couch with $mention and turns on The Big Bang Theory. After a Sheldon Cooper joke, $mention laughs uncontrollably as they die.",
    "$author Alt+F4'd $mention.exe!",
    "$author attempted to play a flute, exploding the head of $mention.",
    "$author blew his ear drums out listening to music too hard.",
    "$author challenges $mention to a fist fight to the death. $mention wins.",
    "$author cleaves the head of $mention with a keyboard.",
    "$author crushes $mention with a fridge.",
    "$author decapitates $mention with a sword.",
    "$author drags $mentions ears too hard and rips them off.",
    "$author drowns $mention in a beer barrel.",
    "$author drowns $mention in a tub of hot chocolate. *How was your last drink?*",
    "$author eviscerates $mention with a rusty butter knife. Ouch!",
    "$author feeds toothpaste-filled oreos to $mention, who were apparently allergic to fluorine. GGWP.",
    "$author fell in love with $mention then broke his heart literally.",
    "$author fires a supersonic frozen turkey at $mention, killing them instantly.",
    "$author forgot to leave the car door window open and $mention dies from overheating",
    "$author forgot to zombie-proof $mention lawn... Looks like zombies had a feast last night.",
    "$author gets $mention to watch anime with them. $mention couldn't handle it.",
    "$author grabs $mention and shoves them into an auto-freeze machine with some juice and sets the temperature to 100 Kelvin, creating human ice pops.",
    "$author hired me to kill you, but I don't want to! $mention",
    "$author hugs $mention too hard..",
    "$author hulk smashes $mention into a pulp.",
    "$author killed $mention by ripping the skin off of their face and making a mask out of it.",
    "$author kills $mention after hours of torture.",
    "$author kills $mention with a candlestick in the study",
    "$author kills $mention with kindness",
    "$author kills $mention with their own foot.",
    "$author murders $mention with an axe.",
    "$author pressed delete. It deleted $mention",
    "$author pushes $mention into the cold vacuum of space.",
    "$author runs $mention over with a PT Cruiser.",
    "$author shoots $mention in the head.",
    "$author shoots in $mention mouth with rainbow laser, causing $mention head to explode with rainbows and $mention is reborn as unicorn. :unicorn:",
    "$author shot $mention using the Starkiller Base!",
    "$author slips bleach into $mention's lemonade.",
    "$author strangles $mention.",
    "$author straps $mention to an ICBM and sends them to North Korea along with it.",
    "$author strikes $mention with the killing curse... *Avada Kedavra!*",
    "$author tears off $mentions lips after a kiss.",
    "$author thicc and collapses $mention's rib cage",
    "$author tries to shoot the broad side of a barn, misses and hits $mention instead.",
    "$author turns on Goosebumps(2015 film) on the TV. $mention being a scaredy-cat, dies of an heart attack.",
    "$author was so swag that $mention died due to it. #Swag",
    "$author, are you sure you want to kill $mention? They seem nice to me.",
    "$mention accidentally tripped and died while getting up to write their suicide note.",
    "$mention ate a piece of exotic butter. It was so amazing that it killed them.",
    "$mention ate an apple and turned out it was made out of wax. Someone died from wax poisoning later that day.",
    "$mention ate too many laxatives and drowned in their own shit. Ew.",
    "$mention bought a fidget spinner and drowned in pussy.",
    "$mention can't be killed, as they are a ghost.",
    "$mention chokes in a trash can.",
    "$mention chokes on a chicken bone.",
    "$mention chokes on cheerios and dies. What an idiot...",
    "$mention cranks up the music system only to realize the volume was at max and the song playing was Baby by Justin Beiber...",
    "$mention cums in eye, goes blind, runs for help but ran straight onto train tracks and gets plowed by a train.",
    "$mention decided it was a good idea to fight a tiger while smelling like meat. It did not end well.",
    "$mention did not make a meme dank enough and was stoned.",
    "$mention died after fapping 50 times in a row with no break.",
    "$mention died after gaming for 90 hours straight without moving or eating.",
    "$mention died after playing with an edgy razor blade fidget spinner.",
    "$mention died after realizing how shitty their grammar was",
    "$mention died after trying to out-meme Dank Memer.",
    "$mention died an honorable death. Death by snoo snoo.",
    "$mention died because RemindMeBot forgot to remind them to breathe",
    "$mention died because they started playing with a fidget spinner but they realise its 2016 so you start fapping to the old witch in snow white and obama starts mowing their lawn and they jump out of the window and get ripped to pieces by Obama's lawn mower",
    "$mention died due to $author being so stupid",
    "$mention died due to eating WAY too many hotdogs in preparation for their date Friday night.",
    "$mention died eating expired and infected raw fish with the filthiest rice in the world as sushi while being constantly stabbed in the scrotum with a 9inch nail sharp enough to stab through kevlar. The soy sauce was cat piss.",
    "$mention died from a high salt intake",
    "$mention died from a swift kick to the brain.",
    "$mention died from a tragic amount of bad succ",
    "$mention died from doing the ice bucket challenge.",
    "$mention died from drinking too much water Huh, I guess it IS possible!.",
    "$mention died from eating cactus needles.",
    "$mention died from eating too much ass.",
    "$mention died from eating too much bread :/",
    "$mention died from ebola.",
    "$mention died from meme underdose :/",
    "$mention died from not eating enough ass.",
    "$mention died from not whacking it enough. (There's a healthy balance, boys)",
    "$mention died from reposting in the wrong neighborhood",
    "$mention died from shitting for 36 hours straight.",
    "$mention died from swallowing rocks too fast",
    "$mention died from too many sunburns.",
    "$mention died from whacking it too much. (There's a healthy balance, boys)",
    "$mention died of oversucc",
    "$mention died when testing a hydrogen bomb. There is nothing left to bury.",
    "$mention died while listening to 'It's every day bro'",
    "$mention died while playing hopscotch on *seemingly* deactivated land mines.",
    "$mention died while trying to find the city of England",
    "$mention died. OOF",
    "$mention dies after swallowing a toothpick.",
    "$mention dies at the hands of $author.",
    "$mention dies because they used a bobby pin to lift their eyelashes",
    "$mention dies because they were just too angry.",
    "$mention dies by swearing on a Christian Minecraft server",
    "$mention dies due to lack of friends.",
    "$mention dies from bad succ.",
    "$mention dies from dabbing too hard.",
    "$mention dies from dabbing too hard",
    "$mention dies from disrespecting wahmen.",
    "$mention dies from just being a bad, un-likeable dude.",
    "$mention dies from posting normie memes.",
    "$mention dies from severe dislike of sand. It's coarse and rough and irritating it gets everywhere",
    "$mention dies from watching the emoji movie and enjoying it.",
    "$mention dies in a horrible accident, and it was engineered by $author.",
    "$mention dies north of the wall and transforms into a white walker",
    "$mention dies of AIDS.",
    "$mention dies of dysentery.",
    "$mention dies of natural causes.",
    "$mention dies of starvation.",
    "$mention dies on death row via lethal injection after murdering $author and their family.",
    "$mention dies, but don't let this distract you from the fact that in 1998, The Undertaker threw Mankind off Hell In A Cell, and plummeted 16 ft through an announcer’s table",
    "$mention dies.", "After a struggle, $mention kills $author",
    "$mention disappeared from the universe.",
    "$mention drank some toxic soda before it was recalled.",
    "$mention dropped a Nokia phone on their face and split their skull.",
    "$mention drowned in their own tears.",
    "$mention eats too much copypasta and explodes",
    "$mention fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:",
    "$mention fell into a pit of angry feminists.",
    "$mention gets hit by a car.",
    "$mention gets stabbed by $author",
    "$mention gets struck by lightning.",
    "$mention goes genocide and Sans totally dunks $mention!",
    "$mention got into a knife fight with the pope. One of them is in hell now.",
    "$mention got stepped on by an elephant.", "$mention died from eating too much ass.",
    "$mention has a stroke after a sad miserable existence. They are then devoured by their ample cats.",
    "$mention has been found guilty, time for their execution!",
    "$mention has some bad chinese food, and pays the ultimate price.",
    "$mention is abducted by aliens, and the government kills them to cover it up.",
    "$mention is dead at the hands of $author.",
    "$mention is injected with chocolate syrup, which mutates them into a person made out of chocolate. While doing a part-time job at the Daycare, they are devoured by the hungry babies. :chocolate_bar:",
    "$mention is killed by a rabbit with a vicious streak a mile wide",
    "$mention is killed by their own stupidity.",
    "$mention is killed in a robbery gone wrong.",
    "$mention is not able to be killed. Oh, wait, no, $author kills them anyway.",
    "$mention is so dumb that they choked on oxygen.",
    "$mention is stuffed into a suit by Freddy on their night guard duty. Oh, not those animatronics again!",
    "$mention is sucked into Minecraft. $mention, being a noob at the so called Real-Life Minecraft faces the Game Over screen.",
    "$mention killed themselves after seeing the normie memes that $author posts.",
    "$mention kills themselves after realizing how dumb $author is.",
    "$mention lives, despite $author's murder attempt.",
    "$mention loses the will to live",
    "$mention presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death. Moral of the story: Don't go around pressing random buttons.",
    "$mention reads memes till they die.",
    "$mention ripped his heart out..",
    "$mention ripped their own heart out to show their love for $author.",
    "$mention slipped in the bathroom and choked on the shower curtain.",
    "$mention slips on a banana peel and falls down the stairs.",
    "$mention spins a fidget spinner and when it stops he dies...",
    "$mention steps on a george foreman and dies of waffle foot.",
    "$mention takes an arrow to the knee. And everywhere else.",
    "$mention talked back to mods and got destroyed by the ban hammer.",
    "$mention tips his fedora too far and falls onto the tracks of an oncoming subway.",
    "$mention tried to get crafty, but they accidentally cut themselves with the scissors.:scissors:",
    "$mention tried to get famous on YouTube by live-streaming something dumb. Skydiving while chained to a fridge.",
    "$mention tried to outrun a train, the train won.",
    "$mention tried to pick out the holy grail. He chose... poorly.",
    "$mention tried to play in the street...",
    "$mention trips over his own shoe laces and dies.",
    "$mention vocally opposed the Clintons and then suddenly disappeared.",
    "$mention was a resident of Alderaan before Darth Vader destroyed the planet...",
    "$mention was accused of stealing Neptune's crown...",
    "$mention was charging their Samsung Galaxy Note 7...",
    "$mention was eaten alive by ants",
    "$mention was given a chance to synthesize element 119 (Ununennium) and have it named after them, but they messed up. R.I.P.",
    "$mention was killed by $author with baby wipes.",
    "$mention was murdered by $author and everyone knows it, but there is no proof.",
    "$mention was scooped by $author and their innards are now Ennard.",
    "$mention was teleported to the timeline where Jurassic World was real and they were eaten alive by the Indominus Rex.",
    "$mention was thrown in the crusher of a trash truck by $author.",
    "$mention was walking normally when out of the corner of their eye they saw someone do a bottle flip and dab causing $mention to have a stroke.",
    "$mention watched the Emoji Movie and died of sheer cringe.",
    "$mention went on a ride with a lead balloon.",
    "After getting pushed into the ocean by $author, $mention is eaten by a shark.",
    "After raid of roblox kids entered the server, $mention died of cancer.",
    "Aids, $mention died from aids.",
    "Calling upon the divine powers, $author smites $mention and their heathen ways",
    "In a sudden turn of events, I **don't** kill $mention.",
    "no u",
    "Our lord and savior Gaben strikes $mention with a lighting bolt.",
    "Sorry, $author, I don't like killing people.",
    "The bullet missed Harambe and hit $mention instead. Yay for Harambe!",
    "While performing colonoscopy on an elephant, $mention gets their head stuck in the elephants rectum and chokes."
    
]


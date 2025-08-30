# Install first:
# pip install telethon

import random
import time
from telethon import TelegramClient

# Your API credentials
api_id = 21169204
api_hash = 'f643acf583e871ffb4fb2fe952fa03a5'
phone = '+13412425375'

# Group username or ID
target = 't.me/chatter'  # You can also use group ID

# A sample list of random phrases
messages = [
    "What's up, fam?",
    "Just chilling 😎",
    "Bruh moment!",
    "Life’s good, stay positive!",
    "Coffee solves 90% of problems ☕",
    "Anyone gaming tonight?",
    "No cap, that's wild!",
    "Let’s get it 🔥",
    "LOL, that’s hilarious!",
    "Keep grinding 💪","Bro woke up and chose chaos", "Nah fam this wild", "Who even asked?", "Touch some grass", "Skill issue fr", "Main character vibes", "NPC energy detected", "Certified hood classic", "On god fr", "Stay mad lol", 
"Ratio incoming", "Delulu is the solulu", "Nah fam cooked", "Bruh sound effect #2", "Bro built like a side quest", "Go outside bro", "Sigma grindset vibes", "Bro thinks he’s him", "He is NOT him", "Clown spotted", 
"Goofy ahh moment", "Mid at best", "Peak content", "This goes hard", "We move", "Bro sweating fr", "Top G energy", "This ain’t it chief", "Bro lagging", "Bro tweaking rn", 
"Insert coin to continue", "Respawn in 5", "NPC dialogue moment", "Side quest energy", "Bro cooking something", "This is peak comedy", "Get gud scrub", "Bro fell off", "Rizz level 0", "Certified L", 
"Touch sunlight challenge", "Skill diff moment", "Stay hydrated king", "Massive W", "Bro afk", "Straight fax", "No printer", "Cold take", "Hot take", "Spicy take", 
"Bro praying rn", "This is wild behavior", "Nah fam tripping", "Crying in the club rn", "Bro farming karma", "This is not the vibe", "Man down", "He folded", "Bro vanished", "Alt+F4 energy", 
"NPC spotted", "Bro side questing", "Big yikes", "Bro scheming", "He cooking", "Nah man built like a filler arc", "Plot armor vibes", "Boss fight incoming", "Perma ban vibes", "Bro needs a patch update", 
"Cheat codes detected", "Respawn time activated", "Nah this scripted", "Overpowered NPC", "Giga Chad moment", "Beta male arc", "Alpha energy", "This is canon now", "He’s cracked", "Bro off cooldown", 
"Patch notes coming soon", "Loot box moment", "This is RNG diff", "Side mob energy", "Grind never stops", "Insert dramatic music", "Nah man caught in 4k", "Discord mod energy", "Bro speaking facts", "Copium overdose", 
"Goofy level 9000", "Main quest completed", "He’s level 99", "Bro softlocked", "Nah man’s glitched", "Speedrun any%", "Hardstuck vibes", "Bro camping spawn", "Ranked mode activated", "This is free elo", 
"Casual enjoyer vibes", "Sweaty lobby moment", "Nah man smurfing", "Toxic teammate energy", "Mute him", "Kick from lobby", "Queue dodging detected", "Duo queue moment", "Solo carry incoming", "Bro low HP", 
"HP critical warning", "Mana low vibes", "Nah man cooldowns ready", "Respawn in 10", "Tower diving moment", "AFK farming", "Meta pick detected", "Off-meta hero vibes", "Bro one trick pony", "Rank decay incoming", 
"Prestige level flex", "Skin collector vibes", "Default skin detected", "P2W moment", "Bro broke", "Steam sale addict", "Free trial vibes", "Nah man uninstalled", "Reinstalled instantly", "Nah bro alt account", 
"Second monitor flex", "RGB keyboard enjoyer", "Caffeine addiction detected", "Bro cracked out", "Sleep deprived arc", "Energy drink buff active", "Cozy gamer vibes", "Gamer chair supremacy", "Potato PC detected", "Overclocked PC moment", 
"Blue light glasses buff", "Nah man’s frame rate tanking", "Server maintenance moment", "Patch day vibes", "Streamer RNG luck", "Chat spam detected", "Sub only mode", "Twitch mod arc", "YouTube comment war", "TikTok doomscroll moment", 
"Instagram story flex", "Twitter/X rant arc", "Facebook boomer vibes", "Discord VC chaos", "Server muted moment", "Bot farm detected", "Nah bro ratio’d", "Bro farming likes", "Algorithm blessed him", "Shadowban arc", 
"Trending page moment", "Nah fam viral", "For You Page vibes", "Hashtag spam detected", "Influencer cringe", "Clout chasing moment", "Simp alert", "Beta orbiters spotted", "Giga Chad spotted", "Sigma approved", 
"NPC rizz levels", "Charisma stat 0", "Luck stat maxed", "Bro’s RNG insane", "Nah bro cursed", "Blessed run", "First try vibes", "Retry mission", "Checkpoint reached", "Cutscene skip incoming", 
"Final boss vibes", "Mini boss energy", "Side mob moment", "XP farm detected", "Skill tree unlocked", "Talent tree maxed", "Crafting simulator arc", "Inventory full warning", "Encumbrance detected", "Quest failed", 
"Mission successful", "Achievement unlocked", "100% completionist vibes", "Bro’s DLC installed", "Expansion pack vibes", "Nah man beta tester", "Early access moment", "Launch day chaos", "Server queues maxed", "Patch notes incoming", 
"Dev update vibes", "Roadmap promises", "Kickstarter backer energy", "Indie game enjoyer", "Triple A game hate", "Retro nostalgia moment", "Pixel art supremacy", "Nah man speedrunning IRL", "Any% glitchless run", "Tool assisted speedrun", 
"Frame perfect execution", "World record pace", "Nah man throwing", "Choke artist moment", "Clutch king energy", "Bro’s RNG insane", "Critical hit incoming", "Low roll vibes", "D20 failed", "Nah man nat 20", 
"DM laughing rn", "Roleplay cringe detected", "Tabletop gamer arc", "Board game supremacy", "Uno reverse card moment", "Nah man stacking +4s", "Draw 25 vibes", "Monopoly rage quit", "Checkmate moment", "Nah man stalemate", 
"Queen sacrifice energy", "Pawn promotion flex", "ELO diff", "Chess.com ban incoming", "Stockfish vibes", "Opening prep moment", "Endgame study enjoyer", "Gambit lover arc", "Nah man blundering", "Mate in 3 vibes", 
"Overtime clutch moment", "Sudden death vibes", "Nah man overtime IRL", "Extra life buff", "1UP moment", "Continue screen countdown", "Nah man game over", "Credits roll vibes", "Secret ending unlocked", "True ending moment", 
"Bad ending vibes", "Neutral ending arc", "Good ending secured", "Speedrun credits skip", "Skip intro vibes", "Modded game chaos", "Cheat engine moment", "God mode activated", "No clip vibes", "Wallhack detected", 
"Aimbot energy", "ESP wallhack vibes", "VAC ban incoming", "Report him", "Nah bro rage hacking", "Lag switch moment", "Packet loss vibes", "Ping spike incoming", "Server desync detected", "Rubber banding arc", 
"Connection lost moment", "Reconnect in 5", "Lobby disbanded", "Nah bro rage quit", "Alt account grinding", "Boosting vibes", "Smurf detected", "Placement matches incoming", "Promo series vibes", "Ranked anxiety arc", 
"Matchmaking diff", "MMR inflation", "LP gain pain", "Rank reset vibes", "Season end grind", "Battle pass grinder", "Event quest enjoyer", "Loot crate addict", "Skin flex moment", "Legendary drop vibes", 
"Epic rarity moment", "Common loot sadness", "Crafting grind incoming", "Blueprint farm vibes", "Auction house simulator", "Market crash moment", "Economy diff", "Stock market sim IRL", "Crypto crash arc", "NFT rugpull vibes", 
"Web3 enjoyer moment", "Blockchain spam detected", "Gas fees pain", "Bro’s portfolio tanked", "Buy the dip vibes", "HODL energy", "Lambo dreams arc", "Nah bro rekt", "Paper hands moment", "Diamond hands flex", 
"Meme coin vibes", "Dogecoin to the moon", "Shiba Inu investor arc", "Pump and dump detected", "Influencer shill moment", "Discord alpha leaks", "Telegram group chaos", "Reddit DD vibes", "WSB nostalgia arc", "Stonk go brrr", 
"Economic downturn moment", "Recession vibes", "Inflation arc", "Layoff speedrun", "Side hustle activated", "Freelancer arc", "Gig economy enjoyer", "Uber driver main quest", "DoorDash NPC vibes", "Fiverr grindset moment", 
"LinkedIn cringe detected", "Resume buff incoming", "Networking grindset", "Office NPC energy", "Manager boss fight", "HR side quest", "Team meeting filler episode", "PowerPoint enjoyer", "Excel spreadsheet final boss", "Pivot table arc""Brain empty, vibes only", "Cry about it", "That’s a skill issue", "No thoughts head empty", "Certified clown award", "Zero drip detected", "L take incoming", "Nah, man flopped", "Who invited this guy?", "Touch some air",
"Go outside challenge", "Goofy energy", "Actual menace to society", "Nah, he tweaking", "Chill bro", "NPC dialogue unlocked", "Ratio speedrun", "Nah fam, he cooked", "Bro’s a side quest", "Stay pressed",
"Mid-tier opinion", "Nah bro crying", "Delete app challenge", "Phone storage crying", "Not even surprised", "Bro talking to himself", "Silent character arc", "Main villain energy", "Plot twist moment", "Not canon behavior",
"Red flag factory", "Big walking L", "Low effort moment", "Nah fam lazy", "Meme generator vibes", "Bro tripping", "Keep scrolling", "NPC level rizz", "Man forgot English", "Brain lag detected",
"Bro’s a filler episode", "Lagging IRL", "Nah, that’s cursed", "Cursed image vibes", "Blessed day moment", "Delulu mode active", "Sigma move", "Nah fam, no way", "He folded so quick", "Uninstall yourself",
"Bro out of pocket", "Nah bro, illegal move", "Comedy DLC unlocked", "Beta behavior detected", "Clown emoji energy", "Overthinking speedrun", "Why you mad bro?", "Calm down champ", "Bro’s life is patch notes", "Nah fam NPC questline",
"Moments before disaster", "Emotional damage detected", "Random sidekick vibes", "Villain origin story moment", "Bro running side quests", "Skill issue confirmed", "Goofy ending unlocked", "Nah man panicking", "Touching grass speedrun", "Procrastination king",
"Introvert supremacy", "Nah bro evaporated", "Faded than a hoe", "Nah fam teleported", "AFK IRL moment", "Bro ghosted", "Social battery empty", "Energy low vibes", "Silent observer arc", "Why so quiet bro?",
"Overthinking simulator", "Brain buffering", "Bro’s lagging", "High ping personality", "Error 404 vibes", "Not found energy", "Nah, that’s sus", "Suspicious activity detected", "NPC update needed", "Low IQ detected",
"Brain cell war", "IQ test failed", "Nah fam clueless", "Goofy moment IRL", "NPC eyes", "He’s confused", "Lost in the sauce", "Sauce expired", "Expired vibes", "Nah fam outdated",
"Retro gamer vibes", "Old school moment", "Back in my day vibes", "Boomer energy", "Zoomer chaos", "Gen Alpha incoming", "Bro’s a millennial meme", "Throwback Thursday vibes", "Flashback episode", "Vintage cringe",
"Overrated energy", "Underrated opinion", "Nah fam, underrated", "Peak vibes incoming", "Nah that’s fire", "Certified banger", "Mid vibes detected", "Nah fam overhyped", "Hot garbage alert", "Dumpster fire vibes",
"Keyboard warrior detected", "Nah fam typing essay", "Bro paragraphing", "Nah fam MLA format", "PowerPoint energy", "Spreadsheet enthusiast", "Bro in Excel", "Work from home NPC", "Zoom call vibes", "Mute mic moment",
"Camera off vibes", "Nah fam pretending to listen", "Silent nodding arc", "Teams notification trauma", "Slack pings detected", "Corporate cringe", "Office simulator IRL", "Nah bro 9 to 5", "Overtime unpaid vibes", "Monday boss fight",
"Weekend side quest", "Friday energy boost", "Nah fam Friday night L", "Saturday gamer vibes", "Sunday scaries incoming", "Nah bro stressed", "Deadline speedrun", "Procrastination Olympics", "Sleep deprivation moment", "Coffee addict energy",
"Energy drink speedrun", "Caffeine overdose vibes", "Insomnia DLC unlocked", "Bro not sleeping", "Nah fam awake since 3AM", "No sleep arc", "Power nap failed", "Sleep schedule broken", "Alarm boss fight", "Snooze button spam",
"Phone addiction moment", "Scroll marathon vibes", "Doomscrolling speedrun", "Social media NPC", "TikTok zombie detected", "Reels enjoyer", "YouTube shorts goblin", "Snap streak addict", "Story posting NPC", "Oversharing king",
"DM ghosting energy", "Nah fam left on read", "Delivered not seen vibes", "Typing for 5 mins moment", "Nah fam essay texting", "One-word reply energy", "Dry texter vibes", "Double texting anxiety", "Triple texting clown", "Seen-zoned boss fight",
"Netflix binge vibes", "Series marathon arc", "Anime filler saga", "Manga reader supremacy", "Spoiler king energy", "Nah fam spoiled it", "Plot twist crying", "Season finale moment", "Nah fam cliffhanger", "Next season never",
"Movie buff energy", "Nah fam critic mode", "IMDB review addict", "Rotten Tomatoes vibes", "Letterboxd warrior", "Nah fam one star review", "Cinema enjoyer arc", "Film nerd energy", "Nah fam Oscars time", "Golden Globes vibes",
"Streamer arc", "Nah fam Twitch affiliate", "Subscriber flex moment", "Tier 3 sub energy", "Emote spam detected", "Chat flooded vibes", "Nah fam banned in chat", "VIP badge flex", "Mod power trip", "Stream delay detected",
"Gaming marathon moment", "24-hour stream vibes", "Nah fam no breaks", "Controller drift arc", "Mouse click warrior", "Keyboard combo master", "Nah fam button masher", "Fighting game enjoyer", "Racing sim addict", "FPS sweat",
"Third party detected", "Nah fam camping", "Sniper nest energy", "Respawn simulator", "Killcam moment", "Nah fam one tap", "Ace clutch energy", "Nah fam team wipe", "Final kill cam flex", "Rank grind pain",
"Battle royale vibes", "Circle closing arc", "Nah fam storm chasing", "Loot goblin moment", "Inventory management pro", "Nah fam looted everything", "Revive me bro", "Knocked down vibes", "Reboot card energy", "Victory royale moment",
"Music enjoyer vibes", "Nah fam playlist curator", "Spotify wrapped flex", "Apple Music NPC", "Vinyl enjoyer", "CD collector energy", "Nah fam radio only", "Mixtape drop vibes", "SoundCloud rapper arc", "Lofi beats supremacy",
"Gym bro energy", "Nah fam skipping leg day", "Protein shake addict", "Cardio hater vibes", "Weightlifting enthusiast", "Bro deadlifting his feelings", "Nah fam flexing mirror selfie", "Gym fit check", "PR achieved vibes", "Nah fam maxed out",
"Health arc unlocked", "Nah fam salad eater", "Vegan NPC vibes", "Carnivore diet moment", "Intermittent fasting king", "Keto enjoyer", "Gluten-free arc", "Nah fam tracking macros", "Water gallon flex", "Nah fam meal prep Sunday",
"Pet owner arc", "Nah fam cat person", "Dog lover vibes", "Bird whisperer", "Fish tank simulator", "Reptile enjoyer", "Hamster speedrun", "Pet TikTok creator", "Animal meme enjoyer", "Nah fam pet cam live",
"Travel vlog vibes", "Nah fam wanderlust energy", "Backpacking moment", "Budget airline pain", "Airport boss fight", "Security line speedrun", "Customs NPC encounter", "Jetlag simulator", "Lost luggage vibes", "Nah fam delayed flight",
"Foodie vibes", "Nah fam chef arc", "Michelin star enjoyer", "Fast food NPC", "Street food enthusiast", "Cooking show binge", "Nah fam kitchen disaster", "MasterChef wannabe", "Takeout marathon vibes", "Delivery driver arc",
"Shopping spree vibes", "Nah fam broke after mall", "Cart full moment", "Amazon addict arc", "eBay bargain hunter", "Secondhand treasure vibes", "Vintage drip moment", "Luxury flex vibes", "Budget king energy", "Nah fam coupon hunter",
"Fashion NPC", "Nah fam thrift store king", "Sneakerhead vibes", "Designer drip flex", "Streetwear enthusiast", "OOTD flex moment", "Nah fam fashion week", "Runway model arc", "Bro styling IRL", "Nah fam clashing colors",
"Holiday spirit arc", "Nah fam festive vibes", "Halloween costume NPC", "Thanksgiving feast enjoyer", "Christmas lights boss fight", "New Year resolution clown", "Valentine’s Day loner", "Easter egg hunter", "Nah fam fireworks enjoyer", "Independence Day vibes",
"Back to school energy", "Nah fam homework pain", "Exam anxiety arc", "Pop quiz boss fight", "Teacher’s pet vibes", "Group project L", "Presentation trauma moment", "Science fair enjoyer", "Math Olympiad NPC", "Nah fam detention arc",
"Tech nerd energy", "Nah fam coding in C", "Programmer arc", "StackOverflow warrior", "Nah fam copy-paste master", "Debugging simulator", "Syntax error moment", "Compiler crying", "Hackathon vibes", "Nah fam Linux enjoyer",
]"bruh", "wtf", "lol", "nah", "fr", "bet", "smh", "ngl", "ayo", "yooo", "yo", "nah fam", "deadass", "cap", "no cap", "ok", "ight", "ye", "yup", "sup", "yo bro", "bro", "sis", "fam", "gang", "lit", "fire", "sheesh", "lowkey", "highkey", "mood", "vibe", "facts", "big facts", "bet bet", "valid", "frrr", "word", "tru", "okok", "say less", "on god", "frfr", "bruhhh", "heh", "lmao", "lmfao", "rofl", "crying", "skrrt", "ouch", "yikes", "hm", "huh", "what", "wyd", "hbu", "idk", "idc", "ikr", "omg", "omfg", "wtfff", "dawg", "brooo", "brooooo", "yo fam", "slatt", "drip", "fit", "bop", "sus", "sussy", "im dead", "no shot", "capper", "ok bet", "say no more", "good looks", "respect", "yo bet", "tru dat", "ugh", "oop", "nah bruh", "lolol", "zzz", "nahh", "ayo fam", "flex", "pull up", "we up", "vibin", "mhm", "sheeeesh", "bruh moment", "real talk", "facts only", "100", "keep it 100", "gotchu", "yup yup", "all good", "ight bet", "ok cool", "yo bet", "yea yea", "heard", "aye", "brodie", "homie", "my guy", "gang gang", "fr dawg", "legit", "dang", "yo yo", "big drip", "facts bro", "oof", "big oof", "bruh tf", "crazy", "insane", "weird", "wild", "damn", "yo bet", "bet fam", "bet bro", "aye bet", "yuh", "yo facts", "tbh", "idc fr", "no way", "damn bro", "ayo wtf", "mad", "nah fr", "ok bet fam", "bet say less", "bet brodie", "brodie fr", "gang fr", "nah gang", "word bro", "true that", "ok cool fam", "frfr bro", "ayo bet", "yo word", "gang gang bro", "no lie", "straight up", "dead", "deadass bro", "bet say no more", "cap bro", "no capp", "lit fr", "yo crazy", "omg bruh", "yo wild", "ayo bruh", "yo homie", "mad respect", "much love", "safe", "hold up", "yo hold up", "one sec", "sec", "pause", "nah pause", "stop", "chill", "relax", "calm", "easy", "yo easy", "good looks fam", "heard you", "copy", "copy that", "aye bet bet", "say less bro", "for real", "no way bruh", "crazy fr", "oof bro", "massive oof", "yo fam"

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone=phone)
    while True:
        msg = random.choice(messages)
        await client.send_message(target, msg)
        print(f"Sent: {msg}")
        time.sleep(15)  # wait 15 seconds

with client:
    client.loop.run_until_complete(main())

from pathlib import Path
root=Path('/mnt/data/blab-expanded')
footer='''<footer><div class="wrap"><p>© 2026 BLab. All rights reserved.</p><p>Contact: <a href="mailto:andyboy.ca99@gmail.com">andyboy.ca99@gmail.com</a></p></div></footer>'''
nav='''<nav><div class="wrap"><a class="brand" href="index.html">BLab</a><div class="nav-links"><a href="levels.html">Levels</a><a href="beginner.html">Beginner</a><a href="intermediate.html">Intermediate</a><a href="advanced.html">Advanced</a><a href="varsity.html">Varsity</a><a href="underdog.html">Underdog</a></div></div></nav>'''
def page(title,body,navon=True):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | BLab</title><link rel="stylesheet" href="assets/css/styles.css"></head><body>{nav if navon else ''}{body}{footer}<script src="assets/js/main.js"></script></body></html>'''
def vid(title,desc,id):
    return f'''<article class="video-card"><div class="embed"><iframe src="https://www.youtube.com/embed/{id}" title="{title}" allowfullscreen></iframe></div><div class="video-body"><h3>{title}</h3><p>{desc}</p></div></article>'''
def module(title,items,videos,practice):
    lis=''.join(f'<li>{x}</li>' for x in items)
    vids=''.join(vid(*v) for v in videos)
    checks=''.join(f'<div class="check">✓ {x}</div>' for x in practice)
    return f'''<section class="module-card"><div class="module-head"><div><h3>{title}</h3><ul>{lis}</ul></div><div><p><strong>How to use this module:</strong> Watch each video, take notes on one teaching cue, then try the drill slowly before adding speed.</p><div class="checklist">{checks}</div></div></div><div class="video-grid">{vids}</div></section>'''

# index
index_body='''<main class="hero"><div class="wrap hero-grid"><section><p class="eyebrow">Basketball Learning and Advancement Base</p><h1>Free basketball learning paths for players at every level.</h1><p>BLab helps youth athletes move from their first dribble to competitive basketball through organized skills, IQ, training, recruitment, and leadership resources.</p><a class="btn" href="levels.html">Choose your level</a></section><aside class="panel"><h2>Mission</h2><p>To provide free, structured basketball education for youth athletes regardless of financial background.</p></aside></div></main>'''
(root/'index.html').write_text(page('Home',index_body,False))
levels_body='''<main class="section"><div class="wrap"><p class="eyebrow">Start here</p><h2>What level are you?</h2><div class="levels-grid"><a class="level-card card" href="beginner.html"><span class="dot green"></span><h3>Beginner</h3><p>New players learning fundamentals.</p></a><a class="level-card card" href="intermediate.html"><span class="dot blue"></span><h3>Intermediate</h3><p>House league and school team hopefuls.</p></a><a class="level-card card" href="advanced.html"><span class="dot orange"></span><h3>Advanced</h3><p>Rep, AA/AAA, and serious athletes.</p></a><a class="level-card card" href="varsity.html"><span class="dot red"></span><h3>Varsity</h3><p>High school athletes pursuing opportunities.</p></a></div><p><a class="btn" href="underdog.html">Visit the Underdog Hub</a></p></div></main>'''
(root/'levels.html').write_text(page('Choose Your Level',levels_body))

beginner_modules=[
('Module 1: Ball Control',['How to hold a basketball','Triple threat','Basic dribbling'],[
('Holding the Ball','Learn strong hand placement and control before dribbling or shooting.','A-Jg0BwOYGE'),('Triple Threat Basics','Build the stance that lets you shoot, pass, or drive.','szkISZ7z0XU'),('How to Dribble','Start with simple dribbling mechanics and control.','sQBZE-SkuuI')],['Keep eyes up','Use fingertips','Stay balanced','Practice both hands']),
('Module 2: Scoring and Passing',['Layups','Form shooting','Passing'],[
('Beginner Layups','Break down the steps, footwork, and finish.','d0z7QqblJaM'),('Form Shooting','Build repeatable shooting mechanics close to the rim.','J6_-SaW_GUE'),('Passing and Layup Drill','Use passing movement to create easy finishes.','Tm7N2HU4noQ')],['Make 10 right layups','Make 10 left layups','Hold follow-through','Pass to target hand']),
('Module 3: Defense and Rebounding',['Defensive stance','Footwork','Rebounding'],[
('Youth Defense Drills','Learn simple defensive habits and stance.','XTIfQoI-kEI'),('Basketball Footwork','Improve pivots, balance, and control.','nFNXFc0dvzI'),('Rebounding Fundamentals','Learn how to box out and chase rebounds.','J6QmHTVdKKc')],['Stay low','Slide without crossing feet','Find body first','Go get the ball']),
('Module 4: Playing the Game',['Basic game rules','Spacing','Team play'],[
('Youth Offense Drills','Learn small-sided games that teach team concepts.','9rmqHLkkHpo'),('Spacing and Movement','Understand where to stand and how to move.','m1uWLf6kcDA'),('Pass and Cut','Simple team play using pass, cut, and replace.','LwgIOKvwKNc')],['Know your spots','Cut after passing','Talk on defense','Make the simple play'])]
body='<main class="section"><div class="wrap intro"><p class="eyebrow">Beginner Portal</p><h2>Become comfortable playing organized basketball.</h2><p>For players who have never played, just joined house league, or are learning the fundamentals.</p></div><div class="wrap">'+''.join(module(*m) for m in beginner_modules)+'</div></main>'
(root/'beginner.html').write_text(page('Beginner',body))

intermediate_modules=[
('Skills',['Change of pace','Finishing through contact','Pull-up jumpers'],[
('Change of Pace Dribbling','Learn how to slow down, shift gears, and create separation.','kfFoh94tNlw'),('Finishing Through Contact','Build paint scoring moves that work against defenders.','jR5px_BYd4I'),('Pull-Up Jumpers','Work on stopping on balance into a clean jumper.','bC3kcKO0MnI')],['Change speeds','Protect the ball','Land balanced','Use game pace']),
('Basketball IQ',['Help defense','Pick-and-roll basics','Shot selection'],[
('Help Defense','Learn when and where to help teammates defensively.','O5-zLYkJaN8'),('Pick and Roll Basics','Understand timing, angles, and simple reads.','qvzzv-t_AeA'),('Shot Selection','Learn what makes a shot good, okay, or forced.','kZn5BIoMU0o')],['See ball and man','Call screens','Attack advantage','Avoid rushed shots']),
('Athletic Development',['Speed','Conditioning','Mobility'],[
('Speed and Strength','Build athletic foundations for young basketball players.','PhAXCWAjnU8'),('Agility Training','Improve lateral quickness and multi-direction movement.','TTtZzcOZ7Ic'),('Mobility for Basketball','Recover better and move more freely on court.','F26Lm_qMsNE')],['Warm up first','Sprint with control','Train both sides','Recover properly'])]
body='<main class="section"><div class="wrap intro"><p class="eyebrow">Intermediate Portal</p><h2>Become a strong competitive basketball player.</h2><p>For house league players, lower-level rep players, and school team hopefuls.</p></div><div class="wrap">'+''.join(module(*m) for m in intermediate_modules)+'</div></main>'
(root/'intermediate.html').write_text(page('Intermediate',body))

advanced_modules=[
('Skill Development',['Reads out of ball screens','Advanced finishing','Shooting under pressure'],[
('Ball Screen Reads','Learn how to read ball-screen coverages instead of guessing.','9k4Nr6Y4dHQ'),('Advanced Finishing','Add counters, angles, and paint scoring options.','4qXoGZsfyOU'),('Pressure Shooting','Practice shooting drills that better transfer to games.','lSQEf0iCbM4')],['Read defender','Change angle','Finish off two feet','Shoot while tired']),
('Film Study',['How to watch film','Decision-making','Offensive reads'],[
('Film Study Made Simple','Learn what to look for when reviewing game film.','ftJr8ZTjHlM'),('Read the Defense','Build decision-making through defensive reads.','PaUKMDmj3fU'),('Downhill Decisions','Study choices when attacking closeouts and gaps.','xLAD8hi6-gA')],['Pause and predict','Track mistakes','Write 3 takeaways','Apply next workout']),
('Recruitment Basics',['Highlight tapes','Contacting coaches','Building a player profile'],[
('Highlight Video Basics','Learn what coaches look for in a recruiting video.','9fvRJLLMZSE'),('Contacting Coaches','Learn how to send video so coaches actually watch.','40D-WDkki5M'),('Recruiting Profile','Understand what information should be easy to find.','BCk7gDzNm8E')],['Keep clips short','Show full info','Use real game clips','Be professional'])]
body='<main class="section"><div class="wrap intro"><p class="eyebrow">Advanced Portal</p><h2>Prepare for high-level high school basketball.</h2><p>For rep, AA/AAA, and serious athletes who want sharper skills, film habits, and recruiting basics.</p></div><div class="wrap">'+''.join(module(*m) for m in advanced_modules)+'</div></main>'
(root/'advanced.html').write_text(page('Advanced',body))

varsity_modules=[
('Recruitment Hub',['How recruiting works','OUA','CCAA','NCAA','USPORTS'],[
('Recruiting Explained','Understand the role of highlight videos and coach attention.','9fvRJLLMZSE'),('Send Video to Coaches','Learn how to package and send your clips.','40D-WDkki5M'),('Coach Attention','Understand how long coaches may watch and why your intro matters.','BCk7gDzNm8E')],['Know your target level','Build profile','Email respectfully','Track replies']),
('Training',['Off-season plans','In-season plans','Recovery'],[
('Basketball Strength','Use strength training to support performance.','4yNPdR6e0vg'),('Efficient Training','Train in ways that transfer to game situations.','SsRw7QFkQRM'),('Recovery Methods','Learn recovery habits during the season.','JAStGpAxrc0')],['Plan weeks','Balance skill and strength','Manage fatigue','Sleep consistently']),
('Performance',['Sleep','Nutrition','Injury prevention'],[
('Sleep for Athletes','Learn why sleep matters for performance and recovery.','fybq6V74qRk'),('Recovery Tools','Use sleep, nutrition, and movement for better recovery.','shl33LIF0CE'),('Injury Prevention','Build habits that protect your body over a season.','TVgMs6ZeIPU')],['Hydrate daily','Eat before training','Do mobility work','Report pain early']),
('Leadership',['Becoming a captain','Mentoring younger players','Communication'],[
('Youth Leadership','Learn leadership strategies for young athletes.','KacC-jQ0cos'),('Teamwork and Standards','Understand how strong teams build culture.','87ERqIURGkk'),('Leadership Culture','Learn why team culture affects performance.','7ZPprx42UQE')],['Lead by example','Encourage teammates','Communicate clearly','Serve the team'])]
body='<main class="section"><div class="wrap intro"><p class="eyebrow">Varsity Portal</p><h2>Maximize opportunities beyond high school.</h2><p>For high school varsity athletes pursuing collegiate opportunities and leadership growth.</p></div><div class="wrap">'+''.join(module(*m) for m in varsity_modules)+'</div></main>'
(root/'varsity.html').write_text(page('Varsity',body))

underdog='''<main class="section"><div class="wrap intro"><p class="eyebrow">The Underdog Hub</p><h2>Built for players who are learning without expensive training.</h2><p>Growing up, many players spend hours searching through YouTube videos, forums, and articles trying to figure out how to improve. BLab organizes those resources into one free platform so athletes do not have to navigate that journey alone.</p></div><div class="wrap"><section class="module-card"><h3>Who this is for</h3><ul><li>Players who cannot afford private training</li><li>Players who do not play on elite circuits</li><li>Players with limited gym access</li><li>Self-taught athletes trying to build structure</li></ul><div class="video-grid">'''+vid('At-Home Ball Handling','Build control with limited space and simple equipment.','BqeOaxPg8fo')+vid('Beginner Workout Structure','Use a clear beginner workout progression.','ynkhxHilaKA')+vid('Dynamic Warm-Up','Prepare your body before training.','pfGX3-Dufpc')+'''</div></section></div></main>'''
(root/'underdog.html').write_text(page('Underdog Hub',underdog))

(root/'README.md').write_text('''# BLab Website\n\nOpen `index.html` with Live Server.\n\nStructure:\n- `index.html`: homepage only\n- `levels.html`: level selection\n- `beginner.html`, `intermediate.html`, `advanced.html`, `varsity.html`: expanded portals with embedded YouTube videos\n- `underdog.html`: Underdog Hub\n\nContact footer: andyboy.ca99@gmail.com\n''')

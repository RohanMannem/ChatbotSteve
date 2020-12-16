---
layout: default
title: Final Report
---

<h2>Final Video</h2>
<iframe width="560" height="315" src="https://www.youtube.com/embed/mslOyz09SFg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<h2>Project Summary</h2>
<p> Minecraft is a video game in which players can create and break apart various types of blocks in a 3-dimensional world. Our project, ChatbotSteve, allows 
players to play the game without manually controlling the character’s actions. ChatbotSteve is essentially a messaging platform between the user and the agent, 
Steve. The player can type or dictate his command to the agent, Steve, and Steve will perform the task assigned to him. In order to complete this project, 
we focused on understanding and applying Natural Language Processing (NLP), which would allow us to interpret English player commands in our own way.
</p>

<p>
Our interpretation of player commands relied on defining each word’s part-of-speech, then grouping together pairs of action verbs and direct-object nouns. 
One of the challenges we faced while implementing this was how we could use NLP to tag certain words with a certain part of speech. For example, excluding articles
such as ‘the’, ‘a’, or ‘an’ could potentially change the part-of-speech of a noun to an adjective, producing an incomplete pair of verb action and noun object. 
This incorrect deduction of part-of-speech grouping would then prevent the agent from acting out the correct command or prevent the agent from even 
understanding the command. After we realized this problem, we focused on improving upon our NLP application in such a way that agent, Steve, would be able to 
understand various ways a player could give the same command.
</p>

<p>
Once we created a way for our agent to understand the player, our next step was to code methods which would allow the agent to perform the action desired. 
Our current list of actions ranges from basic commands (walk, jump, crouch, turn) to more complicated ones (find, feed, ride, attack, kill, fish). The basic 
commands were provided by Malmo’s API through the agent.sendCommand() function. One challenge we encountered in implementing these functions was checking 
whether or not Steve had actually finished his task. For example, when commanding “kill the pig”, would Steve be able to attack the pig till it died or would 
it be unable to finish the job if the pig runs away? In order to tackle issues such as these for the more complex commands, we had to access some more 
complicated features of Malmo’s API, such as world_state_observations.
</p>

<h2>Approaches</h2>
<p>
Our approach to understanding human text relies on NLP, natural language processing. The program is split into two main parts. The first one is a reader 
that contains the implementations of the NLP algorithms that understand the user input. The second part is the execution of the actions in the way that the 
user intended to. In the first part, we choose the python dictionary as the container for all the critical information that we get from the user input about 
actions and their corresponding object because of its property of maintaining the insertion order by default. 
</p>

<p>
Before getting started with the reader, we research various NLP algorithms to understand how NLP worked. We found the best method to be splitting the user 
command into a list of tuples. Each tuple would be a pair of the word and that word’s part of speech. Also, in real life, there could be misspelling in the 
users input. To minimize the impact of misspelling and maintain the correctness of our model, we add a light-weight spell checker to the initial user input. 
It’s invented by Dr. Peter Norvig, and it uses probability theory to predict the existence of misspelling. It works by finding the correction c from all 
possible candidate corrections that maximizes the probability that c is the intended correction, given the original word w:
</p>

- argmax c ∈ candidates P(c|w)
- argmax c ∈ candidates P(c) P(w|c) / P(w)  	(by Bayes’ Theorem)
- argmax c ∈ candidates P(c) P(w|c)

<p>
Using NLTK, Natural Language Toolkit, we were able to easily split the user’s commands into the list of tuples, as previously mentioned. A few examples of 
how we are parsing the user command are shown below:
</p>

**Sentence:** I want you to walk<br>
**NLTK:** [('I', 'PRP'), ('want', 'VBP'), ('you', 'PRP'), ('to', 'TO'), ('walk', 'VB')]
 
**Sentence:** I want you to kill 10 skeletons and find one wolf<br>
**NLTK:** [('I', 'PRP'), ('want', 'VBP'), ('you', 'PRP'), ('to', 'TO'), ('kill', 'VB'), ('10', 'CD'), ('skeletons', 'NNS'), ('and', 'CC'), 
('find', 'VB'), ('one', 'CD'), ('wolf', 'NN')]
 
**Sentence:** I want you to kill a pig and find a cow<br>
**NLTK:** [('I', 'PRP'), ('want', 'VBP'), ('you', 'PRP'), ('to', 'TO'), ('kill', 'VB'), ('a', 'DT'), ('pig', 'NN'), ('and', 'CC'), ('find', 'VB'), 
('a', 'DT'), ('cow', 'NN')]<br>

<p>
Using NLTK to tokenize our output into tuples of (word, part of speech), we created commands based on the part of speech (if it is a verb) and pass parameters
based on the word (depending on if it’s a noun or an adjective). Our code also takes numbers into consideration and we will run the command as many times as 
the user wants. To make sure all the numbers can be understood correctly, we include a separate script called “american_number_system” in the helper file to 
effectively convert the numbers from string to numerical type. After numbers are properly handled, our reader then detects the existence of verbs in the input
and extracts the information about the target objects before the next verbs are detected. However, this approach won’t be able to handle all the actions if 
there are pronouns in the user input. The image below shows that we needed to read more than just part-of-speech to be able to derive objects from pronouns 
such as “it”, “them”, etc.
</p>

![](/images/1.png)

<p>
To solve this problem efficiently, our approach was to use “NeuralCoref” - a state-of-the-art coreference resolution based on neural nets and Spacy. 
A few examples of how our parsing works after implementing coreference-understandability:
</p>

**Sentence:** I want you to find a pig and kill it.<br>
**NeuralCoref:** {“find”: [[“pig”, 1]], “kill”: [[“pig”, 1]]}

**Sentence:** I want you to find three pigs, feed two chickens and kill them.<br>
**NeuralCoref:** {“find”: [[“pig”, 3]], “feed”: [[“chicken”, 2]], “kill”: [[“pig”, 3], [“chicken”, 2]]}

<p>
Considering the complexity of this project, we choose a small size model “en_coref_sm.” The doc._.has_coref allows us to detect if there is any 
coreference in the input. If there is, the doc._.coref_resolved function returns the user input after all the coreferences are resolved. The image 
below illustrates that our model achieves the goal of coreference resolution.
</p>



<p>
</p>

<p>
</p>

<p>
</p>

<p>
</p>

<p>
</p>




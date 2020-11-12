---
layout: default 
title: Status 
---

<h4>Status Video:</h4>

[![ChatbotSteve](https://cdn.vox-cdn.com/thumbor/ipajjnzaEyDK1badzdbQ32MSxVI=/0x0:767x431/1200x800/filters:focal(323x155:445x277)/cdn.vox-cdn.com/uploads/chorus_image/image/63226878/0fe20042_0bb8_4781_82f4_7130f928b021.0.jpg)](https://www.youtube.com/watch?v=-h_ab_9RHSw&feature=youtu.be "ChatbotSteve")

Status Video
== 
<iframe width="560" height="315" src="https://www.youtube.com/embed/-h_ab_9RHSw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<h2>Project Summary</h2>
<p>Our main idea for the project is to implement user text/speech recognition to control	the character. We plan to move the agent depending on the user’s command. Our current list of actions ranges from basic commands (walk, jump, crouch, turn) to more complicated ones (find animals/objects, feed/kill them, etc.). In a real time example, typing ‘find the pig’ will command the agent, Steve, to find the closest pig in the spawned world. We can further command Steve to ‘feed the pig’ or ‘kill the pig’. These commands will be implemented to work for all animals/creatures. Furthermore, we implemented the agent to understand compound sentences, allowing Steve to perform more than one action at a time.</p>

<h2>Approach</h2>
<p>Our approach to understanding human text relies on NLP, natural language processing. Before getting started, we research various NLP algorithms in order to understand how NLP really worked. We found the best method to be splitting the user command into a list of tuples. Each tuple would be a pair of the word and that word’s part of speech.<br>
 
Using NLTK, Natural Language Toolkit, we were able to easily split the user’s commands into the list of tuples, as previously mentioned. A few examples of how we are parsing the user command are shown below:<br>
 
**Sentence:** I want you to walk<br>
**NLTK:** [('I', 'PRP'), ('want', 'VBP'), ('you', 'PRP'), ('to', 'TO'), ('walk', 'VB')]
 
**Sentence:** I want you to kill 10 skeletons and find one wolf<br>
**NLTK:** [('I', 'PRP'), ('want', 'VBP'), ('you', 'PRP'), ('to', 'TO'), ('kill', 'VB'), ('10', 'CD'), ('skeletons', 'NNS'), ('and', 'CC'), ('find', 'VB'), ('one', 'CD'), ('wolf', 'NN')]
 
**Sentence:** I want you to kill a pig and find a cow<br>
**NLTK:** [('I', 'PRP'), ('want', 'VBP'), ('you', 'PRP'), ('to', 'TO'), ('kill', 'VB'), ('a', 'DT'), ('pig', 'NN'), ('and', 'CC'), ('find', 'VB'), ('a', 'DT'), ('cow', 'NN')]<br>
 
Using NLTK to tokenize our output into tuples of (word, part of speech), we will create commands based on the part of speech and pass parameters based on the word. Our code also takes numbers into consideration and we will run the command as many times as the user commands.
</p>

<h2>Evaluation Plan</h2>
<h4>Quantitative evaluation</h4>
<p>The first evaluation method is based on quantity. For example, providing a user input as a list of different actions with varying quantities, and we will check how many times that AI can perform the actions/operations in the correct quantity. For example, one of the commands from the user input is “walk 10 and turn 20 and crouch 5 then jump 40.” We will evaluate if these actions were performed the desired amount of times.
</p>
 
<h4>Qualitative evaluation</h4>
<p>Our second evaluation method is based on accuracy. For example, with the same list in the first method. Then we can check whether AI can perform the command, like “find five cows, kill nine pigs and find three cows, and finally jump.” Under the premise that the correct number of operations are executed in the quantitative evaluation, we then checked if all the operations were completed with good quality. For instance, if the AI is executing “kill nine cows”, we evaluate if all the cows are actually killed. If some cows were only attacked by AI and did not die, then this will be regarded as unqualified.
</p>

<h2>Remaining Goals and Challenges</h2>
<p>Right now, our AI can do all basic commands from user input, walk, jump, turn, crouch, attack. We have also implemented our agent to understand quantitative information, for example, walk 10 times and attack 3 times. The goal for the next 4-5 weeks is for the AI to accept complex commands in a compound format, for example, ‘find a pig and kill it’. Our plan is to incorporate the simple commands we already created and incorporate them in other functions in order to accomplish the complex commands. <br>
 
One of our challenges is that the target will keep moving randomly when AI tries to find it. Furthermore, the target will escape or retaliate against the AI after the AI tries to attack them. We hope to address this challenge by making the AI understand when the job is finished. For example, with the command ‘kill a pig’, if the pig runs away after our agent attacks it once, the agent must understand that the job is not complete until the pig is dead. We will code a way to make sure the agent always stays within attacking range of the target.
</p>

<h2>Resources Used</h2>
<p>The most crucial NLP library we use in writing the implementation is Natural Language Toolkit(nltk). By implementing nltk.word_tokenize, we are able to tokenize a string to split off punctuation other than periods. After tokenizing the user input, the nltk.pos_tag function attaches a part of speech tag to each word from the user input. These tags are crucial for the AI to comprehend the user’s intention.<br>

The inflect library is also a very useful tool. The inflect.engine() allows the algorithm to switch between singular and plural expressions, which helps to standardize the user input.<br>

Finally, the word2number library also plays a big role in the language processing section. Since the user input contains many quantitative data, the word2number library enables the free translation between string number words (eg. twenty-one) to numeric digits (21).</p><br>

<h5>Weekly Meetings: Sunday 2:00 PM</h5>


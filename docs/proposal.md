---
layout: default 
title: Proposal 
---

<h1>SteveAI</h1>

<h2>Summary of the Project</h2>
<p>Our main idea for the project is to implement user text/speech recognition to control	the character. As of now, we plan to find multiple animals/enemies and then feed/kill them depending on their hostility level. For example, typing ‘find the pig’ will command the character to find the closest pig in the world. Since a pig won’t attack us, its hostility level will be 0, so we would resort to feeding it. On the other hand, a zombie which will attack us has a higher hostility level, so we will automate attacking for the command ‘find a zombie’. If we wanted to attack a non-hostile character, we can still kill them if given the command ‘kill a pig/cow/etc.’.</p>

<h2>AI/ML Algorithms</h2>
<p>We will extract the keywords from the user input using NLP models like text classification which allows a set of instructions to be understood by our agent. The instructions will correspond to characters, objects, and actions in the game.</p>

<h2>Evaluation Plan</h2>
<p>The first evaluation method is based on quantity. For example, provided a list of different animals or objects with a certain length, we can check how many times the AI agent can locate the right target. Tthe second evaluation method is based on accuracy. For example, with the same list used for the quantitative test, we can then check whether AI agent can perform the associated command with the animal/enemy such as "kill" or "feed" the target.</p>

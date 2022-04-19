---
title: velma
emoji: ⚖️
colorFrom: green
colorTo: gray
sdk: streamlit
app_file: demo/main.py
pinned: false
---

# VELMA

Value Extraction via Language Model Abduction

##### Placeholder description from past sponsor update

> I mentioned the initial poll was about the next next project, so not the upcoming one, but the one afterwards. For the upcoming one, however, I want to see whether an ML model can predict someone's stance towards a given claim based on their writing. A few scattered thoughts in advance:
>
> For data, I'm planning on scraping the most recent ~100 tweets of ~100 AI alignment researchers. I'll then try to automatically negate each tweet (e.g. P = "Safely aligning a powerful AGI is difficult." to NOT P = "Safely aligning a powerful AGI is easy.") using a mix of prompt engineering and reranking by estimates of contradiction with the original.
>
> The task itself consists in determining which of the two statements was the original, based on the rest of the user's tweets. In practice, you wouldn't have a ground-truth of "yeah they actually used that one", you'd only have two contradictory claims the user has never seen. However, I'm operationalizing stance detection this way based on the assumption that people believe what they say (or perhaps more accurate, people strive to maintain a consistent persona online), which yields a useful signal.
>
> The approach I was thinking of was to check which of the contradictory versions is most likely to follow from the user's most semantically related tweets using a large language model. If they always seem paranoid about AGI taking over the world, the original one above might be more likely, and hence leading to a correct classification.
>
> If successful, this could help in:
> sense-making (estimate expert stances on custom topics, very much related to liquid epistemics or @stuhlmueller's Turning Compute Into Trust);
> aligned language models (incentivize GPT-? to manifest certain stances. This is actually the first candidate project in the poll!);
> truthful language models (incentivize GPT-? to not contradict high-quality research literature. This could be a follow-up to the above...);
> (self-)persuasive technology (synthesize content which exhibits certain stance patterns, with a focus on editing belief systems).
>
> For the demo, maybe you could enter your Twitter handle/RSS feed, answer whether you agree/disagree with statements, and then be presented with predictions and residuals. Or maybe you could enter a list of Twitter users, and have them placed on a spectrum around a claim.
>
> For a name, perhaps VELMA: Value Extraction via Language Model Abduction or with stance as SELMA. I spend too much time on names... Also, will probably be the first time ever I'm cross-posting to LessWrong.

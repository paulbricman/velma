---
layout: post
age: 21.27
title: health protocols
published: True
---

## health protocols

_First, I published a new project exploring [the use of transformer attention in guiding user attention across text](/thoughtware/cybersalience). Second, I helped ship [the "magic labeling" feature](https://www.napkin.one/wp-content/uploads/2022/02/magic-label2.gif) in [Napkin](https://www.napkin.one/), which assists users in [weaving thoughts into their network of concepts](https://www.napkin.one/wp-content/uploads/2021/10/livingsystem.gif), a bit like the recent [Espial](https://github.com/Uzay-G/espial) (and [related work](https://twitter.com/kewbxsh/status/1491791370020818958)). This gig helped me get my feet wet with shipping user-facing NLP features on cloud infrastructure, and by no means indicates a drop in my open source interests. On the contrary, the last days have seen constant progress on the conceptarium rework (e.g. [customizable layout](https://paulbricman.com/assets/vid/conceptarium_layout.mp4), connected microverses persisted across sessions using cookies, bug fixes, etc.)._

---

This piece tackles a more mundane topic than usual. One of my commitments for this year was to reach a stable set of protocols related to health. As I mostly make tiny adjustments on those at this point, I thought it might be fun to write up the details in an article, so here it is.

- procedural diet

For me, a good diet has a few different features, which together lead to quite a tricky optimization landscape to navigate. Food should be nutritious, cheap, easy to put together, quick to put together, easy to procure, tasty, diverse, eco-friendly, etc. I ended up writing a [procedural meal plan generator](https://github.com/paulbricman/meal-planner) using Streamlit which samples simple meal ideas from a local JSON file which acts as the knowledge base. Initially, it generated a plan for an entire week, with 2- or 3-day meal prep cycles. However, I noticed that a simpler 1-day plan which I can then use for a couple days if I need to is more flexible (i.e. for when eating out, celebrating stuff, etc.) and easier to handle. Here's a screenshot of the latest version:

![](/assets/img/meal-planner.png)
_Procedural meal planner ([Source](https://github.com/paulbricman/meal-planner))_

The JSON knowledge base contains four top-level categories: breakfast, lunch, dinner, and snack. Each such category, in turn, contains a non-empty set of meal _frameworks_. For instance, a wrap is one of the lunch frameworks, because it specifies a general structure in which various things can fit. Each framework, in turn, contains a list of ingredients. If an ingredient is a string (e.g. "wholegrain tortilla"), then it's automatically added to the final recipe. However, if an ingredient is a list of strings (e.g. ["red beans", "black beans", "corn"]), then only one element is randomly picked and added to the final recipe. Together with the random sampling of the frameworks themselves, this is what makes the meal planner procedural. Tweaking the ingredients or adding a new framework altogether is as easy as editing the JSON file, while adding a new feature such as probabilistic fasting would simply mean mutating the generated plan in the script. Here's a piece of the JSON:

```json
"breakfast": {
    "🥣 oatmeal": [
      "banana",
      "oatflakes",
      ["crackers", ""],
      "peanut butter",
      ["almond milk", "soy milk", "cow milk"]
    ],
    "🫐 fruit & yogurt": [
      "yogurt",
      "oatflakes",
      ["crackers", ""],
      ["strawberries", "blueberries", "pineapple"]
    ]
  }
```

The range of frameworks available addresses the _easy to put together_, _quick to put together_, and _diverse_ requirements. In contrast, the range of ingredients mostly accounts for _nutritious_, _cheap_, _easy to procur_, and _tasty_. I've generally picked simple ingredients which are themselves regarded as quite healthy, and are available virtually anywhere in the developed world from multiple sources, so as not to break the supply chain if I move back to Romania next year, or somewhere else for my master's. The ingredient level is where things like the Nutri-Score and the NOVA score came in.

The meal planner outputs a list of ingredients clustered by meal in a Markdown-friendly format which I can then copy-paste to Simplenote before heading for groceries, where I then check the boxes. Of course, I mentally do a diff between leftovers and the new shopping list -- the meal planner specifies general guidelines, which I invariably riff on a bit so as not to throw stuff away. It's as if it suggests high-level actions which I make sure to adapt to low-level decisions. The real world is too complex not to break a static low-level plan.

On a related note, if I feel like having a certain meal at a certain time, I'll naturally go for it. The role of the meal planner is to provide a strong default to resort to if I don't feel like eating anything in particular, to help reduce decision fatigue -- nudging myself in moments of lower clarity using a healthier choice architecture.

- water

Nothing too fancy here. I realized at some point that I can use a whiteboard marker on my water bottle, so I'm just marking the number of refills each day, aiming for around five based on online weight/height guidelines.

![](/assets/img/dopper.jpg)
_[Dopper](https://dopper.com/) marked with refills_

- exercise

With this one, just like with diet, it's easy to get lost among endless goals based on number of steps, minutes of exercise, distance walked, reps of a certain exercise, etc. I came across a certain [PAI score](https://support.paihealth.com/hc/en-us/articles/360001037713-What-is-a-PAI-score-) at some point, and immediately adopted it as my main exercise goal due to its simplicity and flexibility. The main idea behind it is that you get PAI _points_ at a rate roughly proportional to your heart rate. If you're sitting at your desk, you'll likely get no points. If you're doing intense cardio, you'll get more points per minute compared to lighter exercise. The exact way you're elevating your heart rate doesn't really matter -- you can run or swim or bike or whatever. The only thing that counts is that you temporarily pressure yourself, you bring in a temporary stressor.

It also adapts to your specific fitness. If your resting heart rate (RHR) is relatively high, you'll get points faster than someone with a low RHR for the very same activity. The fitter you get, the lower your RHR, the stronger the stressor you'll need in order to make a difference. I find it surprising how meaningful heart rate is as a metric -- it appears to be a good proxy for both your fitness in general and the amount of effort in the moment. This means that even an entry-level band I found around the house covers all my tracking needs:

![](/assets/img/pai.jpg)
_Cheap smartband showing PAI today and per day over the past week_

Your PAI _score_ is then the sum of the PAI _points_ you obtained in the past week, so a few intense sessions can be equivalent to lighter daily sessions. If my PAI score in the morning is below the recommended value of 100, I'll go for a run. If not, I'll carry on with the rest of my day. That's it, as simple as a thermostat. If I bike to uni or go for a walk, it adds up in the same rolling window. Staying around 100 helps avoid both under- and overexercise, and the exact rates for earning points are based on some large-scale longitudinal study investigating the relationship between exercise and health. If it wasn't for the proprietary algorithm, it would have really been perfect.

Anyways, those are my current protocols. After the initial setup, the goal was to make them easy to follow so that I could focus on other things, knowing the essentials are covered. We're getting there.

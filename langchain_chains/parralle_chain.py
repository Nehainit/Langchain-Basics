from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap,RunnableParallel


model1= ChatOpenAI()
model2= ChatOpenAI()
# model3= ChatOpenAI()

prompt1 = PromptTemplate(
    template='Create Notes from following text: {text}',
    input_variables=['text']
)   

prompt2 = PromptTemplate(
    template='create 5 multiple choice questions from following notes: {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the Notes and Quiz in single document notes->{notes} and quiz ->{quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableMap(
    notes=prompt1 | model1 | parser,
    quiz=prompt2 | model2 | parser
)

merge_chain = prompt3 | model1| parser

chain=parallel_chain | merge_chain


text="""
How to Get More Impressions on Twitter: A Step-by-Step Guide

Increasing impressions on Twitter means getting your tweets in front of more eyes. More impressions can lead to more engagement, followers, and potential opportunities. Here's a breakdown of actionable steps you can take to boost your Twitter reach:

1. Post Consistently
   - Consistency is Key: Posting regularly keeps you in your followers’ feeds and helps increase visibility. Aim for at least 3-5 tweets per day.
   - Optimal Timing: Tweet during peak hours when your audience is most active. This typically includes:
     - Early morning (8–10 AM)
     - Afternoon (12–2 PM)
     - Evening (6–8 PM)
   - Use Twitter Analytics to figure out when your followers are online and schedule your tweets accordingly.

2. Use Hashtags Wisely
   - Relevant Hashtags: Use trending and relevant hashtags in your niche. This expands the reach of your tweet beyond your followers.
   - Avoid Overloading: Don’t use too many hashtags; 1-3 relevant ones are sufficient. Too many can appear spammy.
   - Research hashtags that are popular in your industry or follow hashtags related to current events.

3. Engage with Others
   - Retweet and Respond: Engage with tweets from other users in your niche. Retweeting, commenting, or liking tweets puts you in front of their audience.
   - Join Conversations: Join trending conversations and participate in Twitter chats. People who see your thoughtful replies may check out your profile.
   - Mention Others: Tag influencers, brands, or users relevant to your content. When they engage with your post, their followers will see it too.

4. Create Shareable Content
   - Visual Content: Tweets with images, videos, GIFs, and polls generally get more engagement. People are more likely to share content that catches their eye.
   - Engaging Headlines: Use intriguing headlines or questions that encourage people to share or reply.
   - Actionable Tips or Insights: Offer value by sharing tips, insights, or actionable advice. People love to share content that can help others.

5. Leverage Twitter Threads
   - Tell a Story: Threads allow you to create a narrative or provide in-depth information. Each tweet in the thread can generate separate impressions.
   - Thread Consistency: When crafting a thread, ensure each tweet is engaging and provides value, keeping users hooked to the next one.

6. Post When There's a Trending Topic
   - Tap Into Trends: Posting content related to trending topics or news increases the chances of your tweets appearing in more people’s feeds.
   - Use the Twitter "Trending" section to stay updated on hot topics and incorporate them into your posts when relevant.

7. Optimize Your Profile
   - Clear Branding: Make sure your bio, profile picture, and cover photo clearly represent who you are and what you tweet about.
   - Link to Website or Portfolio: If you have a personal blog or business, make sure to add links that allow followers to find more about you.
   - Engaging Bio: Keep your bio concise but captivating. A well-crafted bio encourages people to follow you.

8. Use Twitter Ads
   - Promote Tweets: If you have a budget, Twitter Ads can increase impressions by promoting your tweets to a wider audience.
   - Targeting Options: Use Twitter’s targeting features to narrow down your audience by location, interests, and behavior, ensuring your ads reach the right people.

9. Collaborate with Influencers
   - Cross-Promote: Partner with influencers in your industry to promote each other's content. Their audience will be introduced to you, increasing impressions.
   - Guest Tweeting: Some influencers may let you do a guest tweet or shoutout on their profile, helping to boost your visibility.

10. Analyze Your Performance
   - Use Analytics: Regularly check Twitter Analytics to see which posts get the most impressions, engagement, and shares. This will help you understand what works and what doesn’t.
   - Refine Content: Based on your findings, adjust your strategy. Post more of what works, and experiment with different formats to keep things fresh.

Final Thoughts:
Getting more impressions on Twitter takes time, experimentation, and consistency. By following these tips—posting regularly, engaging with others, using the right hashtags, and sharing quality content—you can gradually increase your reach and make your Twitter presence more impactful.

Start small, track your progress, and refine your approach as you learn more about your audience and what resonates with them. Happy tweeting! 🌟
"""

result = chain.invoke({'text':text})
print(result)














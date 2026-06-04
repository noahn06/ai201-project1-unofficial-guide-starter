# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section _after_ you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

The domain I chose was a freshman/transfer's guide to University of Washington Seattle. This knowledge is valuable as the answers that someone new to UW would want are scattered all across the internet (thousands of reddit comments, niche blogs, official school documentation) and that would take tons of time for that person to find. A lot of this information is not provided by the school and thus has to be sourced through online forums where people can voice their actual unfiltered opinions about the school.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| #   | Source                         | Type              | URL or file path                                                                                  |
| --- | ------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------- |
| 1   | r/college                      | Reddit thread     | https://www.reddit.com/r/college/comments/13iggzc/does_anyone_have_an_extremely_detailed_college/ |
| 2   | r/seattle                      | Reddit thread     | https://www.reddit.com/r/Seattle/comments/i2z0u/fun_things_to_do_in_the_u_district/               |
| 3   | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/ta3wg5/just_got_into_uw_very_excited_what_are_the_best/    |
| 4   | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/t748ht/dorms/                                              |
| 5   | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/1rkdhny/uw_first_year_admissions_decisions_megathread/     |
| 6   | UW 2026-2027 Academic Calendar | Official document | https://www.washington.edu/students/reg/2627cal.html                                              |
| 7   | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/1c9zhfj/is_the_dining_hall_bad/                            |
| 8   | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/wgbx4s/favorite_classes_youve_taken_at_uw/                 |
| 9   | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/1d28awz/what_are_good_places_to_eat_in_udistrict/          |
| 10  | r/udub                         | Reddit thread     | https://www.reddit.com/r/udub/comments/1jgjpta/can_yall_share_any_hackstips_to_save_on_tuition/   |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 300

**Overlap:** 50

**Why these choices fit your documents:**
One reddit comment with substantial information is around 100 tokens long, and usually you can get a good perspective on something with 2-3 commments which is why I chose chunk size = 300 which is ~3 comments. I updated from 250 tokens to 300 tokens for chunk size as some crucial information was getting cut out, since due ot the nature of reddit it takes a couple of comments to get to a crucial peice of information. Since some comments have replies on them I added an overlap of 50 to not cut out some information from a chunk.

**Final chunk count:** 87

---

## Sample Chunks

**Chunk 1** — `reddit_fun_things_to_do_seattle_202.txt`, chunk 5

> eries and Woodinville Whisky.
> It really depends what you are in to. Depends where you are coming from, and whether you want something more like what you are used to or something that you cannot find in the city you are from.
> Seattle has loads of medium and small venues for music. There is always a good band in town. You do not need to go to the big stadium or arena to find good music, although Climate Pledge has definitely become a hot spot for tours of lots of well known bands. The showbox is an amazing venue, same with the Paramount and Neptune.
> What are your other interests, or typical drinks/bar types you normally like?
> Happy to give more follow up recommendations.

---

**Chunk 2** — `reddit_college_packing_list.txt`, chunk 3

> cheese, don't recommend Aunt Annie's
> -slippers
> -if your dorm has a key, wear it on a lanyard
> -one of those wallet things to put on the back of your phone for your ID
> Also here's things you don't need:
> -tons of notebooks and folders, you usually only use two at most, it's all online
> -a robe. You'll never wear it.
> An electric kettle/ coffee maker (it's cheaper in the long run to make tea and coffee rather than buying it or having to drink bad dining hall coffee/tea, and good to have hot water when needed) Multiple power strips w surge protectors (I found that I used two every year I lived on campus) Shower slippers (it doesn't matter if you're in a suite or communal shower, slippers aren't an option)

---

**Chunk 3** — `uw_reddit_dorms_2.txt`, chunk 5

> you want the more neighborhood feeling with close access to the quad. Choose north. But if you like a semi urban feel go for west campus. Most dorms are pretty much the same except for hansee and McMahon and haggett(if they decide it's truly livable).
> I'm in west campus and it's not bad but I wouldn't say it's great. You need to spend 1000 a quarter on food which sucks and I find it hard to spend.

---

**Chunk 4** — `uw_reddit_dorms_2.txt`, chunk 1

> Portage Bay is like 5min away.
> The Burke Gillman is right behind you. Tho its close to most North Campus dorms as well.
> You can make whatever experience you want from whichever dorm you choose (excluding old and outliers).
> Lander has really cool lounges compared to Maple. Madrona/Willow usually has the best window "artwork". Center Table has WAYY better views than Local point. The Mill and 8 are better than Area 01. Terry has amazing rooftop access and views.
> So yeah, I'm probably going to move to an apartment next year because killing a level 1 dining account is a struggle and a waste of money.

---

**Chunk 5** — `uw_reddit_dorms.txt`, chunk 4

> cons about mcmahon:
> some room layouts are really bad
> there is a chance ur not gonna like your clustermates
> share a bathroom with 7 ppl
> pros:
> balcony
> someone cleans bathroom and common room for you (the housekeepers here are sooooo nice)
> study rooms + fitness lounge on lobby floor

---

## Retrieval Test Results

_(k=5)_

---

**Query 1:** "what does McMahon Hall have that other dorms dont"

**_Chunk Relevance:_** McMahon is a dorm on UW's campus and is the oldest dorm on campus, is the tallest dorm and has balconies, clusters, and the query is comparing McMahon to to other dorms. These chunks all list features of other dorms and McMahon directly listing features of it.

**[1] uw_reddit_dorms.txt — chunk 3**
dining hall there and a district market there too. Some people prefer this urban feel but it's not for me, at least not when I first moved here and was unfamiliar with the area. As for the actual specific buildings, all the new north campus dorms are pretty similar. Willow has the dining hall and package room in it, Oak has Denny room and the district market in it, and Madrona has this study space in it. However, anyone can access these areas, so it doesn't really matter which one you live in. As for the old north dorms, I have heard that the facilities are pretty run down. Hansee has a lot of singles and the exterior is pretty but I have heard that some people are lonely there. McMahon also has nice views but is run down. I have heard of some people really bonding with their "cluster" in McMahon though, so that's a positive.

**[2] uw_reddit_dorms.txt — chunk 4**
Thank you very much for all the detailed information! Just what I was looking for! If you like cooking though don't go for smaller dorms like Poplar. It only has one kitchen on the 2nd floor, so most of the time you probably won't want to go use it anyway. cons about mcmahon: some room layouts are really bad, there is a chance ur not gonna like your clustermates, share a bathroom with 7 ppl. pros: balcony, someone cleans bathroom and common room for you (the housekeepers here are sooooo nice), study rooms + fitness lounge on lobby floor.

**[3] uw_reddit_dorms_2.txt — chunk 4**
Best dorm is McMahon. You get a living room and each individual room is just as large if not bigger than most of the new dorms. You're basically forced to make new friends because of the clusters. Although it is old the internet is fine. Yep if you actually want to be forced to make friends and have a memorable experience, McMahon is the way to go. However ive seen some people who do not want that and would rather sit in their room all day have had a terrible time in Mcmahon.

**[4] uw_reddit_dorms_2.txt — chunk 3**
going to a triple instead of a double, I would suggest looking at Haggett to save money (if it's open). I agree with the making friends part. It's way more likely in a cluster setup like McMahon. Still not guaranteed, but more of a possibility. No private bathrooms, but they actually have people come in and clean the bathrooms in McMahon for you too, so that's nice. Just make sure to get a room on the second or third floor if you hate stairs or waiting for elevators.

**[5] uw_reddit_firstYear_admissions_deci.txt — chunk 0**
UW First Year Admissions Decisions Megathread. Pretty much all of the dorms aside from McMahon and Hansee are recently updated — both North and West campus. The updated dorms all mostly have private bathrooms (some limited exceptions to that). North campus has more of a classic "collegiate" vibe while west campus feels more like living in a big city, that's definitely worth considering while you're deciding which dorm to pick.

---

**Query 2:** "what are the most recommended food spots on the Ave near UW"

**_Chunk Relevance:_** UW is home to the Ave (which is in the U district) which is a strip of restaurants and shops that spans end to end past UW's campus. Very popular for students to eat on the ave. These chunks all list restaurants that exist on the ave and around the UDistrict.

**[1] uw_reddit_food_udistrict_2024.txt — chunk 0**
What are good places to eat in UDistrict. I'm interning in Seattle this summer and staying in UDistrict. What are some places to get food that aren't really chains where I can get somewhere else? I also love Off the Rez in the Burke Museum on UW campus. It is a Native American owned business with Fry bread, Indian tacos, and rice bowls. Out of all the Mediterranean food places, Sultan's is the best if you ask me. Aladdin's and Shawarma King just don't measure up.

**[2] reddit_fun_things_to_do_seattle_202.txt — chunk 2**
Wings Over Washington — It's campy but the views are incredible. There are TONS of great restaurants and many I am sure you will find on your own, but Barolo is an underrated little spot. For drinks, try the Polar Bar. Food: KAMONEGI is a MUST, especially for this Fall weather, Umi Sake House or Momiji for sushi, Walrus and the Carpenter for oysters, Gracia in Ballard for Mexican.

**[3] uw_reddit_dining_hall.txt — chunk 7**
variety of coffeeshops on campus. A lot of it was closed from midday Friday until Sunday evening when I lived in the dorms a few years ago though, which was kind of frustrating. The food is decent if cooked correctly. I'd say the best meals are probably their mashed potatoes and meatloaf, shrimp etoufee, Korean fried chicken, and Latin bowl. My biggest complaint about the food would be quality vs price.

**[4] uw_reddit_food_udistrict_2024.txt — chunk 2**
On the Ave I don't think there's any places that would wow you extremely, but comparing price to portion and taste, Sizzle&Crunch, Miss Mike's Bento & Noodle, UDubBop and YGF Malatang is probably the best. Seattle is home to the best chicken teriyaki in the world. Rainier Teriyaki or Toshi's teriyaki are widely considered the best of the best. But above all else, go to Paseo Sandwich in Fremont. DUPBOP. Great Asian food with good portions. As others have said Off the Rez and Agua Verde are both wonderful. Taste of India.

**[5] reddit_fun_things_to_do_seattle_202.txt — chunk 3**
Food: KAMONEGI is a MUST, especially for this Fall weather, Umi Sake House or Momiji for sushi, Walrus and the Carpenter for oysters, Gracia in Ballard for Mexican, Itto's Tapas for a fun tapas night out with amazing sangrias!, Musang in Beacon Hill. Things to do: shopping around in University Village, Discovery Park, Fremont Market and Ballard Market, Kerry Park for the Seattle skyline views. Dessert: Hello Robin (100/10), R&M Desserts in Capitol Hill, Molly Moon's ice cream, Indigo Cow (100/10), Pie Bar in Capitol Hill.

---

**Query 3:** "best way for out-of-state students to save money on UW tuition"

**[1] uw_seattle_expenses_hacks_and_tips.txt — chunk 10**
the cc route. if you're not willing to do that, then UW isn't the school for you. to follow our dreams we all have to sacrifice certain things, whether its time, happiness, or the idea of your life following a set path. UW is a great school and as a student I love it, BUT it's not worth being 160k in debt for the rest of your life. you can always come here for grad school! UW is notoriously stingy with aid for out of state students. The Facebook group Paying for College 101 can be very helpful.

**[2] uw_seattle_expenses_hacks_and_tips.txt — chunk 5**
through loans/working so you should be carefully looking at what you can actually afford and really think about if UW is going to work at all. I went to UW and it was fine. FAFSA loans are capped at a certain amount per year (for me they only covered about 1/3 of my expenses). Yes, you can make some money at internships but getting an internship is far from guaranteed. Even in the best of times it can be hard for freshmen and sometimes sophomores to get internships.

**[3] uw_seattle_expenses_hacks_and_tips.txt — chunk 0**
Can y'all share any hacks/tips to save on tuition and other expenses?? Wanna attend UDub but i aint got 60k lying around. I've been admitted to UDub for engineering but its wayyyy too expensive to attend, especially since i'm oos. Move to Seattle. Establish residency (I think it takes a year). Go to community college for two years. Transfer to UW as instate. Save oodles of money. If you are still dependent on your parents, most state schools require your residency to be the same as theirs.

**[4] uw_seattle_expenses_hacks_and_tips.txt — chunk 11**
And if you're comparing between choices right now, the NPC will help you get a better sense of the true cost so you can fairly compare. Also, UW is notorious for not giving very generous merit aid for out of state students. There are some public universities that actively try to woo out of state students, like the University of Alabama. Because Seattle is one of the most expensive cities in the US, it is even more expensive to attend.

**[5] uw_seattle_expenses_hacks_and_tips.txt — chunk 7**
on the lookout for scholarships related to activities you're doing during college — UW has scholarship competitions for undergrads doing research and leadership, for example. Network with your professors! Some professors will hire past students as TAs. Don't live in the most expensive dorm, maybe do a triple room or one of the older buildings. If you live off campus live with more people and try to do your research for the following year very early. Off campus housing has a huge range in cost depending on how high your standards are.

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 (sentence-transformers)

**Production tradeoff reflection:** If I was deploying for real users and cost was not a constraint I would use an embedding model with multilingual support and stronger accuracy on domain-specific text. UW even though it is primarily a school that speaks English, there are a lot of international students that may comment something on their respective online forums or r/udub too. I also feel that with the main provider of these forum comments being college students, there is a lot of slang like "u-district" = university district or "the ave" = university way that a general-purpose model may not pick up on well. I might choose a model that has more a up to date dictionary with slang or something.

Latency does not really matter that much since the information is not time-sensitive, and more context context length does not help here, bigger chunks would just mean probably less relevant information per chunk given the short nature of reddit comments.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
"You are a helpful guide for incoming freshmen / transfer students at the University of Washington Seattle.
Answer the question using ONLY the information provided in the context documents below. Do not be verbose, preferably respond to the query in 2-3 sentences.
If the documents don't contain enough information to answer, say "I don't have enough information on that. Sorry."
Do not provide any reasoning on why you don't have documentation, just say "(No documentation found)"
Do not use any outside knowledge. Cite which document(s) your answer comes from at the end of your response."

**How source attribution is surfaced in the response:**
in the response it diectly labels the document selected as well as chunk number like this:

"For on-campus dining, options include the dining halls, with Plate at CT and Global kitchen at LP being recommended, as well as the hot food bar at District Market and Starbucks locations (uw_reddit_dining_hall.txt, chunk 0). Off the Rez in the Burke Museum is also a recommended option, serving Native American food (uw_reddit_food_udistrict_2024.txt, chunk 0)."

---

## Example Responses

**Example 1**
q: best place to get good coffee near UW?
a: "You can get a good cup of coffee at Cafe Allegra, which has some of the best coffee on the ave, or at Espresso Vivaci on Capitol Hill, which has the best espresso in the city. Additionally, there are various coffee shops on campus where you can use your dining dollars. (uw_reddit_food_udistrict_2024.txt, uw_reddit_dining_hall.txt)"

**Example 2**
q: which dorm has a study room?
a: "Madrona has a study space in it. (uw_reddit_dorms.txt, chunk 3)"

**Refusal Example**
q: where can i meet dubs the husky
a: "I don't have enough information on that. Sorry. (No documentation found)"

---

---

## Query Interface

**Input Field Description**
Purple and gold box (uw colors) titled "Your question"
example text is grayed out and says "e.g. What dorm is best for meeting people?"
giant orange "Ask" button is next to it, question in field is then sent as query to chromaDB

**Output Field Description**
purple and gold box titled "Answer", retrieved and generated response is printed here for user to see

**Sample Transcription**
Query: "what is the easiest class to take freshman year"

Response: "According to uw_reddit_fav_classes.txt, some of the easiest classes mentioned include ASTR 101 with Chris Laws, which has a light workload, and PHIL 347, philosophy in literature, which involves readings and discussions and is also an easy 4.0. (uw_reddit_fav_classes.txt)"

---

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| #   | Question                                                                       | Expected answer                                                                                                                | System response (summarized)                                                                                                                                                                                                                                   | Retrieval quality | Response accuracy                                                                                           |
| --- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | what does McMahon Hall have that other dorms don't?                            | McMahon has clusters of 8 people sharing a common room and balcony, and housekeepers clean the shared bathroom and common room | McMahon Hall has a living room and larger individual rooms, as well as a cluster setup that encourages socialization and making friends. It also has study rooms, a fitness lounge, and a balcony, with housekeepers who clean the bathrooms and common rooms. | relevant          | accurate                                                                                                    |
| 2   | what day does school get out for Fall quarter 2026                             | December 18, 2026                                                                                                              | School gets out for Fall quarter 2026 on December 12, 2026, as it is the last day of class.                                                                                                                                                                    | relevant          | partially accurate, does not account for finals week which is 12-18. end of regular instruction is dec, 12  |
| 3   | most popular things to do near Seattle                                         | as Works Park, the UW Arboretum, and Alki Beach West seattle                                                                   | ballard locks, gas works, arboretum, museums, take ferry                                                                                                                                                                                                       | relevant          | accurate                                                                                                    |
| 4   | what are the most recommended food spots on the Ave near UW?                   | Saigon Deli, Aladdin's, sizzle & crunch                                                                                        | Off the Rez, Agua Verde, DUPBOP, and Taste of India                                                                                                                                                                                                            | relevant          | partially accurate, these places all exist but are definitely not the most popular places to go on the ave. |
| 5   | what is the best way way for out-of-state students to save money on UW tuition | Go to a Washington community college for then transfer to UW as an in-state student - saves a lot in tuition                   | become WA state resident for a year, attend cc for two years, transfer to UW                                                                                                                                                                                   | relevant          | accurate                                                                                                    |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
What is ASTR101 about?

**What the system returned:**
ASTR 101 is a class that doesn't go too hard into the physical science, and it has a relatively light workload with just a short reading and a quiz weekly. (uw_reddit_fav_classes.txt, chunk 0)

**Root cause (tied to a specific pipeline stage):**
ingestion stage, the response i am getting is vague and does not say anything about what the class is about but what the courseload is. i assume it's a lack of breadth and depth of data

**What you would change to fix it:**
scrape all UW classes and upload those course descriptions along with even potentially syllabus, clean and chunk and embed for better retrieval accuracy and relevance

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
writing the spec helped me frontload all of the necessary and cognitive thinking as well as system design decisions first before i jumped into prompting claude. i used to all the time jump in without a spec but with the spec i was able to constantly refer back to it as the master document which helped me follow along with what was happening and claude for instruction following.

**One way your implementation diverged from the spec, and why:**
i ended up having to increase my top k = 5 instead of 3 as i had initially planned to do as sometimes my retrieval would bring back the correct relevant chunks but it would be way too specific about one thing and would be way off. increasing my topk amount allows for slightly less relevant chunks but more chance that i'll be able to retrieve a chunk that answers what the query is asking.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- _What I gave the AI:_ I let claude read my planning.md and README.md to fill out all of the fields that i already wrote for planning.md into readme.md
- _What it produced:_ basically copied and pasted some of my written text from planning.md
- _What I changed or overrode:_ i didn't override anything because i was just being efficient having claude do something redundant while i wrote actual new reflections

**Instance 2**

- _What I gave the AI:_ i gave claude access to my documents folder as well as my chunking strategy in planning.md
- _What it produced:_ produced an ingest.py script with clean_data function as well as chunk_text with parameters for chunk size, overlap and text input. this cleans and chunks data to get it ready for embedding and storing vector db
- _What I changed or overrode:_ the clean_Data function was not perfect and left a lot of remnant usernames, reddit comment scaffolding, so i had to overwrite and tell claude deliberately what to look for (only comment data no usernames, karma, flairs , etc)

# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
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

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | r/college | Reddit thread | documents/reddit_college_packing_list.txt |
| 2 | r/seattle | Reddit thread | documents/reddit_fun_things_to_do_seattle_202.txt |
| 3 | r/udub | Reddit thread | documents/uw_reddit_dorms.txt |
| 4 | r/udub | Reddit thread | documents/uw_reddit_dorms_2.txt |
| 5 | r/udub | Reddit thread | documents/uw_reddit_firstYear_admissions_deci.txt |
| 6 | UW 2026-2027 Academic Calendar | Official document | documents/uw_2026_2027_calendar.txt |
| 7 | r/udub | Reddit thread | documents/uw_reddit_dining_hall.txt |
| 8 | r/udub | Reddit thread | documents/uw_reddit_fav_classes.txt |
| 9 | r/udub | Reddit thread | documents/uw_reddit_food_udistrict_2024.txt |
| 10 | r/udub | Reddit thread | documents/uw_seattle_expenses_hacks_and_tips.txt |

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
One reddit comment with substantial information is around 100 tokens long, and usually you can get a good perspective on something with 2-3 commments which is why I chose chunk size = 300 which is ~3 comments. I updated from 250 tokens to 300 tokens for chunk size as some crucial information was getting cut out, since due ot the nature of reddit it takes a couple of comments to get to a crucial peice of information. Since some comments have replies on them I added an overlap of 50 to  not cut out some information from a chunk.

**Final chunk count:** 87

---

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

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | what does McMahon Hall have that other dorms don't? | McMahon has clusters of 8 people sharing a common room and balcony, and housekeepers clean the shared bathroom and common room | McMahon Hall has a living room and larger individual rooms, as well as a cluster setup that encourages socialization and making friends. It also has study rooms, a fitness lounge, and a balcony, with housekeepers who clean the bathrooms and common rooms. | relevant | accurate |
| 2 | what day does school get out for Fall quarter 2026|December 18, 2026 | School gets out for Fall quarter 2026 on December 12, 2026, as it is the last day of class. | relevant | partially accurate, does not account for finals week which is 12-18. end of regular instruction is dec, 12 |
| 3 | most popular things to do near Seattle  |as Works Park, the UW Arboretum, and Alki Beach West seattle |ballard locks, gas works, arboretum, museums, take ferry  | relevant | accurate  |
| 4 |what are the most recommended food spots on the Ave near UW? | Saigon Deli, Aladdin's, sizzle & crunch| Off the Rez, Agua Verde, DUPBOP, and Taste of India| relevant| partially accurate, these places all exist but are definitely not the most popular places to go on the ave. |
| 5 | what is the best way way for out-of-state students to save money on UW tuition |Go to a Washington community college for then transfer to UW as an in-state student - saves a lot in tuition | become WA state resident for a year, attend cc for two years, transfer to UW |relevant | accurate |

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
i ended up having to increase my top k = 6 instead of 3 as i had initially planned to do as sometimes my retrieval would bring back the correct relevant chunks but it would be way too specific about one thing and would be way off. increasing my topk amount allows for slightly less relevant chunks but more chance that i'll be able to retrieve a chunk that answers what the query is asking.

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

- *What I gave the AI:* I let claude read my planning.md and README.md to fill out all of the fields that i already wrote for planning.md into readme.md
- *What it produced:* basically copied and pasted some of my written text from planning.md
- *What I changed or overrode:* i didn't override anything because i was just being efficient having claude do something redundant while i wrote actual new reflections

**Instance 2**

- *What I gave the AI:* i gave claude access to my documents folder as well as my chunking strategy in planning.md
- *What it produced:* produced an ingest.py script with clean_data function as well as chunk_text with parameters for chunk size, overlap and text input. this cleans and chunks data to get it ready for embedding and storing vector db
- *What I changed or overrode:* the clean_Data function was not perfect and left a lot of remnant usernames, reddit comment scaffolding, so i had to overwrite and tell claude deliberately what to look for.

# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

## The domain I chose was a freshman/transfer's guide to University of Washington Seattle. This knowledge is valuable as the answers that someone new to UW would want is scattered all across the internet (thousands of reddit comments, niche blogs, official school documentation) and that would take tons of time for that person to find. A lot of this information is not provided by the school and thus has to be sourced through online forms where people can voice their actual unfiltered opinions about the school.

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| #   | Source                         | Description                                   | URL or location                                   |
| --- | ------------------------------ | --------------------------------------------- | ------------------------------------------------- |
| 1   | r/college                      | college packing list                          | documents/reddit_college_packing_list.txt         |
| 2   | r/seattle                      | fun things to do in seattle                   | documents/reddit_fun_things_to_do_seattle_202.txt |
| 3   | r/udub                         | UW dorm recommendations and comparisons       | documents/uw_reddit_dorms.txt                     |
| 4   | r/udub                         | More UW student opinions on best dorms        | documents/uw_reddit_dorms_2.txt                   |
| 5   | r/udub                         | UW first year admissions decisions megathread | documents/uw_reddit_firstYear_admissions_deci.txt |
| 6   | UW 2026–2027 academic calendar | UW 2026–2027 academic calendar                | documents/uw_2026_2027_calendar.txt               |
| 7   | r/udub                         | UW dining hall student opinions               | documents/uw_reddit_dining_hall.txt               |
| 8   | r/udub                         | Favorite UW classes students recommend        | documents/uw_reddit_fav_classes.txt               |
| 9   | r/udub                         | Best food spots in UDistrict Seattle          | documents/uw_reddit_food_udistrict_2024.txt       |
| 10  | r/udub                         | UW expense hacks and money-saving tips        | documents/uw_seattle_expenses_hacks_and_tips.txt  |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
250

**Overlap:**
50

**Reasoning:**
One reddit comment with substantial information is around 100 tokens long, and usually you can get a good perspective on something with 2-3 commments which is why I chose chunk size = 250 which is ~2.5 comments. Since some comments have replies on them I added an overlap of 50 to hopefully not cut out some information from a chunk

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
sentence-transformers (all-MiniLM-L6-v2)

**Top-k:**
3

**Production tradeoff reflection:**
If I was deploying for real users and cost wasn't a constraint I would use an embedding model with multilingual support, accuracy on domain-specific text, and.. I feel that UW even though it is primarily a school that speaks English, there are a lot of international students that may comment something on their respective online forums or r/udub too. I also feel that with the main provider of these forum comments being college students, there is a lot of slang like "u-district" = university district or "the ave" = university way that the embedding model may not pick up on.

latency doesn't really matter that much the information is not that time sensitive.
more context length doesn't matter here as bigger chunks would just mean probably less relevant information for reddit comments

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| #   | Question                                                                       | Expected answer                                                                                                                    |
| --- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1   | what does McMahon Hall have that other dorms don't?                            | McMahon has clusters of 8 people sharing a common room and balcony, and housekeepers clean the shared bathroom and common room     |
| 2   | what do students say the dining hall is serving as a vegetable the most ?      | broccolini                                                                                                                         |
| 3   | most popular things to do near Seattle                                         | Gas Works Park, the UW Arboretum, Volunteer Park, and Alki Beach West Seattle                                                      |
| 4   | what are the most recommended cheap food spots on the Ave near UW?             | Saigon Deli for banh mi, Aladdin's for gyros/shawarma, Sizzle & Crunch, Xi'an Noodles,                                             |
| 5   | what is the best way way for out-of-state students to save money on UW tuition | Go to a Washington community college for two years first, then transfer to UW as an in-state student — saves over $160k in tuition |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. there are a lot of contradictory opinions presented as fact as reddit is an online forum. some people might really like a restaurant while some may not, this may confuse the retriever

2. reddit has deleted content and will just fill up some chunks with complete garbage messages like "this post has been deleted"

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

Document Ingestion → Chunking → Embedding → Vector Store → Retrieval → Generation
open() + txt | tiktoken | all-MiniLM-L6-v2 | ChromaDB | cosine k=3 | Claude API

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
tool: claude code
input: i'll give it all of my collected documents in documents. i'll also give claude my chunking strategy section in planning.md

output: ingest.py script with two functions, a clean_text(raw_text) that strips deleted comments, reddit scaffolding
and chunk_text(text, chunk_size, overlap) that returns a list of sized chunks using tiktoken

verification: manually look at printed chunks from uw_reddit_dorms.txt and manually confirm that they are clean/validated, have real comment information from users, and are correctly sized and overlapped correctly.

**Milestone 4 — Embedding and retrieval:**

tool: claude code
input: i'll give it retrieval approach of planning.md and chunk_text() output from milestone 3

output: embed.py script that loads chunks, embeds with miniLM and stores them in chromaDB. gives me retrieve(query, top k = k) function that returns top k relevant chunks

verification: retrieve("best dorm for meeting people", k = 3) and check that returned chunks are about dorms and maybe even answer the test question of McMahon Hall.

**Milestone 5 — Generation and interface:**

tool: claude code
input: retrieve() function @milestone 4 and the 5 testing questions from @evaluation plan

output: generate.py script with ask(question) function that will then call retrieve() giving me top-k chunks to send to claude which prints answers in my interface.

verification: run all 5 eval questions and compare answers to expected answers, see if it is correct.

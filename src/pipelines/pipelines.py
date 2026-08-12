from src.agents.agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain,
)


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # --------------------------------
    # Step 1 — Search Agent
    # --------------------------------

    print("\n" + "=" * 50)
    print("STEP 1 - Search Agent is working...")
    print("=" * 50)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable and detailed information about: {topic}"
            )
        ]
    })

    state["search_results"] = search_result["messages"][-1].content

    print("\nSearch Results:\n")
    print(state["search_results"])


    # --------------------------------
    # Step 2 — Reader Agent
    # --------------------------------

    print("\n" + "=" * 50)
    print("STEP 2 - Reader Agent is scraping resources...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""
Based on the following search results about '{topic}',
pick the most relevant URL and scrape it for deeper content.

Search Results:

{state["search_results"][:800]}
"""
            )
        ]
    })

    state["scraped_content"] = (
        reader_result["messages"][-1].content
    )

    print("\nScraped Content:\n")
    print(state["scraped_content"])


    # --------------------------------
    # Step 3 — Writer Chain
    # --------------------------------

    print("\n" + "=" * 50)
    print("STEP 3 - Writer is drafting the report...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n"
        f"{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n"
        f"{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined,
    })

    print("\nFinal Report:\n")
    print(state["report"])


    # --------------------------------
    # Step 4 — Critic Chain
    # --------------------------------

    print("\n" + "=" * 50)
    print("STEP 4 - Critic is reviewing the report...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCritic Report:\n")
    print(state["feedback"])


    return state
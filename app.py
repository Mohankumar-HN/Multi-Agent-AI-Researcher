import streamlit as st

from src.pipelines.pipelines import run_research_pipeline


st.set_page_config(
    page_title="Multi-Agent AI Researcher",
    page_icon="🔬",
    layout="wide"
)


st.title("🔬 Multi-Agent AI Researcher")

st.write(
    "Enter a topic and let the multi-agent system research, "
    "write and evaluate a report."
)


topic = st.text_input(
    "Research Topic",
    placeholder="Example: Impact of AI on the job market in 2026"
)


if st.button("Start Research"):

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        with st.spinner("Research agents are working..."):

            result = run_research_pipeline(topic)


        st.success("Research completed!")

        # -------------------------
        # Search Results
        # -------------------------

        with st.expander("🔎 Search Results"):

            st.write(result["search_results"])


        # -------------------------
        # Scraped Content
        # -------------------------

        with st.expander("📄 Scraped Content"):

            st.write(result["scraped_content"])


        # -------------------------
        # Final Report
        # -------------------------

        st.header("📝 Research Report")

        st.markdown(result["report"])


        # -------------------------
        # Critic
        # -------------------------

        st.header("🧐 Critic Feedback")

        st.markdown(result["feedback"])
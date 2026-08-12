from src.pipelines.pipelines import run_research_pipeline


def main():

    topic = input("Enter your research topic: ")

    result = run_research_pipeline(topic)

    print("\n" + "=" * 60)
    print("FINAL RESEARCH REPORT")
    print("=" * 60)

    print(result["report"])

    print("\n" + "=" * 60)
    print("CRITIC FEEDBACK")
    print("=" * 60)

    print(result["feedback"])


if __name__ == "__main__":
    main()
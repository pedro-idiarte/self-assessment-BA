import sys

def run_assessment():
    categories = {
        "General Skills": [],
        "User Acceptance Testing": [],
        "Gathering and Documenting User Requirements": [],
        "Project Management": [],
        "Problem Solving": []
    }

    questions = {
        "General Skills": [
            "Do you have a process for making presentations?",
            "Do you understand the principles of effective written communication?",
            "Do you understand the principles of effective oral communication?",
            "Do you obtain at least 40 hours of continuing professional education per year?",
            "Are you trained to perform in the role of a facilitator?",
            "Have you been trained in how to design and deploy work processes?",
            "Do you understand basic concepts of systems development?",
            "Do you have a process for listening which involves active listening, clarification of input, and providing feedback?",
            "Have you had training in conflict resolution/negotiation?",
            "Have you had formal training in project management skills?"
        ],
        "User Acceptance Testing": [
            "Do you understand the basic phases and types of testing?",
            "Do you understand the importance of early and continuous testing?",
            "Do you understand and use reviews and inspections as part of your testing process?",
            "Do you understand the concepts involved in building a test environment?",
            "Have you been involved in facilitating User Acceptance Testing with endusers or people representing end-users?",
            "Do you understand the differences between UAT and other phases of testing?",
            "Do you understand how to create user test scenarios?",
            "Do you understand basic test measurements and metrics?",
            "Do you understand how to depict business processes?",
            "Do you have a process for tracking and analyzing software defects?"
        ],
        "Gathering and Documenting User Requirements": [
            "Do you have a process for gathering user requirements?",
            "Do you have standards and templates that you use for documenting user requirements?",
            "Do you understand how to prioritize user requirements?",
            "Do you understand the basic steps for conducting interviews?",
            "Do you understand how to ask the right questions in an interview?",
            "Do you understand how to review requirements for correctness?",
            "Do you understand how to invite the right people to an interview session?",
            "Do you understand how to review requirements for ambiguity?",
            "Do you understand how to define test cases from user requirements?",
            "Have you had experience in working with end-users to gather and define requirements?"
        ],
        "Project Management": [
            "Do you understand the various system development life cycle methodologies?",
            "Do you have experience in managing projects?",
            "Are you able to select the appropriate level of business analysis techniques based on project size?",
            "Are you able to implement and enforce change management procedures?",
            "Do you understand how to define the scope of a project?",
            "Do you have a process for organizing a project?",
            "Do you have experience in assessing the risk on a project?",
            "Do you have a process for risk assessment?",
            "Do you have a process for creating a project plan?",
            "Do you have experience in dealing with project stakeholders?"
        ],
        "Problem Solving": [
            "Do you have a process for analyzing defects by origin and severity?",
            "Do you understand how to define a problem in writing?",
            "Do you understand how to identify business problems and determine which are in scope?",
            "Do you understand how to analyze business problems to separate problems from symptoms and predetermined solutions?",
            "Do you know how to locate the cause of business problems in business process flows?",
            "Do you know how to identify weaknesses and propose improvements in how the organization uses its information resource",
            "Do you understand how to perform root cause analysis?",
            "Do you understand how to identify and analyze exceptions and errors in business and information system processes?",
            "Do you understand how to organize and document business problems for presentation and discussion?",
            "Have you had formal training in problem resolution techniques?"
        ]
    }

    results = {category: 0 for category in categories}

    print("\n--- Start of the Business Analyst Skills Self-Assessment ---")
    
    for category, q_list in questions.items():
        print(f"\nCategory: {category}")
        for i, question in enumerate(q_list):
            while True:
                sys.stdout.write(f"{i+1}. {question} (y/n): ")
                sys.stdout.flush()
                response = sys.stdin.readline().strip().lower()
                if response in ['y', 'n']:
                    if response == 'y':
                        results[category] += 1
                    break
                else:
                    print("Invalid response. Please enter 'y' for yes or 'n' for no.")

    print("\n--- Self-Assessment Results ---")
    for category, score in results.items():
        print(f"{category}: {score} out of 10 (Score: {score * 10}%)")

    print("\n--- End of Self-Assessment ---")

if __name__ == "__main__":
    run_assessment()

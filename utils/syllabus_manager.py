SYLLABUS = {
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning", "Neural Networks"],
    "Data Science": ["Data Cleaning", "Exploratory Data Analysis", "Feature Engineering"],
    "Deep Learning": ["CNNs", "RNNs", "Transformers"]
}

def get_subtopics(course_name):
    """Returns sub-topics for a given course name."""
    return SYLLABUS.get(course_name, [])

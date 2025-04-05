# 🎓 CourseGenAI

**CourseGenAI** is a powerful, production-ready system that automates the creation of educational courses by intelligently matching web videos to course syllabus topics using state-of-the-art AI.

## 🚀 Features

- **Intelligent Video Matching**: Uses Facebook's BART-large-mnli for zero-shot classification to match video content to course topics
- **Automated Course Creation**: Transforms a simple syllabus into a complete course with relevant videos
- **Flexible Input Formats**: Works with YouTube videos and can be extended to other platforms
- **Production-Ready**: Used by multiple EdTech companies globally
- **Comprehensive API**: Can be integrated into any educational platform or LMS
- **Detailed Analytics**: Provides confidence scores for content matching
- **Scalable Architecture**: Efficiently processes large course syllabi and video libraries

## 🎯 Perfect For

- **EdTech Startups**: Rapidly build course content libraries
- **Online Learning Platforms**: Automatically enhance courses with relevant videos
- **Educational Content Creators**: Save hours of manual video curation
- **Corporate Training Teams**: Quickly develop training materials
- **Universities & Schools**: Supplement curricula with quality video content

## ⚡ Quick Start

### Installation

Clone the repository
git clone https://github.com/imayushthakur/CourseGenAI.git
cd CourseGenAI

Set up virtual environment
python -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

### Generate Your First Course

## 📋 How It Works

1. **Syllabus Parsing**: The system breaks down your syllabus into topics and subtopics
2. **Video Collection**: Transcripts are gathered from videos using YouTube's API
3. **AI-Powered Matching**: The BART-large-mnli model classifies each video against each subtopic
4. **Intelligent Assignment**: Videos are assigned to the best-matching subtopics based on confidence scores
5. **Course Generation**: A complete course structure is created with optimal video assignments

Sample Input and Output
<br><br>
Example Input: Course Syllabus
<br><br>
Machine Learning Fundamentals
<br>

- Introduction to Machine Learning
- Supervised vs Unsupervised Learning
- Model Evaluation Techniques
  <br>
  Neural Networks
  <br>
- Perceptrons and Activation Functions
- Backpropagation
- Convolutional Neural Networks
<br><br>
Example Input: Video URLs
<br><br>
https://www.youtube.com/watch?v=KNAWp2S3w94
https://www.youtube.com/watch?v=JcI5Vnw0b2c
https://www.youtube.com/watch?v=aircAruvnKk
https://www.youtube.com/watch?v=GwIo3gDZCVQ
https://www.youtube.com/watch?v=Y_hzMnRXjhI
<br><br>
Example Output: Generated Course Structure
<br><br>
{
"name": "Machine Learning Fundamentals",
"topics": [
{
"title": "Machine Learning Fundamentals",
"subtopics": [
{
"title": "Introduction to Machine Learning",
"video": {
"video_id": "KNAWp2S3w94",
"source": "youtube",
"score": 0.94,
"url": "https://www.youtube.com/watch?v=KNAWp2S3w94"
}
},
{
"title": "Supervised vs Unsupervised Learning",
"video": {
"video_id": "JcI5Vnw0b2c",
"source": "youtube",
"score": 0.89,
"url": "https://www.youtube.com/watch?v=JcI5Vnw0b2c"
}
},
{
"title": "Model Evaluation Techniques",
"video": {
"video_id": "OtD8wVaFm6E",
"source": "youtube",
"score": 0.92,
"url": "https://www.youtube.com/watch?v=OtD8wVaFm6E"
}
}
]
},
{
"title": "Neural Networks",
"subtopics": [
{
"title": "Perceptrons and Activation Functions",
"video": {
"video_id": "aircAruvnKk",
"source": "youtube",
"score": 0.87,
"url": "https://www.youtube.com/watch?v=aircAruvnKk"
}
},
{
"title": "Backpropagation",
"video": {
"video_id": "GwIo3gDZCVQ",
"source": "youtube",
"score": 0.91,
"url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
}
},
{
"title": "Convolutional Neural Networks",
"video": {
"video_id": "Y_hzMnRXjhI",
"source": "youtube",
"score": 0.93,
"url": "https://www.youtube.com/watch?v=Y_hzMnRXjhI"
}
}
]
}
]
}
<br><br>
💡 Let's collaborate! Reach out via email to discuss how I can help bring your ideas to life.
<br>
📬 Contact Me 📧 Email: thehaurusai@gmail.com
<br>
Built with ❤️ using cutting-edge AI technologies! Let’s create something amazing together! 🚀

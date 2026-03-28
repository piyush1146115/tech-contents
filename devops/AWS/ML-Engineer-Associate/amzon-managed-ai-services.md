# AWS Managed AI Services

- AWS AI Services are pre-trained ML services for your use case
- Responsiveness and Availability
- Redundancy and Regional Coverage

## Amazon Comprehend

- For natural language processing
- Fully managed and serverless service
- Training Data -> Amazon S3 -> Training data -> Comprehend -> Custom Classifier
- Comprehend custom models: trained your own data, custom models may be copied between AWS accounts

## Amazon Translate

- Natural and accurate translation

## Amazon Transcribe

- Automatically convert speech to text
- Uses a deep learning process called automatic speech recognition to convert speech to text quickly and accurately
- Transcribe Toxicity Detection: 
    - ML-powered voice based toxicity detection capability
    - Leverages speech cues: tone and pitch, and text-based cues

## Amazon Polly

- Turn text into lifelike speech using deep learning
- Allowing you to create applications that talk

- Lexicons:
    - Dfine how to read certain specific pieces of text

## Amazon Rekognition

- Find objects, people, text, scenes in images and videos using ML
- Facial analysis and facial search to do user verification, people counting
- Create a database of "familiar faces" or compare against celebrities
- Content Moderation: 
    - Automatically detect inappropriate, unwanted, or offensive content
    - Example: filter out harmful images in social media, broadcast media
- Integrated with Amazon Augmented AI for human review

## Amazon Lex

- Build chatbots quickly for your applications using voice and text
- Example: a chatbot that allows your customers to order pizzas or book a hotel

## Amazon Personalize

- Fully managed ML-service to build apps with real-time personalized recommendations 
- Same technology used by Amazon.com
- Ingrates into existing websites, applications, SMS, email marketing systems
- Use cases: retail stores, media and entertainment

## Amazon Textract

- Automatically extracts text, handwriting, and data from any scanned documeents using AI and ML

## Amazon Kendra

- Fully managed document search service powered by Machine Learning
- Extract answers from within a document
- Natural language search capabilities
- Learn from user interactions/feedback to promote preferred results

## Amazon Augmented AI

- Human oversight of Machine learning predictions in production
- The ML model can be built on AWS or elsewhere
- Trigger human review for labels identified based on the confidence score

## Amazon's Hardware for AI

- Amazon EC2
- GPU based EC2 instances (P3, P4, P5.., G3..G6..)
- AWS Trainium
    - ML chip to perform deep learning on 100B+ parameter
    - Trn1 instance has for example 16 Trainium Accelerators
    - 50% cost reduction when training a model
- AWS Inferentia
    - ML chip built to deliver inference at high performance and low cost
    - Inf1, Inf2 instances are powered by AWS Inferentia
    - Up to 4x throughput and 70% cost reduction
- Trn and Inf have the lowest environmental footprint


## Amazon Q Business

- Fully managed Gen-AI assistant for your employees
- Based on your company's knowledge and data
- Built on Amazon Bedrock
- Data connectors (fully managed RAG) - connects to 40+ popular enterprise data sources
- Users must be authenticated through IAM identity Center
- Users receive responses generated only from the documents they have access to
- IAM Identity Center can be configured with external identity providers
- Admin controls == Guardrails
- Global controls and topic level controls

## Amazon Q Apps

- Create Gen AI-powered apps without coding by using natuaral language
- It's based on company data like Amazon Q business

## Amazon Q Developer

- Amazon Q Developer is rebranded as "Kiro"
- Answer questions about the AWS documentation and AWS service selection
- Suggest CLI (Command Line Interface) to run to make changes to your account
- Helps you do bill analysis, resolve erros, troubleshooting..
- It works like a AI code companion
- Supports many languages: Java, Javascript, Python, C#...
- Integrates with IDE

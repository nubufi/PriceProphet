**PriceProphet** is a GenAI application designed to predict the price of a product based on its description. This project aims to combine state-of-the-art natural language processing (NLP) techniques with deep learning to build a robust pricing model. Leveraging the fine tuned **Llama model** from Hugging Face's library and deploying it via an intuitive frontend interface.

### Key Features:
1. **Data Collection and Preprocessing:**
   - Fetch product descriptions and price data from Hugging Face or other external sources.
   - Perform text cleaning, tokenization, and formatting for model training.

2. **Model Training and Fine-Tuning:**
   - Fine-tune the pre-trained **Llama model** on custom pricing data.
   - Use regression-based approaches to predict continuous price values from text descriptions.

3. **Evaluation and Validation:**
   - Measure model performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
   - Conduct thorough evaluation to ensure accuracy and generalizability.

4. **Deployment with Gradio:**
   - Provide a user-friendly interface for product price prediction.
   - Allow users to input product descriptions and receive instant price estimates.

5. **Integration with Hugging Face:**
   - Leverage Hugging Face's ecosystem for data management, model hosting, and deployment.
   - Upload the trained model back to Hugging Face for public sharing and accessibility.

---

### Objectives:
- Build a comprehensive understanding of the NLP model fine-tuning process.
- Explore regression tasks using LLMs in a practical, business-oriented context.
- Gain hands-on experience with Hugging Face tools and APIs for data and model management.
- Develop a functional, interactive Gradio application to showcase the model's capabilities.

---

### Technologies Used:
- **Backend:**
    - Hugging Face Transformers (Llama model)
    - PyTorch/TensorFlow
    - Flask

- **Frontend:**
    - Gradio for the interactive interface

- **Infrastructure:**
    - Hugging Face Datasets and Model Hub
    - Docker for containerization

---

### Use Cases:
- **E-commerce platforms** can leverage this model to estimate product prices based on user-submitted descriptions.
- **Market researchers** can analyze trends by predicting prices from textual data.
- **Small businesses** can quickly determine price ranges for products without extensive market research.

---

### Why This Project?
PriceProphet is an excellent project for anyone seeking to enhance their machine learning and NLP skills while solving a real-world problem. It provides hands-on experience in data processing, model training, evaluation, and deployment, making it a perfect side project for learning and skill development.

### Requirements
1- A system with nvidia graphic card
2- Docker and docker compose

### How To Run?
1- Create an .env file inside the app directory and add your hugging face token as HF_TOKEN=<your token>.
2- Run docker-compose up --build.
